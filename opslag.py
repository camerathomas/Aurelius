"""
Aurelius — een filosofische coach-app.
Start met: python -m streamlit run app.py
"""

import streamlit as st
import time
from datetime import datetime

# Eigen modules
from filosofen import (
    FILOSOFEN,
    STANDAARD_PANTHEON,
    beschikbare_filosofen,
    PANTHEON_PER_LEVEL,
)
from coach import bouw_coach_prompt, kies_filosoof, chat
from evaluatie import (
    EVALUATIE_RONDE_1,
    EVALUATIE_RONDE_2,
    EVALUATIE_AFSLUITER,
    haal_reacties_op,
    bouw_context,
    bepaal_meest_gesproken,
    verzamel_alle_reacties,
    bereken_leestijd,
)
from wendingen import kies_random_wending, moet_wending_komen


# ============================================================
# Configuratie
# ============================================================
st.set_page_config(
    page_title="Aurelius",
    page_icon="🏛️",
    layout="centered"
)


# ============================================================
# Database-check
# ============================================================
def check_database():
    try:
        secrets = st.secrets["connections"]["aurelius"]
    except KeyError:
        return False, (
            "**Database-configuratie niet gevonden.**\n\n"
            "Ga naar **Settings → Secrets** in Streamlit Cloud en zorg dat er staat:\n"
            "```toml\n[connections.aurelius]\nurl = \"libsql://...\"\nauth_token = \"...\"\n```\n\n"
            "**Belangrijk:** klik daarna op **Reboot**."
        )
    if "url" not in secrets:
        return False, "De sleutel `url` ontbreekt."
    if "auth_token" not in secrets:
        return False, "De sleutel `auth_token` ontbreekt."
    return True, None


db_ok, db_fout = check_database()
if not db_ok:
    st.error("⚠️ **Database niet beschikbaar**")
    st.markdown(db_fout)
    st.stop()

from opslag import (
    initialiseer, laad_profiel, bewaar_profiel,
    bewaar_bericht, laad_gesprek, wis_gesprek,
    bewaar_sessie, laad_sessies, laad_sessie,
)

try:
    initialiseer()
except Exception as e:
    st.error(f"⚠️ **Database-fout:** {e}")
    st.stop()

# API-sleutel voor Gemini
api_key = st.secrets["connections"]["aurelius"]["GEMINI_API_KEY"]


# ============================================================
# Hulp-functies
# ============================================================
def archiveer_sessie(profiel, geschiedenis, rondes, afsluiter, api_key):
    """Slaat de sessie op in het archief in de database."""
    gebruiker_id = st.session_state.get("huidige_gebruiker", "remco")
    incheck = profiel.get("laatste_incheck", {})
    duur = profiel.get("sessie_duur", 10)
    pantheon_nu = st.session_state.get("pantheon", [])

    # Bepaal het thema met de AI
    thema = "onbekend"
    try:
        client = genai.Client(api_key=api_key)
        gesprek_tekst = "\n".join(
            f"{b['naam']}: {b['tekst']}" for b in geschiedenis[-10:]
        )
        prompt = (
            "Geef in maximaal 5 woorden het thema van dit gesprek. "
            "Alleen het thema, geen uitleg, geen punctuatie.\n\n"
            + gesprek_tekst
        )
        thema_antwoord, _ = vraag_ai(client, prompt)
        thema = thema_antwoord.strip()[:60]
    except Exception:
        # Fallback: gebruik het eerste bericht van de gebruiker
        for b in geschiedenis:
            if b["naam"] == "Jij":
                thema = b["tekst"][:60]
                break

    try:
        bewaar_sessie(
            gebruiker_id=gebruiker_id,
            thema=thema,
            incheck=incheck,
            gesprek=geschiedenis,
            rondes=rondes or {},
            afsluiter=afsluiter or {},
            duur_minuten=duur,
            pantheon=pantheon_nu,
        )
    except Exception as e:
        st.error(f"Fout bij archiveren: {e}")


def reset_voor_nieuwe_sessie():
    """Reset alles behalve het profiel, zodat een nieuwe sessie kan beginnen."""
    st.session_state.geschiedenis = []
    st.session_state.incheck = {}
    st.session_state.incheck_stap = 0
    st.session_state.incheck_afgerond = False
    st.session_state.grote_wending_geweest = False
    st.session_state.evaluatie_gestart = False
    st.session_state.evaluatie_context = ""
    st.session_state.evaluatie_rondes = None
    st.session_state.evaluatie_afsluiter = None
    st.session_state.evaluatie_stap = 0
    st.session_state.evaluatie_afgerond = False
    st.session_state.archief_gevraagd = False
    st.session_state.archief_opgeslagen = False
    st.session_state.eind_keuze_gemaakt = False
    st.session_state.nazit_gestart = False
    st.session_state.einde = False
    st.session_state.wendingen_geweest = []
    st.session_state.huidige_wending_label = None
    st.session_state.huidige_wending = None
    st.session_state.beurten_teller = {}
    st.session_state.voorzitter = None
    st.session_state.pantheon = None
    st.session_state.eerste_gesprek_gestart = False
    st.session_state.profiel["sessie_tijd"] = 0
    st.session_state.profiel["sessie_start"] = time.time()
    st.session_state.profiel["laatste_bericht"] = time.time()
    st.rerun()


def veilige_duur(profiel):
    """Haalt de sessieduur op en zorgt dat het altijd een getal is."""
    duur = profiel.get("sessie_duur", 10)
    try:
        duur = int(duur)
    except (ValueError, TypeError):
        duur = 10
    if duur <= 0:
        duur = 10
    return duur


def kies_filosoof_met_verdeling(pantheon, voorzitter, teller):
    """
    Kiest een filosoof op basis van een 60/10-verdeling.
    De voorzitter krijgt 60% van de beurten, de rest elk 10%.
    """
    if not pantheon:
        return "marcus_aurelius"

    totaal = sum(teller.values()) + 1

    doel = {}
    for f in pantheon:
        if f == voorzitter:
            doel[f] = 0.6
        else:
            doel[f] = 0.4 / max(1, len(pantheon) - 1)

    tekort = {}
    for f in pantheon:
        huidig = teller.get(f, 0) / totaal
        tekort[f] = doel[f] - huidig

    return max(tekort, key=tekort.get)


def bouw_pantheon_voor_sessie(profiel):
    """
    Bepaalt het pantheon voor deze sessie.
    - Als de gebruiker het eigen pantheon wil, gebruik dat.
    - Anders het standaard pantheon van het level.
    """
    if profiel.get("gebruik_eigen_pantheon", False):
        eigen = profiel.get("eigen_pantheon", [])
        if eigen:
            return eigen

    huidig_level = profiel.get("level", 1)
    return PANTHEON_PER_LEVEL.get(huidig_level, PANTHEON_PER_LEVEL.get(1, []))


# ============================================================
# Fasen
# ============================================================
FASE_PERCENTAGES = {
    "opening":    (0.00, 0.10),
    "verkennen":  (0.10, 0.30),
    "verdiepen":  (0.30, 0.60),
    "verbreden":  (0.60, 0.80),
    "integreren": (0.80, 0.92),
    "afsluiten":  (0.92, 1.00),
}

FASE_VOLGORDE = ["opening", "verkennen", "verdiepen", "verbreden", "integreren", "afsluiten"]

VRAGEN_PER_FASE = {
    "opening":    ["Waar wil je beginnen?", "Wat speelt er?", "Wat houdt je bezig?"],
    "verkennen":  ["Wat valt je op?", "Wat gebeurt er als je hieraan denkt?", "Wat maakt dit belangrijk?"],
    "verdiepen":  ["Wat zit eronder?", "Wat raakt je hierin?", "Wat vermijd je?"],
    "verbreden":  ["Welke perspectieven zijn er?", "Wat zou een filosoof zeggen?", "Wat als het tegenovergestelde waar is?"],
    "integreren": ["Wat neem je mee?", "Wat ga je doen?", "Wat is je volgende stap?"],
    "afsluiten":  ["Wat was belangrijk vandaag?", "Wat neem je mee naar de volgende keer?"],
}


# ============================================================
# Tijdsysteem
# ============================================================
PAUZE_DREMPEL = 90
BASIS_MARGE = 30
VERSNELLING = 1


def update_sessie_tijd(profiel):
    nu = time.time()
    laatste = profiel.get("laatste_bericht", nu)
    verschil = (nu - laatste) * VERSNELLING

    if verschil < PAUZE_DREMPEL:
        profiel["sessie_tijd"] = profiel.get("sessie_tijd", 0) + verschil
    else:
        profiel["sessie_tijd"] = profiel.get("sessie_tijd", 0) + BASIS_MARGE

    profiel["laatste_bericht"] = nu
    return profiel


def bereken_sessie_minuten(profiel):
    return profiel.get("sessie_tijd", 0) / 60


def bepaal_fase(profiel):
    minuten = bereken_sessie_minuten(profiel)
    duur = veilige_duur(profiel)
    percentage = minuten / duur

    for fase, (start, eind) in FASE_PERCENTAGES.items():
        if start <= percentage < eind:
            return fase
    return "nazit"


def check_einde_sessie(profiel):
    minuten = bereken_sessie_minuten(profiel)
    duur = veilige_duur(profiel)
    fase = bepaal_fase(profiel)

    if minuten >= duur and fase != "afsluiten":
        return (
            "De sessietijd is om, maar we zijn nog niet bij de afsluiting. "
            "Vraag de gebruiker: 'We hebben nog niet alle fasen doorlopen. "
            "Wil je een paar minuten extra om af te ronden, of zullen we "
            "het de volgende keer afmaken?'"
        )
    return None


# ============================================================
# Incheck-vragen
# ============================================================
INCHECK_VRAGEN = [
    {"sleutel": "openheid",
     "vraag": "Wat gaat er om in je bewustzijn? Wat speelt er vandaag? Waar wil je het over hebben?",
     "type": "tekst",
     "placeholder": "Vertel vrijuit — er is geen goed of fout antwoord."},
    {"sleutel": "emotie", "vraag": "Hoe gaat het vandaag?", "type": "tekst",
     "placeholder": "Bijvoorbeeld: druk, moe, rustig..."},
    {"sleutel": "overzicht", "vraag": "Heb je overzicht over je leven?", "type": "slider",
     "min": 1, "max": 10, "default": 5, "toelichting": "1 = geen, 10 = volledig"},
    {"sleutel": "intentie", "vraag": "Wat wil je vandaag?", "type": "keuze",
     "opties": ["Even praten", "Iets bespreken", "Iets onderzoeken", "Iets vieren"]},
    {"sleutel": "volgorde", "vraag": "Zet deze vier op volgorde van belangrijkheid.",
     "type": "sorteren", "opties": ["Respect", "Vertrouwen", "Verbinding", "Analyse"]},
    {"sleutel": "duur", "vraag": "Hoe lang heb je?", "type": "keuze",
     "opties": ["Flitsgesprek (5 min)", "Kort gesprek (10 min)",
                "Standaard (20 min)", "Diep (30 min)"]},
    {"sleutel": "modus", "vraag": "Wie wil je spreken?", "type": "keuze",
     "opties": ["Automatisch — de coach kiest", "Zelf kiezen", "Verrassen"]},
]


# ============================================================
# Sidebar
# ============================================================
st.sidebar.title("🏛️ Aurelius")
st.sidebar.caption("Jouw filosofische metgezel")

gebruiker_id = st.sidebar.text_input("Vul hier je naam in", value="")

level = st.session_state.get("profiel", {}).get("level", 1)
st.sidebar.markdown(f"### 🎯 Level {level}")

st.sidebar.markdown("---")
st.sidebar.subheader("🔌 Model")

provider = st.sidebar.selectbox("Provider", ["Gemini", "Ollama"])

if provider == "Gemini":
    model_naam = st.sidebar.selectbox("Model", ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite"])
    provider_key = "gemini"
else:
    model_naam = st.sidebar.selectbox("Model", ["llama3.2:latest", "qwen3:4b-q4_K_M"])
    provider_key = "ollama"

st.sidebar.markdown("---")
st.sidebar.subheader("🎭 Pantheon")

# Bepaal welk pantheon getoond wordt in de sidebar:
# het eigen pantheon als de gebruiker dat heeft gekozen, anders het standaard.
_sidebar_pantheon = st.session_state.get("pantheon")
if not _sidebar_pantheon:
    _eigen = st.session_state.get("profiel", {}).get("eigen_pantheon", [])
    _gebruik_eigen = st.session_state.get("profiel", {}).get("gebruik_eigen_pantheon", False)
    if _gebruik_eigen and _eigen:
        _sidebar_pantheon = _eigen
    else:
        _sidebar_pantheon = PANTHEON_PER_LEVEL.get(level, PANTHEON_PER_LEVEL.get(1, []))

pantheon = _sidebar_pantheon  # wordt verderop in het gesprek gebruikt

with st.sidebar.expander("Jouw pantheon", expanded=False):
    for f in pantheon:
        if f in FILOSOFEN:
            st.markdown(f"{FILOSOFEN[f]['emoji']} **{FILOSOFEN[f]['naam']}**")

if pantheon:
    with st.sidebar.expander("🎩 Voorzitter", expanded=False):
        huidige_vz = st.session_state.get("voorzitter") or pantheon[0]
        if huidige_vz not in pantheon:
            huidige_vz = pantheon[0]
        nieuwe_vz = st.selectbox(
            "Kies een voorzitter",
            options=pantheon,
            index=pantheon.index(huidige_vz),
            format_func=lambda x: f"{FILOSOFEN[x]['emoji']} {FILOSOFEN[x]['naam']}",
            key="voorzitter_select"
        )
        if nieuwe_vz != huidige_vz:
            st.session_state.voorzitter = nieuwe_vz
            st.rerun()

st.sidebar.markdown("---")
st.sidebar.subheader("🔧 Parameters")

max_historie = st.sidebar.slider("Max. berichten in context", 4, 40, 12, 2)

st.sidebar.markdown("---")
if st.sidebar.button("📊 Dashboard"):
    st.session_state.toon_dashboard = True
    st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🗑️ Wis alle gesprekken"):
    try:
        wis_gesprek(gebruiker_id)
        st.session_state.geschiedenis = []
        st.session_state.incheck_afgerond = False
        st.session_state.incheck = {}
        st.session_state.incheck_stap = 0
        st.session_state.grote_wending_geweest = False
        st.session_state.evaluatie_gestart

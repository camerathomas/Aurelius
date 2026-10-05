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


# ============================================================
# Hulp-functies
# ============================================================
def archiveer_sessie(profiel, geschiedenis, rondes, afsluiter):
    """Slaat de sessie op in het archief in de database."""
    gebruiker_id = st.session_state.get("huidige_gebruiker", "remco")
    incheck = profiel.get("laatste_incheck", {})
    duur = profiel.get("sessie_duur", 10)
    pantheon_nu = st.session_state.get("pantheon", [])

    thema = incheck.get("openheid", "")[:80] if incheck.get("openheid") else "onbekend"

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
    Bepaalt het pantheon voor deze sessie op basis van het level.
    """
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
     "opties": ["Kort (10 min)", "Standaard (20 min)", "Diep (30 min)"]},
    {"sleutel": "modus", "vraag": "Wie wil je spreken?", "type": "keuze",
     "opties": ["Automatisch — de coach kiest", "Zelf kiezen", "Verrassen"]},
]


# ============================================================
# Sidebar
# ============================================================
st.sidebar.title("🏛️ Aurelius")
st.sidebar.caption("Jouw filosofische metgezel")

gebruiker_id = st.sidebar.text_input("Gebruikersnaam", value="remco")

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

pantheon = PANTHEON_PER_LEVEL.get(level, PANTHEON_PER_LEVEL.get(1, []))

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
if st.sidebar.button("🗑️ Wis alle gesprekken"):
    try:
        wis_gesprek(gebruiker_id)
        st.session_state.geschiedenis = []
        st.session_state.incheck_afgerond = False
        st.session_state.incheck = {}
        st.session_state.incheck_stap = 0
        st.session_state.grote_wending_geweest = False
        st.session_state.evaluatie_gestart = False
        st.session_state.evaluatie_context = ""
        st.session_state.evaluatie_rondes = None
        st.session_state.evaluatie_afsluiter = None
        st.session_state.evaluatie_stap = 0
        st.session_state.beurten_teller = {}
        st.sidebar.success("Gewist.")
        st.rerun()
    except Exception as e:
        st.sidebar.error(f"Fout: {e}")


# ============================================================
# Sessie-state
# ============================================================
if "incheck" not in st.session_state:
    st.session_state.incheck = {}
if "incheck_stap" not in st.session_state:
    st.session_state.incheck_stap = 0
if "incheck_afgerond" not in st.session_state:
    st.session_state.incheck_afgerond = False
if "geschiedenis" not in st.session_state:
    st.session_state.geschiedenis = []
if "profiel" not in st.session_state:
    st.session_state.profiel = laad_profiel(gebruiker_id)
if "grote_wending_geweest" not in st.session_state:
    st.session_state.grote_wending_geweest = False
if "evaluatie_gestart" not in st.session_state:
    st.session_state.evaluatie_gestart = False
if "evaluatie_context" not in st.session_state:
    st.session_state.evaluatie_context = ""
if "evaluatie_rondes" not in st.session_state:
    st.session_state.evaluatie_rondes = None
if "evaluatie_afsluiter" not in st.session_state:
    st.session_state.evaluatie_afsluiter = None
if "evaluatie_stap" not in st.session_state:
    st.session_state.evaluatie_stap = 0
if "archief_gevraagd" not in st.session_state:
    st.session_state.archief_gevraagd = False
if "archief_opgeslagen" not in st.session_state:
    st.session_state.archief_opgeslagen = False
if "eind_keuze_gemaakt" not in st.session_state:
    st.session_state.eind_keuze_gemaakt = False
if "nazit_gestart" not in st.session_state:
    st.session_state.nazit_gestart = False
if "einde" not in st.session_state:
    st.session_state.einde = False
if "evaluatie_afgerond" not in st.session_state:
    st.session_state.evaluatie_afgerond = False
if "wendingen_geweest" not in st.session_state:
    st.session_state.wendingen_geweest = []
if "huidige_wending_label" not in st.session_state:
    st.session_state.huidige_wending_label = None
if "huidige_wending" not in st.session_state:
    st.session_state.huidige_wending = None
if "beurten_teller" not in st.session_state:
    st.session_state.beurten_teller = {}
if "voorzitter" not in st.session_state:
    st.session_state.voorzitter = None

if "welkom_geweest" not in st.session_state.profiel:
    st.session_state.profiel["welkom_geweest"] = False
if "proefsessie_geweest" not in st.session_state.profiel:
    st.session_state.profiel["proefsessie_geweest"] = False
if "proef_gestart" not in st.session_state.profiel:
    st.session_state.profiel["proef_gestart"] = False
if "betaald" not in st.session_state.profiel:
    st.session_state.profiel["betaald"] = False
if "incheck_gedaan" not in st.session_state.profiel:
    st.session_state.profiel["incheck_gedaan"] = False

if "level" not in st.session_state.profiel:
    st.session_state.profiel["level"] = 1

if st.session_state.get("huidige_gebruiker") != gebruiker_id:
    st.session_state.profiel = laad_profiel(gebruiker_id)
    if "level" not in st.session_state.profiel:
        st.session_state.profiel["level"] = 1
    st.session_state.huidige_gebruiker = gebruiker_id
    opgeslagen = laad_gesprek(gebruiker_id, limiet=max_historie * 2)
    st.session_state.geschiedenis = [
        {
            "naam": b["filosoof"] if b["rol"] == "assistant" else "Jij",
            "tekst": b["tekst"],
            "icoon": FILOSOFEN.get(b["filosoof"], {}).get("emoji", "🏛️") if b["rol"] == "assistant" else "🧑",
            "tijd": str(b["tijd"])[11:16] if b.get("tijd") else "",
        }
        for b in opgeslagen
    ]
    if st.session_state.geschiedenis:
        st.session_state.incheck_afgerond = True
        st.session_state.incheck = st.session_state.profiel.get("laatste_incheck", {})
    else:
        st.session_state.incheck = {}
        st.session_state.incheck_stap = 0
        st.session_state.incheck_afgerond = False

# ============================================================
# Hoofdinterface
# ============================================================
st.title("🏛️ Aurelius")
st.caption("Een filosofische coach, geïnspireerd door Marcus Aurelius.")


# ============================================================
# Welkomstscherm
# ============================================================
if not st.session_state.profiel.get("welkom_geweest", False):
    st.markdown("---")
    st.markdown("## 🏛️ Welkom bij Aurelius")
    st.markdown("**Marcus Aurelius:**")
    st.markdown(
        "Ik ben Marcus Aurelius. Ik was keizer van Rome, en ik schreef "
        "elke dag aan mezelf — over wat ik wel en niet in de hand had, "
        "over wat ik kon veranderen en wat ik moest laten.\n\n"
        "Deze app is geen therapeut, geen adviseur, geen antwoordenmachine. "
        "Het is een plek om te denken. Met filosofen die je uitnodigen om "
        "zelf te kijken, zelf te vragen, zelf te kiezen.\n\n"
        "Elke sessie nodigen we een pantheon van filosofen uit. Ze komen "
        "uit verschillende tradities, en elk kijkt op een andere manier "
        "naar wat je meebrengt. Je hoeft ze niet te kennen. Je hoeft het "
        "niet eens te zijn. Je hoeft alleen maar te luisteren, en te "
        "antwoorden.\n\n"
        "Ik raad je aan om alle filosofen eens te proberen. Niet omdat ze "
        "allemaal gelijk hebben, maar omdat elke stem je iets laat zien "
        "dat je alleen niet zo snel zou zien.\n\n"
        "Begin rustig. Er is geen goed of fout gesprek. Er is alleen wat "
        "je opmerkt, en wat je ermee doet.\n\n"
        "Welkom."
    )

    if st.button("Verder", type="primary"):
        st.session_state.profiel["welkom_geweest"] = True
        bewaar_profiel(st.session_state.profiel)
        st.rerun()

    st.stop()


# ============================================================
# Proefsessie — 5 minuten, level 1, Marcus Aurelius als voorzitter
# ============================================================
if not st.session_state.profiel.get("proefsessie_geweest", False):

    st.markdown("---")
    st.markdown("## 🕐 Proefsessie")
    st.caption("Een korte kennismaking van 5 minuten.")

    # Pantheon voor de proefsessie
    proef_pantheon = PANTHEON_PER_LEVEL.get(1, [])
    st.session_state.pantheon = proef_pantheon

    if not st.session_state.get("voorzitter") and proef_pantheon:
        st.session_state.voorzitter = proef_pantheon[0]

    # Sessietijd instellen op 5 minuten, eenmalig
    if not st.session_state.profiel.get("proef_gestart", False):
        st.session_state.profiel["sessie_duur"] = 5
        st.session_state.profiel["sessie_tijd"] = 0
        st.session_state.profiel["sessie_start"] = time.time()
        st.session_state.profiel["laatste_bericht"] = time.time()
        st.session_state.profiel["proef_gestart"] = True
        bewaar_profiel(st.session_state.profiel)

    # Toon het gesprek
    gesprek_container = st.container()

    def toon_proef_bericht(naam, tekst, icoon, tijd=None):
        with gesprek_container:
            with st.chat_message(naam, avatar=icoon):
                if tijd:
                    st.markdown(f"**{naam}** · _{tijd}_")
                else:
                    st.markdown(f"**{naam}**")
                st.markdown(tekst)

    for b in st.session_state.geschiedenis:
        toon_proef_bericht(b["naam"], b["tekst"], b["icoon"], b.get("tijd"))

    # Eerste beurt: Marcus Aurelius stelt de openingsvraag
    if not st.session_state.geschiedenis:
        filosoof_naam = "marcus_aurelius"
        filosoof = FILOSOFEN[filosoof_naam]

        proef_prompt = (
            "Dit is de PROEFSESSIE. De gebruiker heeft net het "
            "welkomstwoord gelezen, en dit is het eerste gesprek.\n\n"
            "Jouw taak: stel ÉÉN openingsvraag aan de gebruiker. Kies uit "
            "deze drie vragen, of een variant daarop:\n"
            "- 'Waar denk jij aan als je het woord filosofie hoort?'\n"
            "- 'Wat hoop je hier te vinden?'\n"
            "- 'Heb je eerder met filosofie te maken gehad?'\n\n"
            "Stel er één. Kort, direct, uitnodigend."
        )

        with st.spinner(f"{filosoof['naam']} denkt na..."):
            eerste_vraag = chat(
                model=model_naam,
                messages=[{"role": "user", "content": proef_prompt}],
                system_prompt=bouw_coach_prompt(
                    filosoof=filosoof,
                    profiel=st.session_state.profiel,
                    modus="Coach",
                    fase="opening",
                    vragen=[],
                ),
                provider=provider_key,
            )

        st.session_state.geschiedenis.append({
            "naam": filosoof["naam"], "tekst": eerste_vraag,
            "icoon": filosoof["emoji"], "tijd": datetime.now().strftime("%H:%M"),
        })
        try:
            bewaar_bericht(gebruiker_id, filosoof["naam"], "assistant", eerste_vraag)
        except Exception:
            pass
        st.rerun()

    # Invoer van de gebruiker
    proef_input = None
    if not st.session_state.get("evaluatie_gestart", False):
        proef_input = st.chat_input("Typ je antwoord...")

    if proef_input:
        tijd = datetime.now().strftime("%H:%M")
        st.session_state.geschiedenis.append({
            "naam": "Jij", "tekst": proef_input, "icoon": "🧑", "tijd": tijd,
        })
        try:
            bewaar_bericht(gebruiker_id, "Jij", "user", proef_input)
        except Exception:
            pass

        st.session_state.profiel = update_sessie_tijd(st.session_state.profiel)

        if proef_pantheon and st.session_state.get("voorzitter"):
            filosoof_naam = kies_filosoof_met_verdeling(
                proef_pantheon,
                st.session_state.voorzitter,
                st.session_state.beurten_teller,
            )
        else:
            filosoof_naam = "marcus_aurelius"

        filosoof = FILOSOFEN[filosoof_naam]

        system_prompt = bouw_coach_prompt(
            filosoof=filosoof,
            profiel=st.session_state.profiel,
            modus="Coach",
            fase=None,
            vragen=[],
        )

        context = st.session_state.geschiedenis[-max_historie:]
        messages = []
        for b in context[:-1]:
            rol = "assistant" if b["naam"] != "Jij" else "user"
            messages.append({"role": rol, "content": b["tekst"]})
        messages.append({"role": "user", "content": proef_input})

        with st.spinner(f"{filosoof['naam']} denkt na..."):
            antwoord = chat(
                model=model_naam,
                messages=messages,
                system_prompt=system_prompt,
                provider=provider_key,
            )

        tijd = datetime.now().strftime("%H:%M")
        st.session_state.geschiedenis.append({
            "naam": filosoof["naam"], "tekst": antwoord,
            "icoon": filosoof["emoji"], "tijd": tijd,
        })
        try:
            bewaar_bericht(gebruiker_id, filosoof["naam"], "assistant", antwoord)
        except Exception:
            pass

        st.session_state.beurten_teller[filosoof_naam] = (
            st.session_state.beurten_teller.get(filosoof_naam, 0) + 1
        )

        try:
            bewaar_profiel(st.session_state.profiel)
        except Exception:
            pass

        st.rerun()

    # Einde proefsessie: evaluatie starten
    minuten = bereken_sessie_minuten(st.session_state.profiel)
    if (minuten >= 5
            and not st.session_state.evaluatie_gestart
            and st.session_state.geschiedenis):

        voorzitter = st.session_state.get("voorzitter")
        if voorzitter and voorzitter in FILOSOFEN:
            st.session_state.evaluatie_context = bouw_context(
                st.session_state.profiel,
                st.session_state.geschiedenis,
                proef_pantheon,
            )
            st.session_state.evaluatie_context += (
                f"\n\n--- VOORZITTER ---\n"
                f"De voorzitter van deze sessie is {FILOSOFEN[voorzitter]['naam']}. "
                f"Laat de voorzitter NIET meedoen in ronde 1 en ronde 2. "
                f"De voorzitter komt alleen terug in de afsluiter."
            )
            st.session_state.evaluatie_gestart = True
            st.session_state.evaluatie_stap = 0
            st.rerun()

    if not st.session_state.get("evaluatie_gestart", False):
        st.stop()


# ============================================================
# Betaalmuur
# ============================================================
if not st.session_state.profiel.get("betaald", False):
    st.markdown("---")
    st.markdown("## 🕊️ Uw proeftijd is voorbij")
    st.markdown(
        "Uw proeftijd is voorbij. Als u verder wilt gaan, kunt u zich "
        "aanmelden en betalen. Daarna kunt u de pdf downloaden en "
        "verdergaan met de gesprekken."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📁 Archiveer en betaal")
        if st.button("Ik heb betaald", type="primary"):
            st.session_state.profiel["betaald"] = True
            bewaar_profiel(st.session_state.profiel)
            st.rerun()

    with col2:
        st.markdown("### 👋 Uw proeftijd is voorbij")
        st.caption("U kunt dit tabblad sluiten. Bedankt voor het proberen.")

    st.stop()


# ============================================================
# Incheck — eenmalig, na betaling
# ============================================================
if not st.session_state.profiel.get("incheck_gedaan", False):

    st.markdown("---")
    st.markdown("### 👋 Welkom")
    st.markdown("Even een paar vragen voordat we beginnen.")

    stap = st.session_state.incheck_stap
    totaal = len(INCHECK_VRAGEN)

    st.progress(stap / totaal, text=f"Vraag {stap + 1} van {totaal}" if stap < totaal else "Klaar")

    if stap < totaal:
        vraag = INCHECK_VRAGEN[stap]
        st.markdown(f"**{vraag['vraag']}**")

        if vraag["type"] == "tekst":
            antwoord = st.text_input("Antwoord", placeholder=vraag.get("placeholder", ""),
                                     label_visibility="collapsed", key=f"incheck_{vraag['sleutel']}")
            if st.button("Volgende ➡️"):
                if antwoord.strip():
                    st.session_state.incheck[vraag["sleutel"]] = antwoord.strip()
                    st.session_state.incheck_stap += 1
                    st.rerun()
                else:
                    st.warning("Vul iets in.")

        elif vraag["type"] == "slider":
            if vraag.get("toelichting"):
                st.caption(vraag["toelichting"])
            antwoord = st.slider("Score", vraag["min"], vraag["max"], vraag["default"],
                                 label_visibility="collapsed", key=f"incheck_{vraag['sleutel']}")
            if st.button("Volgende ➡️"):
                st.session_state.incheck[vraag["sleutel"]] = antwoord
                st.session_state.incheck_stap += 1
                st.rerun()

        elif vraag["type"] == "keuze":
            antwoord = st.radio("Keuze", vraag["opties"], label_visibility="collapsed",
                                key=f"incheck_{vraag['sleutel']}")
            if st.button("Volgende ➡️"):
                st.session_state.incheck[vraag["sleutel"]] = antwoord
                st.session_state.incheck_stap += 1
                st.rerun()

        elif vraag["type"] == "sorteren":
            opties = vraag["opties"]
            st.markdown("**1e plaats** (belangrijkst)")
            pos1 = st.selectbox("1e", opties, key="sort_pos1", label_visibility="collapsed")
            st.markdown("**2e plaats**")
            opties_2 = [o for o in opties if o != pos1]
            pos2 = st.selectbox("2e", opties_2, key="sort_pos2", label_visibility="collapsed")
            st.markdown("**3e plaats**")
            opties_3 = [o for o in opties_2 if o != pos2]
            pos3 = st.selectbox("3e", opties_3, key="sort_pos3", label_visibility="collapsed")
            pos4 = [o for o in opties_3 if o != pos3][0]
            st.markdown(f"**4e plaats**: {pos4}")
            if st.button("Volgende ➡️"):
                st.session_state.incheck["volgorde"] = [pos1, pos2, pos3, pos4]
                st.session_state.incheck_stap += 1
                st.rerun()

    else:
        st.markdown("### ✅ Klaar")
        incheck = st.session_state.incheck
        st.markdown(f"- **Wat speelt er**: {incheck.get('openheid', '—')}")
        st.markdown(f"- **Emotie**: {incheck.get('emotie', '—')}")
        st.markdown(f"- **Overzicht**: {incheck.get('overzicht', '—')}/10")
        st.markdown(f"- **Intentie**: {incheck.get('intentie', '—')}")
        volgorde = incheck.get("volgorde", [])
        if volgorde:
            st.markdown(f"- **Volgorde**: {' → '.join(volgorde)}")
        st.markdown(f"- **Duur**: {incheck.get('duur', '—')}")

        if st.button("🚀 Start gesprek", type="primary"):
            st.session_state.incheck_afgerond = True
            st.session_state.profiel["laatste_incheck"] = incheck
            st.session_state.profiel["openheid"] = incheck.get("openheid", "")
            st.session_state.profiel["themas"] = [incheck.get("emotie", "")]
            st.session_state.profiel["waarde_volgorde"] = incheck.get("volgorde", [])

            duur_map = {"Kort (10 min)": 10, "Standaard (20 min)": 20, "Diep (30 min)": 30}
            gekozen_duur = incheck.get("duur", "")
            st.session_state.profiel["sessie_duur"] = duur_map.get(gekozen_duur, 10)
            st.session_state.profiel["sessie_start"] = time.time()
            st.session_state.profiel["sessie_tijd"] = 0
            st.session_state.profiel["laatste_bericht"] = time.time()
            st.session_state.profiel["incheck_gedaan"] = True

            st.session_state.grote_wending_geweest = False
            st.session_state.evaluatie_gestart = False
            st.session_state.evaluatie_context = ""
            st.session_state.evaluatie_rondes = None
            st.session_state.evaluatie_afsluiter = None
            st.session_state.evaluatie_stap = 0
            st.session_state.wendingen_geweest = []
            st.session_state.beurten_teller = {}

            nieuw_pantheon = bouw_pantheon_voor_sessie(st.session_state.profiel)
            st.session_state.voorzitter = nieuw_pantheon[0] if nieuw_pantheon else "marcus_aurelius"

            bewaar_profiel(st.session_state.profiel)
            st.rerun()

    st.stop()

# ============================================================
# Gesprek
# ============================================================
incheck = st.session_state.get("incheck", {})

st.session_state.profiel = update_sessie_tijd(st.session_state.profiel)

fase = bepaal_fase(st.session_state.profiel)
minuten = bereken_sessie_minuten(st.session_state.profiel)
duur = veilige_duur(st.session_state.profiel)
resterend = max(0, duur - minuten)

st.markdown("---")
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    st.markdown(f"**🕐 {minuten:.1f}** van **{duur}** min")
with col2:
    st.markdown(f"**📍 Fase:** {fase.capitalize()}")
with col3:
    if fase == "nazit":
        st.markdown("🌙 **Nazit**")
    else:
        st.markdown(f"⏳ **{resterend:.1f}** min")

huidige_idx = FASE_VOLGORDE.index(fase) if fase in FASE_VOLGORDE else len(FASE_VOLGORDE)
fase_weergave = ""
for i, f in enumerate(FASE_VOLGORDE):
    if i < huidige_idx:
        fase_weergave += f"✅ {f} "
    elif i == huidige_idx:
        fase_weergave += f"**▶️ {f}** "
    else:
        fase_weergave += f"⬜ {f} "
st.markdown(f"<small>{fase_weergave}</small>", unsafe_allow_html=True)

if incheck:
    with st.expander("📋 Jouw incheck", expanded=False):
        st.markdown(f"- **Wat speelt er**: {incheck.get('openheid', '—')}")
        st.markdown(f"- **Emotie**: {incheck.get('emotie', '—')}")
        st.markdown(f"- **Overzicht**: {incheck.get('overzicht', '—')}/10")
        st.markdown(f"- **Intentie**: {incheck.get('intentie', '—')}")
        volgorde = incheck.get("volgorde", [])
        if volgorde:
            st.markdown(f"- **Volgorde**: {' → '.join(volgorde)}")
        st.markdown(f"- **Duur**: {incheck.get('duur', '—')}")

gesprek_container = st.container()

def toon_bericht(naam, tekst, icoon, tijd=None):
    with gesprek_container:
        with st.chat_message(naam, avatar=icoon):
            if tijd:
                st.markdown(f"**{naam}** · _{tijd}_")
            else:
                st.markdown(f"**{naam}**")
            st.markdown(tekst)

for b in st.session_state.geschiedenis:
    toon_bericht(b["naam"], b["tekst"], b["icoon"], b.get("tijd"))

# Eerste coach-beurt
if not st.session_state.geschiedenis:
    openheid = incheck.get("openheid", "")
    emotie = incheck.get("emotie", "")
    overzicht = incheck.get("overzicht", 5)
    intentie = incheck.get("intentie", "")
    volgorde = incheck.get("volgorde", [])

    start_pantheon = bouw_pantheon_voor_sessie(st.session_state.profiel)
    st.session_state.pantheon = start_pantheon

    if not st.session_state.get("voorzitter") and start_pantheon:
        st.session_state.voorzitter = start_pantheon[0]

    eerste_vraag_prompt = (
        f"De gebruiker heeft net de incheck ingevuld:\n"
        f"- Wat speelt er: {openheid}\n"
        f"- Emotie: {emotie}\n"
        f"- Overzicht: {overzicht}/10\n"
        f"- Intentie: {intentie}\n"
        f"- Waarde-volgorde: {' → '.join(volgorde)}\n\n"
        f"Jouw taak: stel nu ÉÉN openingsvraag aan de gebruiker. "
        f"Geen herhaling van de incheck, geen samenvatting. "
        f"Gewoon één vraag die voortkomt uit wat de gebruiker heeft gezegd, "
        f"en die het gesprek opent. Kort, direct, uitnodigend."
    )

    filosoof_naam = st.session_state.get("voorzitter") or "marcus_aurelius"
    filosoof = FILOSOFEN[filosoof_naam]

    system_prompt = bouw_coach_prompt(
        filosoof=filosoof,
        profiel=st.session_state.profiel,
        modus="Coach",
        fase="opening",
        vragen=VRAGEN_PER_FASE.get("opening", []),
    )

    with st.spinner(f"{filosoof['naam']} denkt na..."):
        eerste_vraag = chat(
            model=model_naam,
            messages=[{"role": "user", "content": eerste_vraag_prompt}],
            system_prompt=system_prompt,
            provider=provider_key,
        )

    st.session_state.geschiedenis.append({
        "naam": filosoof["naam"], "tekst": eerste_vraag,
        "icoon": filosoof["emoji"], "tijd": datetime.now().strftime("%H:%M"),
    })
    try:
        bewaar_bericht(gebruiker_id, filosoof["naam"], "assistant", eerste_vraag)
    except Exception:
        pass
    toon_bericht(filosoof["naam"], eerste_vraag, filosoof["emoji"], datetime.now().strftime("%H:%M"))

    st.session_state.beurten_teller[filosoof_naam] = (
        st.session_state.beurten_teller.get(filosoof_naam, 0) + 1
    )


# ============================================================
# Invoer van de gebruiker
# ============================================================
gebruiker_input = None
if not st.session_state.get("evaluatie_gestart", False):
    gebruiker_input = st.chat_input("Waar wil je het over hebben?")

if gebruiker_input:
    tijd = datetime.now().strftime("%H:%M")
    st.session_state.geschiedenis.append({
        "naam": "Jij", "tekst": gebruiker_input, "icoon": "🧑", "tijd": tijd,
    })
    try:
        bewaar_bericht(gebruiker_id, "Jij", "user", gebruiker_input)
    except Exception:
        pass
    toon_bericht("Jij", gebruiker_input, "🧑", tijd)

    st.session_state.profiel = update_sessie_tijd(st.session_state.profiel)
    fase = bepaal_fase(st.session_state.profiel)

    minuten = bereken_sessie_minuten(st.session_state.profiel)
    duur = veilige_duur(st.session_state.profiel)
    halverwege = minuten >= (duur / 2)
    wending_nodig = halverwege and not st.session_state.grote_wending_geweest

    drempel = moet_wending_komen(
        minuten, duur, st.session_state.wendingen_geweest
    )

    if wending_nodig:
        eerdere_filosofen = [
            b["naam"] for b in st.session_state.geschiedenis
            if b["naam"] != "Jij"
        ]
        andere_filosofen = [
            f for f in pantheon
            if FILOSOFEN[f]["naam"] not in eerdere_filosofen
        ] or pantheon

        if andere_filosofen:
            filosoof_naam = kies_filosoof(
                st.session_state.profiel, andere_filosofen, gebruiker_input
            )
        elif pantheon:
            filosoof_naam = kies_filosoof(
                st.session_state.profiel, pantheon, gebruiker_input
            )
        else:
            filosoof_naam = "marcus_aurelius"

        st.session_state.grote_wending_geweest = True

    elif drempel is not None:
        wending = kies_random_wending()
        st.session_state.huidige_wending = wending

        eerdere_filosofen = [
            b["naam"] for b in st.session_state.geschiedenis
            if b["naam"] != "Jij"
        ]
        kandidaten = [
            f for f in pantheon
            if FILOSOFEN[f]["naam"] not in eerdere_filosofen
        ]
        if not kandidaten:
            kandidaten = pantheon

        if kandidaten:
            filosoof_naam = kies_filosoof(
                st.session_state.profiel, kandidaten, gebruiker_input
            )
        elif pantheon:
            filosoof_naam = kies_filosoof(
                st.session_state.profiel, pantheon, gebruiker_input
            )
        else:
            filosoof_naam = "marcus_aurelius"

        st.session_state.wendingen_geweest.append(drempel)
        st.session_state.huidige_wending_label = wending["naam"]

    else:
        if pantheon and st.session_state.get("voorzitter"):
            filosoof_naam = kies_filosoof_met_verdeling(
                pantheon,
                st.session_state.voorzitter,
                st.session_state.beurten_teller,
            )
        elif pantheon:
            filosoof_naam = kies_filosoof(
                st.session_state.profiel, pantheon, gebruiker_input
            )
        else:
            filosoof_naam = "marcus_aurelius"

    filosoof = FILOSOFEN[filosoof_naam]

    system_prompt = bouw_coach_prompt(
        filosoof=filosoof,
        profiel=st.session_state.profiel,
        modus="Coach",
        fase=fase,
        vragen=VRAGEN_PER_FASE.get(fase, [])
    )

    if filosoof.get("naam") == "Socrates":
        aantal_socrates = sum(
            1 for b in st.session_state.geschiedenis
            if b.get("naam") == "Socrates"
        )
        if aantal_socrates >= 3:
            system_prompt += (
                "\n\n[ELENCHUS VOORBIJ]\n"
                "Je hebt de elenchus al gebruikt in de eerste beurten. "
                "Ga nu over op een gewoon filosofisch gesprek. Blijf "
                "onderzoekend en vriendelijk, maar herhaal niet steeds "
                "hetzelfde patroon van instemming-consequentie-tegenstrijdigheid."
            )

    if wending_nodig:
        system_prompt += (
            "\n\n[OVERGANGSMOMENT]\n"
            "We zijn halverwege de sessie. Je bent een andere filosoof dan "
            "degene die tot nu toe sprak. Jouw taak in deze beurt:\n"
            "1. Vat in 2-3 zinnen samen wat er tot nu toe besproken is, "
            "in jouw eigen woorden.\n"
            "2. Breng een nieuw perspectief in dat nog niet aan bod kwam.\n"
            "3. Eindig met één nieuwe vraag die het gesprek verder opent.\n"
            "Doe dit in één doorlopend bericht, geen kopjes, geen opsomming."
        )

    if drempel is not None and st.session_state.get("huidige_wending"):
        system_prompt += (
            f"\n\n[WENDING: {st.session_state.huidige_wending['naam'].upper()}]\n"
            f"{st.session_state.huidige_wending['instructie']}"
        )

    einde_check = check_einde_sessie(st.session_state.profiel)
    if einde_check:
        system_prompt += f"\n\n[EINDE SESSIE]\n{einde_check}"

    context = st.session_state.geschiedenis[-max_historie:]
    messages = []
    for b in context[:-1]:
        rol = "assistant" if b["naam"] != "Jij" else "user"
        messages.append({"role": rol, "content": b["tekst"]})

    if drempel is not None and st.session_state.get("huidige_wending"):
        user_content = (
            f"{gebruiker_input}\n\n"
            f"[INSTRUCTIE VOOR DEZE BEURT — DIT IS GEEN GEWONE BEURT]\n"
            f"{st.session_state.huidige_wending['instructie']}\n\n"
            f"Negeer je standaard coach-instructies voor deze ene beurt. "
            f"Doe alleen wat hierboven staat."
        )
    else:
        user_content = gebruiker_input

    messages.append({"role": "user", "content": user_content})

    with st.spinner(f"{filosoof['naam']} denkt na..."):
        antwoord = chat(
            model=model_naam,
            messages=messages,
            system_prompt=system_prompt,
            provider=provider_key
        )

    tijd = datetime.now().strftime("%H:%M")
    st.session_state.geschiedenis.append({
        "naam": filosoof["naam"], "tekst": antwoord,
        "icoon": filosoof["emoji"], "tijd": tijd,
    })
    try:
        bewaar_bericht(gebruiker_id, filosoof["naam"], "assistant", antwoord)
    except Exception:
        pass
    toon_bericht(filosoof["naam"], antwoord, filosoof["emoji"], tijd)

    if st.session_state.get("huidige_wending_label"):
        st.caption(f"🔄 Wending: {st.session_state.huidige_wending_label}")
        st.session_state.huidige_wending_label = None

    st.session_state.beurten_teller[filosoof_naam] = (
        st.session_state.beurten_teller.get(filosoof_naam, 0) + 1
    )

    try:
        bewaar_profiel(st.session_state.profiel)
    except Exception:
        pass


# ============================================================
# AFRONDING — automatisch starten zodra de coach heeft afgesloten
# ============================================================
fase_nu = bepaal_fase(st.session_state.profiel)

laatste_bericht = (
    st.session_state.geschiedenis[-1]
    if st.session_state.geschiedenis
    else None
)
laatste_is_coach = (
    laatste_bericht is not None
    and laatste_bericht.get("naam") != "Jij"
)

if (fase_nu in ("afsluiten", "nazit")
        and laatste_is_coach
        and not st.session_state.evaluatie_gestart
        and st.session_state.geschiedenis):
    st.session_state.evaluatie_gestart = True
    st.session_state.evaluatie_stap = 0
    st.session_state.evaluatie_context = bouw_context(
        st.session_state.profiel,
        st.session_state.geschiedenis,
        pantheon,
    )

    voorzitter = st.session_state.get("voorzitter")
    if voorzitter and voorzitter in FILOSOFEN:
        st.session_state.evaluatie_context += (
            f"\n\n--- VOORZITTER ---\n"
            f"De voorzitter van deze sessie is {FILOSOFEN[voorzitter]['naam']}. "
            f"Laat de voorzitter NIET meedoen in ronde 1 en ronde 2. "
            f"De voorzitter komt alleen terug in de afsluiter."
        )

    st.rerun()


# ============================================================
# EINDEVALUATIE
# ============================================================
if st.session_state.evaluatie_gestart:
    st.markdown("---")
    st.markdown("## 🕊️ Eindgesprek")
    st.caption("De filosofen kijken terug op wat er is gezegd.")

    if st.session_state.evaluatie_rondes is None:
        with st.spinner("De filosofen denken na..."):
            try:
                context = st.session_state.evaluatie_context

                data1 = haal_reacties_op(
                    model_naam, provider_key,
                    EVALUATIE_RONDE_1, context
                )
                rondes = {"ronde_1": (data1 or {}).get("reacties", [])}

                context2 = context + "\n\n--- RONDE 1 ---\n"
                for r in rondes["ronde_1"]:
                    context2 += f"{r['naam']}: {r['tekst']}\n\n"
                data2 = haal_reacties_op(
                    model_naam, provider_key,
                    EVALUATIE_RONDE_2, context2
                )
                rondes["ronde_2"] = (data2 or {}).get("reacties", [])

                st.session_state.evaluatie_rondes = rondes

            except Exception as e:
                st.error(f"Fout bij het ophalen van de evaluatie: {e}")

    if (st.session_state.evaluatie_rondes is not None
            and st.session_state.evaluatie_afsluiter is None):
        with st.spinner("De afsluiting wordt voorbereid..."):
            try:
                voorzitter = st.session_state.get("voorzitter")
                if voorzitter and voorzitter in FILOSOFEN:
                    meest = FILOSOFEN[voorzitter]["naam"]
                else:
                    meest = bepaal_meest_gesproken(st.session_state.geschiedenis) or "Socrates"

                context_afsluiter = st.session_state.evaluatie_context
                context_afsluiter += f"\n\n--- AFSLUITING DOOR ---\n{meest}\n\n"

                for ronde_naam, reacties in st.session_state.evaluatie_rondes.items():
                    context_afsluiter += f"\n--- {ronde_naam.upper()} ---\n"
                    for r in reacties:
                        context_afsluiter += f"{r['naam']}: {r['tekst']}\n\n"

                data_afsluiter = haal_reacties_op(
                    model_naam, provider_key,
                    EVALUATIE_AFSLUITER, context_afsluiter
                )
                st.session_state.evaluatie_afsluiter = (
                    data_afsluiter or {}
                ).get("afsluiter")

            except Exception as e:
                st.error(f"Fout bij de afsluiter: {e}")

    if st.session_state.evaluatie_rondes is not None:
        alle_reacties = verzamel_alle_reacties(
            st.session_state.evaluatie_rondes,
            st.session_state.evaluatie_afsluiter,
        )

        stap = st.session_state.evaluatie_stap

        for i, (ronde_label, r) in enumerate(alle_reacties):
            if i > stap:
                break
            with st.chat_message(r.get("naam", "?"), avatar=r.get("emoji", "🏛️")):
                st.markdown(f"**{r.get('naam', '?')}** · _{ronde_label}_")
                st.markdown(r.get("tekst", ""))

        if stap < len(alle_reacties) - 1:
            volgende = alle_reacties[stap + 1][1]
            wachttijd = bereken_leestijd(volgende.get("tekst", ""))
            time.sleep(wachttijd)
            st.session_state.evaluatie_stap = stap + 1
            st.rerun()

        else:
            st.session_state.evaluatie_afgerond = True


# ============================================================
# EINDSCHERM
# ============================================================
if (st.session_state.get("evaluatie_afgerond", False)
        and not st.session_state.get("archief_gevraagd", False)):

    st.markdown("---")
    st.markdown("## 🏛️ De sessie is afgerond")
    st.markdown("Wil je deze sessie bewaren in je archief?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📁 Ja, archiveer deze sessie", type="primary"):
            archiveer_sessie(
                st.session_state.profiel,
                st.session_state.geschiedenis,
                st.session_state.evaluatie_rondes,
                st.session_state.evaluatie_afsluiter,
            )

            huidig_level = st.session_state.profiel.get("level", 1)
            if huidig_level < 5:
                st.session_state.profiel["level"] = huidig_level + 1
                bewaar_profiel(st.session_state.profiel)

            st.session_state.archief_gevraagd = True
            st.session_state.archief_opgeslagen = True
            st.rerun()

    with col2:
        if st.button("Nee, bewaar niet"):
            huidig_level = st.session_state.profiel.get("level", 1)
            if huidig_level < 5:
                st.session_state.profiel["level"] = huidig_level + 1
                bewaar_profiel(st.session_state.profiel)

            st.session_state.archief_gevraagd = True
            st.session_state.archief_opgeslagen = False
            st.rerun()


if (st.session_state.get("archief_gevraagd", False)
        and not st.session_state.get("eind_keuze_gemaakt", False)):

    st.markdown("---")
    st.markdown("## 🕊️")
    st.caption("Even stilte.")

    st.markdown("---")
    st.markdown("### Wat wil je nu doen?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("☕ Nazit"):
            st.session_state.nazit_gestart = True
            st.session_state.eind_keuze_gemaakt = True
            st.rerun()

    with col2:
        if st.button("🔄 Nieuwe sessie"):
            reset_voor_nieuwe_sessie()
            st.rerun()

    with col3:
        if st.button("👋 Afsluiten"):
            st.session_state.einde = True
            st.session_state.eind_keuze_gemaakt = True
            st.rerun()


if st.session_state.get("einde", False):
    st.markdown("---")
    st.markdown("## 👋 Bedankt voor het gesprek")
    st.caption("Tot de volgende keer.")

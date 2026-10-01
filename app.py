"""
Aurelius — een filosofische coach-app.
Start met: python -m streamlit run app.py
"""

import streamlit as st
import time
from datetime import datetime

# Eigen modules
from filosofen import FILOSOFEN, STANDAARD_PANTHEON
from coach import bouw_coach_prompt, kies_filosoof, chat

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
)

try:
    initialiseer()
except Exception as e:
    st.error(f"⚠️ **Database-fout:** {e}")
    st.stop()

# ============================================================
# Fasen en vragen
# ============================================================
FASE_PERCENTAGES = {
    "incheck":    (0.00, 0.08),
    "opening":    (0.08, 0.20),
    "verkennen":  (0.20, 0.40),
    "verdiepen":  (0.40, 0.72),
    "verbreden":  (0.72, 0.88),
    "integreren": (0.88, 0.96),
    "afsluiten":  (0.96, 1.00),
}

VRAGEN_PER_FASE = {
    "incheck":   ["Hoe gaat het vandaag?", "Wat wil je bereiken?", "Hoe lang heb je?"],
    "opening":   ["Waar wil je beginnen?", "Wat speelt er?", "Wat houdt je bezig?"],
    "verkennen": ["Wat valt je op?", "Wat gebeurt er als je hieraan denkt?", "Wat maakt dit belangrijk?"],
    "verdiepen": ["Wat zit eronder?", "Wat raakt je hierin?", "Wat vermijd je?"],
    "verbreden": ["Welke perspectieven zijn er?", "Wat zou een filosoof zeggen?", "Wat als het tegenovergestelde waar is?"],
    "integreren":["Wat neem je mee?", "Wat ga je doen?", "Wat is je volgende stap?"],
    "afsluiten": ["Wat was belangrijk vandaag?", "Wat neem je mee naar de volgende keer?"],
    "nazit":     ["Wat wil je nog bespreken?", "Waar wil je nog over filosoferen?"],
}

# ============================================================
# Tijdsysteem
# ============================================================
PAUZE_DREMPEL = 30  # seconden

def update_sessie_tijd(profiel):
    """Werkt de sessietijd bij. Pauzes langer dan 30 sec tellen niet mee."""
    nu = time.time()
    laatste = profiel.get("laatste_bericht", nu)
    verschil = nu - laatste

    if verschil < PAUZE_DREMPEL:
        profiel["sessie_tijd"] = profiel.get("sessie_tijd", 0) + verschil

    profiel["laatste_bericht"] = nu
    return profiel


def bereken_sessie_minuten(profiel):
    return profiel.get("sessie_tijd", 0) / 60


def bepaal_fase(profiel):
    minuten = bereken_sessie_minuten(profiel)
    duur = profiel.get("sessie_duur", 25)
    if duur <= 0:
        return "incheck"
    percentage = minuten / duur

    for fase, (start, eind) in FASE_PERCENTAGES.items():
        if start <= percentage < eind:
            return fase
    return "nazit"


def check_einde_sessie(profiel):
    minuten = bereken_sessie_minuten(profiel)
    duur = profiel.get("sessie_duur", 25)
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
    {"sleutel": "emotie", "vraag": "Hoe gaat het vandaag?", "type": "tekst",
     "placeholder": "Bijvoorbeeld: druk, moe, rustig..."},
    {"sleutel": "overzicht", "vraag": "Heb je overzicht over je leven?", "type": "slider",
     "min": 1, "max": 10, "default": 5, "toelichting": "1 = geen, 10 = volledig"},
    {"sleutel": "intentie", "vraag": "Wat wil je vandaag?", "type": "keuze",
     "opties": ["Even praten", "Iets bespreken", "Iets onderzoeken", "Iets vieren"]},
    {"sleutel": "volgorde", "vraag": "Zet deze vier op volgorde van belangrijkheid.",
     "type": "sorteren", "opties": ["Respect", "Vertrouwen", "Verbinding", "Analyse"]},
    {"sleutel": "duur", "vraag": "Hoe lang heb je?", "type": "keuze",
     "opties": ["Kort (10 min)", "Standaard (25 min)", "Diep (50 min)"]},
    {"sleutel": "modus", "vraag": "Wie wil je spreken?", "type": "keuze",
     "opties": ["Automatisch — de coach kiest", "Zelf kiezen", "Verrassen"]},
]

# ============================================================
# Sidebar
# ============================================================
st.sidebar.title("🏛️ Aurelius")
st.sidebar.caption("Jouw filosofische metgezel")

gebruiker_id = st.sidebar.text_input("Gebruikersnaam", value="remco")

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

pantheon = st.sidebar.multiselect(
    "Kies je filosofen",
    options=list(FILOSOFEN.keys()),
    default=STANDAARD_PANTHEON,
    format_func=lambda x: f"{FILOSOFEN[x]['emoji']} {FILOSOFEN[x]['naam']}",
)

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

if st.session_state.get("huidige_gebruiker") != gebruiker_id:
    st.session_state.profiel = laad_profiel(gebruiker_id)
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
# Incheck
# ============================================================
if not st.session_state.incheck_afgerond:
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
            st.session_state.profiel["themas"] = [incheck.get("emotie", "")]
            st.session_state.profiel["waarde_volgorde"] = volgorde

            # Sessie-tijd initialiseren
            duur_map = {"Kort (10 min)": 10, "Standaard (25 min)": 25, "Diep (50 min)": 50}
            st.session_state.profiel["sessie_duur"] = duur_map.get(incheck.get("duur"), 25)
            st.session_state.profiel["sessie_start"] = time.time()
            st.session_state.profiel["sessie_tijd"] = 0
            st.session_state.profiel["laatste_bericht"] = time.time()

            bewaar_profiel(st.session_state.profiel)
            st.rerun()

    st.stop()

# ============================================================
# Gesprek
# ============================================================
incheck = st.session_state.get("incheck", {})

# Update sessietijd
st.session_state.profiel = update_sessie_tijd(st.session_state.profiel)

# Bepaal fase en tijden
fase = bepaal_fase(st.session_state.profiel)
minuten = bereken_sessie_minuten(st.session_state.profiel)
duur = st.session_state.profiel.get("sessie_duur", 25)
resterend = max(0, duur - minuten)

# Toon de statusbalk
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

# Toon de voortgangsbalk van de fasen
FASE_VOLGORDE = ["incheck", "opening", "verkennen", "verdiepen", "verbreden", "integreren", "afsluiten"]
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

# Toon incheck in expander
if incheck:
    with st.expander("📋 Jouw incheck", expanded=False):
        st.markdown(f"- **Emotie**: {incheck.get('emotie', '—')}")
        st.markdown(f"- **Overzicht**: {incheck.get('overzicht', '—')}/10")
        st.markdown(f"- **Intentie**: {incheck.get('intentie', '—')}")
        volgorde = incheck.get("volgorde", [])
        if volgorde:
            st.markdown(f"- **Volgorde**: {' → '.join(volgorde)}")
        st.markdown(f"- **Duur**: {incheck.get('duur', '—')}")

# Gesprek renderen
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

# ============================================================
# Eerste coach-beurt
# ============================================================
if not st.session_state.geschiedenis:
    emotie = incheck.get("emotie", "")
    overzicht = incheck.get("overzicht", 5)
    intentie = incheck.get("intentie", "")
    volgorde = incheck.get("volgorde", [])
    eerste_waarde = volgorde[0] if volgorde else "Respect"

    opening = (
        f"Je zegt: {emotie}. Je gaf een {overzicht}/10 op overzicht. "
        f"En je wilt: {intentie.lower()}.\n\n"
        f"Je zet **{eerste_waarde}** bovenaan. Laten we daar beginnen."
    )

    st.session_state.geschiedenis.append({
        "naam": "Coach", "tekst": opening, "icoon": "🏛️",
        "tijd": datetime.now().strftime("%H:%M"),
    })
    try:
        bewaar_bericht(gebruiker_id, "Coach", "assistant", opening)
    except Exception:
        pass
    toon_bericht("Coach", opening, "🏛️", datetime.now().strftime("%H:%M"))

# ============================================================
# Invoer
# ============================================================
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

    # Update sessietijd
    st.session_state.profiel = update_sessie_tijd(st.session_state.profiel)
    fase = bepaal_fase(st.session_state.profiel)

    # Kies filosoof
    if pantheon:
        filosoof_naam = kies_filosoof(st.session_state.profiel, pantheon, gebruiker_input)
    else:
        filosoof_naam = "aurelius"

    filosoof = FILOSOFEN[filosoof_naam]

    # Bouw de prompt
    system_prompt = bouw_coach_prompt(
        filosoof=filosoof,
        profiel=st.session_state.profiel,
        modus="Coach",
        fase=fase,
        vragen=VRAGEN_PER_FASE.get(fase, [])
    )

    # Check of de sessie bijna voorbij is
    einde_check = check_einde_sessie(st.session_state.profiel)
    if einde_check:
        system_prompt += f"\n\n[EINDE SESSIE]\n{einde_check}"

    # Bouw de messages
    context = st.session_state.geschiedenis[-max_historie:]
    messages = []
    for b in context[:-1]:
        rol = "assistant" if b["naam"] != "Jij" else "user"
        messages.append({"role": rol, "content": b["tekst"]})
    messages.append({"role": "user", "content": gebruiker_input})

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

    try:
        bewaar_profiel(st.session_state.profiel)
    except Exception:
        pass

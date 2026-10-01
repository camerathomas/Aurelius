"""
Aurelius — een filosofische coach-app.
Start met: python -m streamlit run app.py
"""

import streamlit as st
from datetime import datetime

# Eigen modules
from filosofen import FILOSOFEN, STANDAARD_PANTHEON
from coach import bouw_coach_prompt, kies_filosoof, chat
from profiel import laad_profiel, bewaar_profiel

# ============================================================
# Configuratie
# ============================================================
st.set_page_config(
    page_title="Aurelius",
    page_icon="🏛️",
    layout="centered"
)

# ============================================================
# Incheck-vragen
# ============================================================
INCHECK_VRAGEN = [
    {
        "sleutel": "emotie",
        "vraag": "Hoe gaat het vandaag?",
        "type": "tekst",
        "placeholder": "Bijvoorbeeld: druk, moe, rustig, gespannen...",
    },
    {
        "sleutel": "score",
        "vraag": "Op een schaal van 1-10, waar sta je?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
    },
    {
        "sleutel": "intentie",
        "vraag": "Wat wil je vandaag?",
        "type": "keuze",
        "opties": ["Even praten", "Iets bespreken", "Iets onderzoeken", "Iets vieren"],
    },
    {
        "sleutel": "duur",
        "vraag": "Hoe lang heb je?",
        "type": "keuze",
        "opties": ["Kort (10 min)", "Standaard (25 min)", "Diep (50 min)", "Open"],
    },
    {
        "sleutel": "modus",
        "vraag": "Wie wil je spreken?",
        "type": "keuze",
        "opties": ["Automatisch — de coach kiest", "Zelf kiezen", "Verrassen"],
    },
]

# ============================================================
# Sidebar
# ============================================================
st.sidebar.title("🏛️ Aurelius")
st.sidebar.caption("Jouw filosofische metgezel")

gebruiker_id = st.sidebar.text_input(
    "Gebruikersnaam",
    value="remco",
    help="Alles wordt lokaal opgeslagen onder deze naam."
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔌 Model")

provider = st.sidebar.selectbox(
    "Provider",
    ["Gemini", "Ollama"],
    help="Gemini werkt online (gratis tier). Ollama werkt lokaal."
)

if provider == "Gemini":
    model_naam = st.sidebar.selectbox(
        "Model",
        ["gemini-3.5-flash-lite"],
        help="Flash is snel en gratis. Pro is slimmer maar langzamer."
    )
    provider_key = "gemini"
else:
    model_naam = st.sidebar.selectbox(
        "Model",
        ["llama3.2:latest", "qwen3:4b-q4_K_M"],
    )
    provider_key = "ollama"

st.sidebar.markdown("---")
st.sidebar.subheader("🎭 Pantheon")

pantheon = st.sidebar.multiselect(
    "Kies je filosofen",
    options=list(FILOSOFEN.keys()),
    default=STANDAARD_PANTHEON,
    format_func=lambda x: f"{FILOSOFEN[x]['emoji']} {FILOSOFEN[x]['naam']}",
    help="Standaard staan er 6 filosofen aan. Je kunt er meer of minder kiezen."
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔧 Parameters")

temperature = st.sidebar.slider("Temperature", 0.0, 1.5, 0.8, 0.1)
max_historie = st.sidebar.slider(
    "Max. berichten in context", 4, 40, 12, 2,
    help="Hoeveel eerdere berichten de modellen zien."
)

# ============================================================
# Sessie-state
# ============================================================
if "geschiedenis" not in st.session_state:
    st.session_state.geschiedenis = []
if "profiel" not in st.session_state:
    st.session_state.profiel = laad_profiel(gebruiker_id)
if "incheck" not in st.session_state:
    st.session_state.incheck = {}
if "incheck_stap" not in st.session_state:
    st.session_state.incheck_stap = 0
if "incheck_afgerond" not in st.session_state:
    st.session_state.incheck_afgerond = False

# Als de gebruiker wisselt, herlaad het profiel en reset de incheck
if st.session_state.get("huidige_gebruiker") != gebruiker_id:
    st.session_state.profiel = laad_profiel(gebruiker_id)
    st.session_state.huidige_gebruiker = gebruiker_id
    st.session_state.geschiedenis = []
    st.session_state.incheck = {}
    st.session_state.incheck_stap = 0
    st.session_state.incheck_afgerond = False

# ============================================================
# Hoofdinterface — titel
# ============================================================
st.title("🏛️ Aurelius")
st.caption("Een filosofische coach, geïnspireerd door Marcus Aurelius.")

# ============================================================
# Incheck — als nog niet afgerond
# ============================================================
if not st.session_state.incheck_afgerond:
    st.markdown("---")
    st.markdown("### 👋 Welkom")
    st.markdown("Even een paar vragen voordat we beginnen.")

    stap = st.session_state.incheck_stap

    # Voortgang
    voortgang = stap / len(INCHECK_VRAGEN)
    st.progress(voortgang, text=f"Vraag {stap + 1} van {len(INCHECK_VRAGEN)}" if stap < len(INCHECK_VRAGEN) else "Klaar")

    if stap < len(INCHECK_VRAGEN):
        vraag = INCHECK_VRAGEN[stap]
        st.markdown(f"**{vraag['vraag']}**")

        if vraag["type"] == "tekst":
            antwoord = st.text_input(
                "Antwoord",
                placeholder=vraag.get("placeholder", ""),
                label_visibility="collapsed",
                key=f"incheck_{vraag['sleutel']}"
            )
            if st.button("Volgende ➡️"):
                if antwoord.strip():
                    st.session_state.incheck[vraag["sleutel"]] = antwoord.strip()
                    st.session_state.incheck_stap += 1
                    st.rerun()
                else:
                    st.warning("Vul iets in om verder te gaan.")

        elif vraag["type"] == "slider":
            antwoord = st.slider(
                "Score",
                vraag["min"],
                vraag["max"],
                vraag["default"],
                label_visibility="collapsed",
                key=f"incheck_{vraag['sleutel']}"
            )
            if st.button("Volgende ➡️"):
                st.session_state.incheck[vraag["sleutel"]] = antwoord
                st.session_state.incheck_stap += 1
                st.rerun()

        elif vraag["type"] == "keuze":
            antwoord = st.radio(
                "Keuze",
                vraag["opties"],
                label_visibility="collapsed",
                key=f"incheck_{vraag['sleutel']}"
            )
            if st.button("Volgende ➡️"):
                st.session_state.incheck[vraag["sleutel"]] = antwoord
                st.session_state.incheck_stap += 1
                st.rerun()

    else:
        # Incheck is klaar — toon samenvatting
        st.markdown("### ✅ Klaar")
        st.markdown("Dit is wat ik heb onthouden:")
        for sleutel, waarde in st.session_state.incheck.items():
            st.markdown(f"- **{sleutel.capitalize()}**: {waarde}")

        if st.button("🚀 Start gesprek", type="primary"):
            st.session_state.incheck_afgerond = True
            st.session_state.profiel["laatste_incheck"] = st.session_state.incheck
            st.session_state.profiel["themas"] = [st.session_state.incheck.get("emotie", "")]
            bewaar_profiel(gebruiker_id, st.session_state.profiel)
            st.rerun()

    st.stop()  # Stop hier — toon de chat niet

# ============================================================
# Gesprek — na de incheck
# ============================================================

# Toon de incheck-context
incheck = st.session_state.get("incheck", {})
if incheck:
    with st.expander("📋 Jouw incheck", expanded=False):
        st.markdown(f"- **Emotie**: {incheck.get('emotie', '—')}")
        st.markdown(f"- **Score**: {incheck.get('score', '—')}/10")
        st.markdown(f"- **Intentie**: {incheck.get('intentie', '—')}")
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
# Eerste coach-beurt na de incheck
# ============================================================
if not st.session_state.geschiedenis:
    # De coach opent het gesprek op basis van de incheck
    emotie = incheck.get("emotie", "")
    intentie = incheck.get("intentie", "")
    score = incheck.get("score", 5)

    opening = (
        f"Je zegt: {emotie}. Je gaf een {score}/10. "
        f"En je wilt: {intentie.lower()}."
    )

    st.session_state.geschiedenis.append({
        "naam": "Coach",
        "tekst": opening,
        "icoon": "🏛️",
        "tijd": datetime.now().strftime("%H:%M"),
    })
    toon_bericht("Coach", opening, "🏛️", datetime.now().strftime("%H:%M"))

# ============================================================
# Invoer
# ============================================================
gebruiker_input = st.chat_input("Waar wil je het over hebben?")

if gebruiker_input:
    # Voeg gebruikersbericht toe
    tijd = datetime.now().strftime("%H:%M")
    st.session_state.geschiedenis.append({
        "naam": "Jij",
        "tekst": gebruiker_input,
        "icoon": "🧑",
        "tijd": tijd,
    })
    toon_bericht("Jij", gebruiker_input, "🧑", tijd)

    # Kies een filosoof
    if pantheon:
        filosoof_naam = kies_filosoof(
            st.session_state.profiel,
            pantheon,
            gebruiker_input
        )
    else:
        filosoof_naam = "aurelius"

    filosoof = FILOSOFEN[filosoof_naam]

    # Bouw de system prompt
    system_prompt = bouw_coach_prompt(
        filosoof=filosoof,
        profiel=st.session_state.profiel,
        modus="Coach"
    )

    # Bouw de messages
    context = st.session_state.geschiedenis[-max_historie:]
    messages = []
    for b in context[:-1]:
        rol = "assistant" if b["naam"] != "Jij" else "user"
        messages.append({"role": rol, "content": b["tekst"]})
    messages.append({"role": "user", "content": gebruiker_input})

    # Roep het model aan
    with st.spinner(f"{filosoof['naam']} denkt na..."):
        antwoord = chat(
            model=model_naam,
            messages=messages,
            system_prompt=system_prompt,
            temperature=temperature,
            provider=provider_key
        )

    # Voeg antwoord toe
    tijd = datetime.now().strftime("%H:%M")
    st.session_state.geschiedenis.append({
        "naam": filosoof["naam"],
        "tekst": antwoord,
        "icoon": filosoof["emoji"],
        "tijd": tijd,
    })
    toon_bericht(filosoof["naam"], antwoord, filosoof["emoji"], tijd)

    # Bewaar profiel
    bewaar_profiel(gebruiker_id, st.session_state.profiel)

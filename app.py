"""
Aurelius — een filosofische coach-app.
Start met: python -m streamlit run app.py
"""

import streamlit as st
from datetime import datetime

# Eigen modules
from filosofen import FILOSOFEN, STANDAARD_PANTHEON
from coach import bouw_coach_prompt, kies_filosoof
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
# Sidebar — instellingen
# ============================================================
st.sidebar.title("🏛️ Aurelius")
st.sidebar.caption("Jouw filosofische metgezel")

gebruiker_id = st.sidebar.text_input(
    "Gebruikersnaam",
    value="remco",
    help="Alles wordt lokaal opgeslagen onder deze naam."
)

modus = st.sidebar.radio(
    "Modus",
    ["Coach", "Filosofie", "Dialoog"],
    help=(
        "Coach — de coach kiest de filosoof.\n"
        "Filosofie — jij kiest de filosoof.\n"
        "Dialoog — twee filosofen in gesprek."
    )
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎭 Pantheon")

# Welke filosofen zijn actief?
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
if "actief" not in st.session_state:
    st.session_state.actief = False

# ============================================================
# Hoofdinterface
# ============================================================
st.title("🏛️ Aurelius")
st.caption("Een filosofische coach, geïnspireerd door Marcus Aurelius.")

# Status
if st.session_state.actief:
    st.info(f"🟢 Gesprek actief · modus: {modus}")
else:
    st.info("Typ hieronder om een gesprek te beginnen.")

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
    if modus == "Filosofie":
        # Gebruiker kiest via sidebar (later uitwerken)
        filosoof_naam = pantheon[0] if pantheon else STANDAARD_PANTHEON[0]
    else:
        filosoof_naam = kies_filosoof(
            st.session_state.profiel,
            pantheon,
            gebruiker_input
        )

    filosoof = FILOSOFEN[filosoof_naam]

    # Bouw de prompt
    system_prompt = bouw_coach_prompt(
        filosoof=filosoof,
        profiel=st.session_state.profiel,
        modus=modus
    )

    # Roep het model aan
    from coach import chat
    antwoord = chat(
        model="llama3.2:latest",  # standaard coach-model
        messages=[{"role": "user", "content": gebruiker_input}],
        system_prompt=system_prompt,
        temperature=temperature
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

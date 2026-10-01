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
        "sleutel": "overzicht",
        "vraag": "Heb je op dit moment goed overzicht over je leven?",
        "type": "slider",
        "min": 1,
        "max": 10,
        "default": 5,
        "toelichting": "1 = geen overzicht, 10 = volledig overzicht",
    },
    {
        "sleutel": "intentie",
        "vraag": "Wat wil je vandaag?",
        "type": "keuze",
        "opties": ["Even praten", "Iets bespreken", "Iets onderzoeken", "Iets vieren"],
    },
    {
        "sleutel": "volgorde",
        "vraag": "Zet deze vier op volgorde van belangrijkheid voor jou.",
        "type": "sorteren",
        "opties": ["Respect", "Vertrouwen", "Verbinding", "Analyse"],
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
        ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite"],
        help="Lite modellen hebben 500 gratis requests per dag."
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
    help="Standaard staan er 6 filosofen aan."
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
if "sorteer_posities" not in st.session_state:
    st.session_state.sorteer_posities = {}

# Als de gebruiker wisselt, herlaad het profiel en reset de incheck
if st.session_state.get("huidige_gebruiker") != gebruiker_id:
    st.session_state.profiel = laad_profiel(gebruiker_id)
    st.session_state.huidige_gebruiker = gebruiker_id
    st.session_state.geschiedenis = []
    st.session_state.incheck = {}
    st.session_state.incheck_stap = 0
    st.session_state.incheck_afgerond = False
    st.session_state.sorteer_posities = {}

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
    totaal = len(INCHECK_VRAGEN)

    # Voortgang
    voortgang = stap / totaal
    if stap < totaal:
        st.progress(voortgang, text=f"Vraag {stap + 1} van {totaal}")
    else:
        st.progress(1.0, text="Klaar")

    if stap < totaal:
        vraag = INCHECK_VRAGEN[stap]
        st.markdown(f"**{vraag['vraag']}**")

        # --- Type: tekst ---
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

        # --- Type: slider ---
        elif vraag["type"] == "slider":
            if vraag.get("toelichting"):
                st.caption(vraag["toelichting"])
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

        # --- Type: keuze ---
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

        # --- Type: sorteren ---
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
                volgorde = [pos1, pos2, pos3, pos4]
                st.session_state.incheck["volgorde"] = volgorde
                st.session_state.incheck_stap += 1
                st.rerun()

    else:
        # Incheck klaar — toon samenvatting
        st.markdown("### ✅ Klaar")
        st.markdown("Dit is wat ik heb onthouden:")

        incheck = st.session_state.incheck

        st.markdown(f"- **Emotie**: {incheck.get('emotie', '—')}")
        st.markdown(f"- **Overzicht**: {incheck.get('overzicht', '—')}/10")
        st.markdown(f"- **Intentie**: {incheck.get('intentie', '—')}")
        volgorde = incheck.get("volgorde", [])
        if volgorde:
            st.markdown(f"- **Jouw volgorde**: {' → '.join(volgorde)}")
        st.markdown(f"- **Duur**: {incheck.get('duur', '—')}")
        st.markdown(f"- **Modus**: {incheck.get('modus', '—')}")

        if st.button("🚀 Start gesprek", type="primary"):
            st.session_state.incheck_afgerond = True
            st.session_state.profiel["laatste_incheck"] = incheck
            st.session_state.profiel["themas"] = [incheck.get("emotie", "")]
            st.session_state.profiel["waarde_volgorde"] = volgorde
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
# Eerste coach-beurt na de incheck
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

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
)
from coach import bouw_coach_prompt, kies_filosoof, chat
from evaluatie import (
    EVALUATIE_RONDE_1,
    EVALUATIE_RONDE_2,
    EVALUATIE_RONDE_3,
    EVALUATIE_AFSLUITER,
    haal_reacties_op,
    bouw_context,
    bepaal_meest_gesproken,
    verzamel_alle_reacties,
    bereken_leestijd,
)

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


def update_sessie_tijd(profiel):
    nu = time.time()
    laatste = profiel.get("laatste_bericht", nu)
    verschil = nu - laatste

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
    duur = profiel.get("sessie_duur", 25)
    if duur <= 0:
        return "opening"
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

beschikbaar = beschikbare_filosofen(level)

pantheon = st.sidebar.multiselect(
    "Kies je filosofen",
    options=beschikbaar,
    default=[f for f in STANDAARD_PANTHEON if f in beschikbaar],
    format_func=lambda x: f"{FILOSOFEN[x]['emoji']} {FILOSOFEN[x]['naam']}",
    help=f"Level {level} — er komen meer filosofen bij als je groeit."
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
        st.session_state.grote_wending_geweest = False
        st.session_state.evaluatie_gestart = False
        st.session_state.evaluatie_context = ""
        st.session_state.evaluatie_rondes = None
        st.session_state.evaluatie_afsluiter = None
        st.session_state.evaluatie_stap = 0
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
            st.session_state.profiel["waarde_volgorde"] = volgorde

            duur_map = {"Kort (10 min)": 10, "Standaard (25 min)": 25, "Diep (50 min)": 50}
            st.session_state.profiel["sessie_duur"] = duur_map.get(incheck.get("duur"), 25)
            st.session_state.profiel["sessie_start"] = time.time()
            st.session_state.profiel["sessie_tijd"] = 0
            st.session_state.profiel["laatste_bericht"] = time.time()

            st.session_state.grote_wending_geweest = False
            st.session_state.evaluatie_gestart = False
            st.session_state.evaluatie_context = ""
            st.session_state.evaluatie_rondes = None
            st.session_state.evaluatie_afsluiter = None
            st.session_state.evaluatie_stap = 0

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
duur = st.session_state.profiel.get("sessie_duur", 25)
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
    eerste_waarde = volgorde[0] if volgorde else "Respect"

    opening_delen = []
    if openheid:
        opening_delen.append(f"Je vertelt: *{openheid}*")
    if emotie:
        opening_delen.append(f"Je zegt: *{emotie}*")
    opening_delen.append(f"Je gaf een **{overzicht}/10** op overzicht")
    if intentie:
        opening_delen.append(f"Je wilt: **{intentie.lower()}**")
    if volgorde:
        staart = f" → {' → '.join(volgorde[1:])}" if len(volgorde) > 1 else ""
        opening_delen.append(f"Je zet **{eerste_waarde}** bovenaan{staart}")

    opening = "  \n".join(opening_delen) + "\n\nLaten we daar beginnen."

    st.session_state.geschiedenis.append({
        "naam": "Coach", "tekst": opening, "icoon": "🏛️",
        "tijd": datetime.now().strftime("%H:%M"),
    })
    try:
        bewaar_bericht(gebruiker_id, "Coach", "assistant", opening)
    except Exception:
        pass
    toon_bericht("Coach", opening, "🏛️", datetime.now().strftime("%H:%M"))

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

    if pantheon:
        filosoof_naam = kies_filosoof(
            st.session_state.profiel, pantheon, openheid or emotie or "begin"
        )
    else:
        filosoof_naam = "aurelius"

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

# Invoer
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
    duur = st.session_state.profiel.get("sessie_duur", 25)
    halverwege = minuten >= (duur / 2)
    wending_nodig = halverwege and not st.session_state.grote_wending_geweest

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
            filosoof_naam = "aurelius"

        st.session_state.grote_wending_geweest = True

    else:
        if pantheon:
            filosoof_naam = kies_filosoof(
                st.session_state.profiel, pantheon, gebruiker_input
            )
        else:
            filosoof_naam = "aurelius"

    filosoof = FILOSOFEN[filosoof_naam]

    system_prompt = bouw_coach_prompt(
        filosoof=filosoof,
        profiel=st.session_state.profiel,
        modus="Coach",
        fase=fase,
        vragen=VRAGEN_PER_FASE.get(fase, [])
    )

    # Socrates: elenchus alleen in het begin
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

    # Grote wending: halverwege de sessie
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

    einde_check = check_einde_sessie(st.session_state.profiel)
    if einde_check:
        system_prompt += f"\n\n[EINDE SESSIE]\n{einde_check}"

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
# ============================================================
# AFRONDING — automatisch starten zodra Socrates heeft afgesloten
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
    st.rerun()


# ============================================================
# EINDEVALUATIE
# ============================================================
if st.session_state.evaluatie_gestart:
    st.markdown("---")
    st.markdown("## 🕊️ Eindgesprek")
    st.caption("De filosofen kijken terug op wat er is gezegd.")

    # --- Stap A: de drie rondes ophalen ---
    if st.session_state.evaluatie_rondes is None:
        with st.spinner("De filosofen denken na..."):
            try:
                context = st.session_state.evaluatie_context

                # Ronde 1
                data1 = haal_reacties_op(
                    model_naam, provider_key,
                    EVALUATIE_RONDE_1, context
                )
                rondes = {"ronde_1": (data1 or {}).get("reacties", [])}

                # Ronde 2
                context2 = context + "\n\n--- RONDE 1 ---\n"
                for r in rondes["ronde_1"]:
                    context2 += f"{r['naam']}: {r['tekst']}\n\n"
                data2 = haal_reacties_op(
                    model_naam, provider_key,
                    EVALUATIE_RONDE_2, context2
                )
                rondes["ronde_2"] = (data2 or {}).get("reacties", [])

                # Ronde 3
                context3 = context + "\n\n--- RONDE 2 ---\n"
                for r in rondes["ronde_2"]:
                    context3 += f"{r['naam']}: {r['tekst']}\n\n"
                data3 = haal_reacties_op(
                    model_naam, provider_key,
                    EVALUATIE_RONDE_3, context3
                )
                rondes["ronde_3"] = (data3 or {}).get("reacties", [])

                st.session_state.evaluatie_rondes = rondes

            except Exception as e:
                st.error(f"Fout bij het ophalen van de evaluatie: {e}")

    # --- Stap B: de afsluiter ophalen ---
    if (st.session_state.evaluatie_rondes is not None
            and st.session_state.evaluatie_afsluiter is None):
        with st.spinner("De afsluiting wordt voorbereid..."):
            try:
                meest = bepaal_meest_gesproken(st.session_state.geschiedenis) or "Socrates"

                context_afsluiter = st.session_state.evaluatie_context
                context_afsluiter += f"\n\n--- MEEST GESPROKEN ---\n{meest}\n\n"

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

    # --- Stap C: de reacties één voor één tonen ---
    if st.session_state.evaluatie_rondes is not None:
        alle_reacties = verzamel_alle_reacties(
            st.session_state.evaluatie_rondes,
            st.session_state.evaluatie_afsluiter,
        )

        stap = st.session_state.evaluatie_stap

        # Toon alle reacties tot en met de huidige stap
        for i, (ronde_label, r) in enumerate(alle_reacties):
            if i > stap:
                break
            with st.chat_message(r.get("naam", "?"), avatar=r.get("emoji", "🏛️")):
                st.markdown(f"**{r.get('naam', '?')}** · _{ronde_label}_")
                st.markdown(r.get("tekst", ""))

        # Is er nog een volgende reactie?
        if stap < len(alle_reacties) - 1:
            volgende = alle_reacties[stap + 1][1]
            wachttijd = bereken_leestijd(volgende.get("tekst", ""))
            time.sleep(wachttijd)
            st.session_state.evaluatie_stap = stap + 1
            st.rerun()

        else:
            # Alles is getoond — toon de afsluitende boodschap
            st.markdown("---")
            st.success("Het eindgesprek is afgerond.")
            st.caption(
                "De volledige evaluatie wordt opgeslagen in je archief. "
                "De PDF-versie volgt in een latere versie."
            )


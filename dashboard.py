"""
Dashboard voor Aurelius.
Toont het archief, de voortgang, de favorieten, en de instellingen.
"""

import streamlit as st

from filosofen import FILOSOFEN, PANTHEON_PER_LEVEL
from opslag import laad_sessies, bewaar_profiel


def toon_dashboard(gebruiker_id, profiel):
    """Toont het hele dashboard."""
    st.title("🏛️ Jouw dashboard")
    st.caption(f"Welkom terug, {gebruiker_id}.")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Archief", "Voortgang", "Favorieten", "Instellingen"]
    )

    with tab1:
        _toon_archief(gebruiker_id)

    with tab2:
        _toon_voortgang(profiel)

    with tab3:
        _toon_favorieten(profiel)

    with tab4:
        _toon_instellingen(profiel, gebruiker_id)


def _toon_archief(gebruiker_id):
    """Toont de gearchiveerde sessies."""
    st.markdown("### Jouw archief")

    sessies = laad_sessies(gebruiker_id)

    if not sessies:
        st.markdown(
            "Je hebt nog geen sessies gearchiveerd. "
            "Na elk gesprek kun je de sessie bewaren, en dan verschijnt "
            "hij hier."
        )
        return

    st.caption(f"{len(sessies)} sessies gevonden.")

    for sessie in sessies:
        datum = str(sessie.get("datum", "?"))[:16]
        thema = sessie.get("thema", "onbekend")

        with st.expander(f"📁 {datum} — {thema}"):
            # Pantheon
            pantheon = sessie.get("pantheon", [])
            if pantheon:
                namen = [
                    FILOSOFEN[f]["naam"]
                    for f in pantheon
                    if f in FILOSOFEN
                ]
                st.markdown(f"**Pantheon:** {', '.join(namen)}")

            # Duur
            duur = sessie.get("duur_minuten", "?")
            st.markdown(f"**Duur:** {duur} minuten")

            # Incheck
            incheck = sessie.get("incheck", {})
            if incheck:
                st.markdown("**Incheck:**")
                st.markdown(f"- Wat speelt er: {incheck.get('openheid', '—')}")
                st.markdown(f"- Emotie: {incheck.get('emotie', '—')}")
                st.markdown(f"- Overzicht: {incheck.get('overzicht', '—')}/10")
                st.markdown(f"- Intentie: {incheck.get('intentie', '—')}")
                volgorde = incheck.get("volgorde", [])
                if volgorde:
                    st.markdown(f"- Volgorde: {' → '.join(volgorde)}")

            # Gesprek
            gesprek = sessie.get("gesprek", [])
            if gesprek:
                st.markdown("### Gesprek")
                for bericht in gesprek:
                    naam = bericht.get("naam", "?")
                    tekst = bericht.get("tekst", "")
                    st.markdown(f"**{naam}:** {tekst}")

            # Rondes
            rondes = sessie.get("rondes", {})
            if rondes:
                st.markdown("### Eindgesprek")
                for ronde_naam, reacties in rondes.items():
                    st.markdown(f"**{ronde_naam.replace('_', ' ').title()}**")
                    for r in reacties:
                        st.markdown(
                            f"**{r.get('naam', '?')}:** {r.get('tekst', '')}"
                        )

            # Afsluiter
            afsluiter = sessie.get("afsluiter", {})
            if afsluiter:
                st.markdown("### Afsluiting")
                st.markdown(
                    f"**{afsluiter.get('naam', '?')}:** "
                    f"{afsluiter.get('tekst', '')}"
                )


def _toon_voortgang(profiel):
    """Toont de voortgang van de gebruiker."""
    st.markdown("### Jouw voortgang")
    st.markdown(f"**Level:** {profiel.get('level', 1)}")
    st.caption("Meer statistieken volgen later.")


def _toon_favorieten(profiel):
    """Toont de favorieten van de gebruiker."""
    st.markdown("### Jouw favorieten")
    st.caption("Deze functie komt later.")


def _toon_instellingen(profiel, gebruiker_id):
    """Toont de instellingen."""
    st.markdown("### Instellingen")
    st.caption("Deze functie komt later.")

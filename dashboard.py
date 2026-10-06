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

    level = profiel.get("level", 1)
    tier = profiel.get("tier", "sessie")

    # Favoriete filosoof (drempel 5)
    _toon_favoriet_filosoof(profiel, level, tier)

    st.markdown("---")

    # Eigen pantheon
    _toon_eigen_pantheon(profiel, level, tier)

def _toon_favoriet_filosoof(profiel, level, tier):
    """Toont de keuze voor de favoriete filosoof."""
    from tiers import heeft_toegang, beschikbare_filosofen, drempel_van
    from filosofen import FILOSOFEN

    st.markdown("#### Favoriete filosoof")
    st.caption(
        "Kies de filosoof die je het meeste aanspreekt. "
        "Hij zit altijd in je eigen pantheon."
    )

    if not heeft_toegang(tier, level, "favoriete_filosoof"):
        drempel = drempel_van("favoriete_filosoof")
        st.text_input(
            "Favoriete filosoof",
            value="",
            disabled=True,
            placeholder=f"Beschikbaar vanaf level {drempel}" if drempel else "Niet beschikbaar",
            key="favoriete_filosoof_disabled"
        )
        return

    opties = ["Geen"] + beschikbare_filosofen(tier, level)
    huidige = profiel.get("favoriete_filosoof") or "Geen"
    if huidige not in opties:
        huidige = "Geen"

    keuze = st.selectbox(
        "Favoriete filosoof",
        opties,
        index=opties.index(huidige),
        format_func=lambda x: (
            f"{FILOSOFEN[x]['emoji']} {FILOSOFEN[x]['naam']}"
            if x in FILOSOFEN else "Geen"
        ),
        key="favoriete_filosoof_keuze"
    )

    if keuze != huidige:
        nieuwe_favoriet = None if keuze == "Geen" else keuze
        oude_favoriet = profiel.get("favoriete_filosoof")

        # Werk het eigen pantheon bij
        eigen_pantheon = list(profiel.get("eigen_pantheon", []))

        # Verwijder de oude favoriet
        if oude_favoriet and oude_favoriet in eigen_pantheon:
            eigen_pantheon.remove(oude_favoriet)

        # Voeg de nieuwe favoriet toe
        if nieuwe_favoriet:
            if nieuwe_favoriet not in eigen_pantheon:
                if len(eigen_pantheon) >= 5:
                    eigen_pantheon = eigen_pantheon[:-1] + [nieuwe_favoriet]
                else:
                    eigen_pantheon.append(nieuwe_favoriet)

        profiel["favoriete_filosoof"] = nieuwe_favoriet
        profiel["eigen_pantheon"] = eigen_pantheon
        bewaar_profiel(profiel)
        st.success("Favoriete filosoof opgeslagen.")
        st.rerun()


def _toon_eigen_pantheon(profiel, level, tier):
    """Toont de keuze voor het eigen pantheon."""
    from tiers import beschikbare_filosofen
    from filosofen import FILOSOFEN

    st.markdown("#### Eigen pantheon")
    st.caption(
        "Kies vijf filosofen voor je eigen pantheon. "
        "Je favoriete filosoof zit er altijd in."
    )

    if tier == "sessie":
        st.text_input(
            "Eigen pantheon",
            value="",
            disabled=True,
            placeholder="Beschikbaar met een abonnement",
            key="eigen_pantheon_disabled"
        )
        return

    opties = beschikbare_filosofen(tier, level)
    if not opties:
        st.markdown("Je hebt nog geen filosofen vrijgespeeld.")
        return

    # Huidige pantheon
    eigen = list(profiel.get("eigen_pantheon", []))
    favoriet = profiel.get("favoriete_filosoof")

    # Zorg dat de favoriet erin zit
    if favoriet and favoriet not in eigen:
        if len(eigen) >= 5:
            eigen = eigen[:-1] + [favoriet]
        else:
            eigen.append(favoriet)

    # Toon de vijf keuzes
    nieuwe_eigen = []
    for i in range(5):
        huidige = eigen[i] if i < len(eigen) else None
        index = opties.index(huidige) if huidige in opties else 0

        keuze = st.selectbox(
            f"Filosoof {i + 1}",
            opties,
            index=index,
            format_func=lambda x: (
                f"{FILOSOFEN[x]['emoji']} {FILOSOFEN[x]['naam']}"
                if x in FILOSOFEN else x
            ),
            key=f"eigen_pantheon_{i}"
        )
        nieuwe_eigen.append(keuze)

    # Zorg dat de favoriet er altijd in zit
    if favoriet and favoriet not in nieuwe_eigen:
        nieuwe_eigen[-1] = favoriet
        st.caption(
            f"Let op: {FILOSOFEN[favoriet]['naam']} is je favoriet, "
            f"en is daarom op de laatste plek gezet."
        )

    if nieuwe_eigen != profiel.get("eigen_pantheon", []):
        profiel["eigen_pantheon"] = nieuwe_eigen
        bewaar_profiel(profiel)
        st.success("Eigen pantheon opgeslagen.")

def _toon_instellingen(profiel, gebruiker_id):
    """Toont de instellingen."""
    st.markdown("### Instellingen")
    st.caption("Deze functie komt later.")

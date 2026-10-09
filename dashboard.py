"""
Dashboard voor Aurelius.
Toont het archief, de voortgang en de favorieten.
"""

import streamlit as st

from filosofen import FILOSOFEN, PANTHEON_PER_LEVEL
from opslag import laad_sessies, bewaar_profiel


def toon_dashboard(gebruiker_id, profiel):
    """Toont het hele dashboard."""
    st.title("🏛️ Jouw dashboard")
    st.caption(f"Welkom terug, {gebruiker_id}.")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Archief", "Voortgang", "Favorieten", "Gespreksvormen"]
    )

    with tab1:
        _toon_archief(gebruiker_id, profiel)

    with tab2:
        _toon_voortgang(profiel)

    with tab3:
        _toon_favorieten(profiel)

    with tab4:
        _toon_gespreksvormen(profiel, gebruiker_id)
# ============================================================
# Archief
# ============================================================
def _toon_archief(gebruiker_id, profiel):
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
            # PDF-download (alleen voor basic en gold)
            from tiers import heeft_toegang
            _tier = profiel.get("tier", "sessie")
            _level = profiel.get("level", 1)

            if heeft_toegang(_tier, _level, "pdf"):
                st.markdown("---")
                from pdf import maak_pdf
                try:
                    pdf_pad = maak_pdf(sessie=sessie)
                    with open(pdf_pad, "rb") as f:
                        pdf_bytes = f.read()
                    st.download_button(
                        "📄 Download als PDF",
                        pdf_bytes,
                        file_name=f"aurelius_{str(sessie.get('datum', ''))[:10]}.pdf",
                        mime="application/pdf",
                        key=f"pdf_{sessie.get('id', 'x')}",
                    )
                except Exception as e:
                    st.caption(f"PDF kon niet worden gemaakt: {e}")
            # Vervolggesprek (alleen voor gold)
            if heeft_toegang(_tier, _level, "vervolggesprek"):
                if st.button(
                    "🔄 Vervolggesprek",
                    key=f"vervolg_{sessie.get('id', 'x')}",
                    use_container_width=True,
                    type="primary",
                ):
                    st.session_state.profiel["gespreksvorm"] = "vervolggesprek"
                    st.session_state.profiel["vervolg_sessie_id"] = sessie.get("id")
                    st.session_state.profiel["sessie_afgerond"] = False
                    from opslag import bewaar_profiel
                    bewaar_profiel(st.session_state.profiel)
                    st.session_state.toon_dashboard = False
                    st.session_state.toon_duur_keuze = True
                    st.rerun()
# ============================================================
# Voortgang
# ============================================================
def _toon_voortgang(profiel):
    """Toont de voortgang van de gebruiker."""
    st.markdown("### Jouw voortgang")
    st.markdown(f"**Level:** {profiel.get('level', 1)}")
    st.markdown(f"**Tier:** {profiel.get('tier', 'sessie')}")
    st.caption("Meer statistieken volgen later.")


# ============================================================
# Favorieten
# ============================================================
def _toon_favorieten(profiel):
    """Toont de favorieten van de gebruiker."""
    st.markdown("### Jouw favorieten")

    level = profiel.get("level", 1)
    tier = profiel.get("tier", "sessie")

    _toon_favoriet_filosoof(profiel, level, tier)

    st.markdown("---")

    _toon_eigen_pantheon(profiel, level, tier)


def _toon_favoriet_filosoof(profiel, level, tier):
    """Toont de keuze voor de favoriete filosoof."""
    from tiers import heeft_toegang, beschikbare_filosofen, drempel_van

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
            placeholder=f"Beschikbaar vanaf level {drempel}"
            if drempel else "Niet beschikbaar",
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
    from tiers import heeft_toegang, beschikbare_filosofen, drempel_van

    st.markdown("#### Eigen pantheon")
    st.caption(
        "Kies vijf filosofen voor je eigen pantheon. "
        "Je favoriete filosoof zit er altijd in."
    )

    # Toegangscheck op basis van tier én level
    if not heeft_toegang(tier, level, "eigen_pantheon"):
        drempel = drempel_van("eigen_pantheon")
        st.text_input(
            "Eigen pantheon",
            value="",
            disabled=True,
            placeholder=(
                f"Beschikbaar vanaf level {drempel}"
                if drempel else "Beschikbaar met een abonnement"
            ),
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

    # Als er een favoriet is, dan zijn er vier keuzes.
    # Anders zijn er vijf keuzes.
    if favoriet:
        aantal_keuzes = 4
        if favoriet in eigen:
            eigen.remove(favoriet)
    else:
        aantal_keuzes = 5

    # Toon de keuzes
    nieuwe_eigen = []
    for i in range(aantal_keuzes):
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

    # Voeg de favoriet toe als die er is
    if favoriet:
        nieuwe_eigen.append(favoriet)
        st.markdown(
            f"**Jouw favoriet:** "
            f"{FILOSOFEN[favoriet]['emoji']} {FILOSOFEN[favoriet]['naam']} "
            f"(staat vast op de laatste plek)"
        )

    # Sla het pantheon op als het veranderd is
    if nieuwe_eigen != profiel.get("eigen_pantheon", []):
        profiel["eigen_pantheon"] = nieuwe_eigen
        bewaar_profiel(profiel)
        st.success("Eigen pantheon opgeslagen.")

# ============================================================
# Gespreksvormen
# ============================================================

def _toon_gespreksvormen(profiel, gebruiker_id):
    from gespreksvormen import GESPREKSVORMEN
    from tiers import heeft_toegang, drempel_van
    
    tier = profiel.get("tier", "sessie")
    level = profiel.get("level", 1)
    
    st.markdown("### Kies een gespreksvorm")
    st.caption("Waarmee wil je beginnen?")
    
    if not heeft_toegang(tier, level, "gespreksvormen"):
        drempel = drempel_van("gespreksvormen")
        st.text_input(
            "Gespreksvormen",
            value="",
            disabled=True,
            placeholder=f"Beschikbaar vanaf level {drempel}" if drempel else "Beschikbaar met een abonnement",
            key="gespreksvormen_disabled",
        )
        return
    
    # De drie vormen: themagesprek, grote_dialoog, tweegesprek
    vormen = ["themagesprek", "grote_dialoog", "tweegesprek", "groot_pantheon"]
    
    col1, col2 = st.columns(2)
    
    for i, naam in enumerate(vormen):
        vorm = GESPREKSVORMEN[naam]
        kolom = col1 if i % 2 == 0 else col2
        with kolom:
            st.markdown(f"**{vorm['icoon']} {vorm['naam']}**")
            st.caption(vorm["beschrijving"])
            if st.button(
                "Start",
                key=f"vorm_{naam}",
                use_container_width=True,
                type="primary",
            ):
                st.session_state.profiel["gespreksvorm"] = naam
                st.session_state.profiel["sessie_afgerond"] = False
                from opslag import bewaar_profiel
                bewaar_profiel(st.session_state.profiel)
                st.session_state.toon_dashboard = False
                st.session_state.toon_duur_keuze = True
                st.rerun()

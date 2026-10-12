"""
Acceptatiescherm voor privacyverklaring en algemene voorwaarden.
Wordt getoond vóór de betaling.
"""

import streamlit as st


def toon_acceptatie():
    """
    Toont het acceptatiescherm.
    Geeft True terug als de gebruiker akkoord is gegaan.
    """
    st.markdown("## 📋 Voordat je verdergaat")
    st.markdown(
        "Lees onze voorwaarden en privacyverklaring. "
        "Je moet ze accepteren voordat je een sessie of abonnement kunt kopen."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📜 Privacyverklaring lezen", use_container_width=True):
            st.session_state.toon_privacy = True
            st.rerun()

    with col2:
        if st.button("📋 Algemene voorwaarden lezen", use_container_width=True):
            st.session_state.toon_voorwaarden = True
            st.rerun()

    st.markdown("---")

    akkoord = st.checkbox(
        "Ik heb de privacyverklaring en de algemene voorwaarden gelezen "
        "en ik ga ermee akkoord."
    )

    if akkoord:
        if st.button("Doorgaan naar betaling", type="primary"):
            st.session_state.acceptatie_gedaan = True
            return True
    else:
        st.button("Doorgaan naar betaling", disabled=True, type="primary")

    return False

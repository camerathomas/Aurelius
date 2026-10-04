"""
Wendingen voor Aurelius.
Elke wending is een korte onderbreking van het gesprek, waarna
het gesprek gewoon doorgaat.
"""

import random

WENDINGEN = [
    {
        "naam": "De anekdote",
        "instructie": (
            "[WENDING: DE ANEKDOTE]\n"
            "Deze wending wordt gedaan door een filosoof uit het pantheon "
            "van deze sessie, iemand die nog niet of nauwelijks sprak. "
            "Je ziet een patroon in wat de gebruiker heeft gezegd, en dat "
            "herinnert je aan iets uit je eigen werk. Citeer kort uit je "
            "eigen boek, noem de titel, en vraag of die vergelijking deels "
            "opgaat. Gebruik maximaal 5 zinnen."
        ),
    },
    {
        "naam": "De incheckvragen",
        "instructie": (
            "[WENDING: DE INCHECKVRAGEN]\n"
            "Deze wending wordt gedaan door een filosoof uit het pantheon "
            "van deze sessie, iemand die nog niet of nauwelijks sprak. "
            "Kijk terug op de incheck van de gebruiker (wat speelt er, "
            "emotie, overzicht, intentie, waarde-volgorde). Stel één vraag "
            "die direct voortkomt uit wat de gebruiker daar heeft ingevuld. "
            "Als de overzicht-slider laag was, vraag daar dan naar. Gebruik "
            "maximaal 4 zinnen."
        ),
    },
    {
        "naam": "De spiegel",
        "instructie": (
            "[WENDING: DE SPIEGEL]\n"
            "Deze wending wordt gedaan door een filosoof uit het pantheon "
            "van deze sessie, iemand die nog niet of nauwelijks sprak. "
            "Vat in één zin samen wat de gebruiker net zei, in jouw eigen "
            "woorden, zonder oordeel. Vraag dan: 'Klopt dat?' of 'Is dat "
            "wat je bedoelt?' Wacht op het antwoord en ga daarna verder "
            "met één verdiepende vraag. Gebruik maximaal 4 zinnen."
        ),
    },
    {
        "naam": "De andere kant",
        "instructie": (
            "[WENDING: DE ANDERE KANT]\n"
            "Deze wending wordt gedaan door een filosoof uit het pantheon "
            "van deze sessie, iemand die nog niet of nauwelijks sprak. "
            "Neem het tegenovergestelde standpunt in van wat de gebruiker "
            "net zei. Doe dit niet provocerend, maar onderzoekend: 'Stel "
            "nu eens dat het omgekeerde waar is...' of 'Wat als je je "
            "vergist?' Vraag de gebruiker zijn positie te verdedigen of "
            "bij te stellen. Gebruik maximaal 4 zinnen."
        ),
    },
]


def kies_random_wending():
    """Kiest een willekeurige wending uit de lijst."""
    return random.choice(WENDINGEN)


def moet_wending_komen(minuten, duur, al_geweest):
    """
    Bepaalt of er nu een random wending moet komen.
    - Om de 5 minuten sessietijd.
    - Niet op het midden (daar komt de vaste [OVERGANGSMOMENT]).
    - Niet op het einde (dus niet op minuut == duur).
    - Niet twee keer op dezelfde drempel.

    Geeft een drempel-index terug (int), of None.
    """
    if duur <= 0:
        return None

    midden = duur / 2

    drempels = []
    teller = 5
    while teller < duur:
        # Sla het midden over
        if abs(teller - midden) >= 2.5:
            drempels.append(teller)
        teller += 5

    for i, drempel in enumerate(drempels):
        if minuten >= drempel and i not in al_geweest:
            return i

    return None

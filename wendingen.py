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
            "Je herkent in deze beurt een patroon in de redenering van de "
            "gebruiker — iets dat je ook beschreven hebt in je eigen werk. "
            "Je vertelt in maximaal 3 zinnen een korte anekdote of passage "
            "uit je eigen boek, en noemt de titel. Daarna vraag je of die "
            "vergelijking deels opgaat voor wat de gebruiker zei. "
            "Doe NIETS anders. Geen Socratische vraag. Geen doorvragen. "
            "Alleen de anekdote en de vraag."
        ),
    },
    {
        "naam": "De incheckvragen",
        "instructie": (
            "Je verbindt in deze beurt een van de vier waarden "
            "(vertrouwen, respect, verbinding, analyse) met iets wat de "
            "gebruiker zojuist heeft gezegd. Je kijkt ook naar de incheck "
            "(wat speelt er, emotie, overzicht, intentie, waarde-volgorde). "
            "Je stelt ÉÉN vraag die die twee met elkaar verbindt. Als de "
            "overzicht-slider laag was, mag je daar ook naar vragen. "
            "Doe NIETS anders. Geen Socratische vraag. Alleen deze ene vraag."
        ),
    },
    {
        "naam": "De spiegel",
        "instructie": (
            "Je vat in deze beurt in ÉÉN zin samen wat de gebruiker net zei, "
            "in jouw eigen woorden, zonder oordeel. Daarna vraag je: 'Klopt "
            "dat?' of 'Is dat wat je bedoelt?' Doe NIETS anders. Geen "
            "Socratische vraag. Geen doorvragen. Alleen de samenvatting en "
            "de vraag."
        ),
    },
    {
        "naam": "De andere kant",
        "instructie": (
            "Je neemt in deze beurt het tegenovergestelde standpunt in van "
            "wat de gebruiker net zei. Doe dit onderzoekend, niet "
            "provocerend: 'Stel nu eens dat het omgekeerde waar is...' of "
            "'Wat als je je vergist?' Vraag de gebruiker zijn positie te "
            "verdedigen. Doe NIETS anders. Geen Socratische vraag. Alleen "
            "het tegenovergestelde standpunt en de vraag."
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

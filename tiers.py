"""
Tiers voor Aurelius.
Bepaalt welke mogelijkheden een gebruiker heeft, op basis van tier en level.

Drie tiers:
- sessie: één losse sessie, geen abonnement.
- basic: maandelijks, speelt de levels vrij.
- gold: maandelijks, alles vanaf het begin.
"""


# ============================================================
# De tiers
# ============================================================
TIERS = {
    "sessie": {
        "naam": "Losse sessie",
        "beschrijving": "Eén sessie. Geen abonnement.",
        "toegang": {
            "gesprek": True,
            "archief": False,
            "pdf": False,
            "favoriete_filosoof": False,
            "favoriete_pantheon": False,
            "favoriete_stroming": False,
            "favoriete_onderwerp": False,
            "video": False,
            "elevenlabs": False,
            "eigen_pantheon": False,
        },
    },
    "basic": {
        "naam": "Basic",
        "beschrijving": "Speel de levels vrij, stap voor stap.",
        "toegang": {
            "gesprek": True,
            "archief": True,
            "pdf": True,
            "favoriete_filosoof": "level_5",
            "favoriete_pantheon": "level_7",
            "favoriete_stroming": "level_9",
            "favoriete_onderwerp": "level_10",
            "video": False,
            "elevenlabs": False,
            "eigen_pantheon": "level_5",
        },
    },
    "gold": {
        "naam": "Gold",
        "beschrijving": "Alles vanaf het begin.",
        "toegang": {
            "gesprek": True,
            "archief": True,
            "pdf": True,
            "favoriete_filosoof": True,
            "favoriete_pantheon": True,
            "favoriete_stroming": True,
            "favoriete_onderwerp": True,
            "video": True,
            "elevenlabs": True,
            "eigen_pantheon": True,
        },
    },
}


# ============================================================
# Toegangscheck
# ============================================================
def heeft_toegang(tier, level, functie):
    """
    Bepaalt of een gebruiker toegang heeft tot een functie.

    - tier: "sessie", "basic", of "gold"
    - level: het level van de gebruiker (int)
    - functie: de naam van de functie (bijv. "favoriete_filosoof")

    Geeft True of False terug.
    """
    if tier not in TIERS:
        return False

    waarde = TIERS[tier]["toegang"].get(functie, False)

    if waarde is True:
        return True
    if waarde is False:
        return False
    if isinstance(waarde, str) and waarde.startswith("level_"):
        try:
            drempel = int(waarde.replace("level_", ""))
        except ValueError:
            return False
        return level >= drempel
    return False


def drempel_van(functie):
    """
    Geeft de level-drempel van een functie, of None als er geen drempel is.
    Handig voor de UI, om te tonen "beschikbaar vanaf level X".
    """
    for tier_naam, tier in TIERS.items():
        waarde = tier["toegang"].get(functie)
        if isinstance(waarde, str) and waarde.startswith("level_"):
            try:
                return int(waarde.replace("level_", ""))
            except ValueError:
                return None
    return None


# ============================================================
# Beschikbare filosofen en pantheons
# ============================================================
def beschikbare_filosofen(tier, level):
    """
    Geeft de filosofen die de gebruiker heeft vrijgespeeld.

    - Gold: alle filosofen.
    - Basic en sessie: alleen de levels die zijn behaald.
    """
    from filosofen import FILOSOFEN, PANTHEON_PER_LEVEL

    if tier == "gold":
        return list(FILOSOFEN.keys())

    beschikbaar = []
    for lvl in range(1, level + 1):
        beschikbaar.extend(PANTHEON_PER_LEVEL.get(lvl, []))

    gezien = set()
    uniek = []
    for f in beschikbaar:
        if f not in gezien:
            gezien.add(f)
            uniek.append(f)
    return uniek


def beschikbare_pantheons(tier, level):
    """
    Geeft de pantheons die de gebruiker heeft vrijgespeeld.

    - Gold: alle pantheons.
    - Basic en sessie: alleen de levels die zijn behaald.
    """
    from filosofen import PANTHEON_PER_LEVEL

    if tier == "gold":
        return list(PANTHEON_PER_LEVEL.keys())

    return [lvl for lvl in range(1, level + 1) if lvl in PANTHEON_PER_LEVEL]


# ============================================================
# Standaard tier
# ============================================================
STANDAARD_TIER = "sessie"

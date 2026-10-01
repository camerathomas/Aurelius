"""
Het profiel van de gebruiker.
Alles wordt lokaal opgeslagen als JSON.
"""

import json
import os

PROFIEL_MAP = "profielen"


def laad_profiel(gebruiker_id):
    """Laadt het profiel van de gebruiker, of maakt een nieuw aan."""
    os.makedirs(PROFIEL_MAP, exist_ok=True)
    pad = os.path.join(PROFIEL_MAP, f"{gebruiker_id}.json")

    if os.path.exists(pad):
        with open(pad, "r", encoding="utf-8") as f:
            return json.load(f)

    # Nieuw profiel
    return {
        "gebruiker_id": gebruiker_id,
        "waarden": {
            "directheid": 5,
            "respect": 5,
            "vertrouwen": 5,
            "verbinding": 5,
            "analyse": 5,
        },
        "methoden": {
            "spiegel": 5,
            "troost": 5,
            "confrontatie": 5,
            "vraag": 5,
        },
        "themas": [],
        "gesprekken": [],
    }


def bewaar_profiel(gebruiker_id, profiel):
    """Slaat het profiel op."""
    os.makedirs(PROFIEL_MAP, exist_ok=True)
    pad = os.path.join(PROFIEL_MAP, f"{gebruiker_id}.json")
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(profiel, f, ensure_ascii=False, indent=2)

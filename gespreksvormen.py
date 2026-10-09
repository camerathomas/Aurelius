"""
Gespreksvormen voor Aurelius.
Elke gespreksvorm bepaalt de rol van de gebruiker en de rol van de
filosofen. Verder blijft alles hetzelfde: pantheon-principe, wendingen,
eindgesprek.
"""


GESPREKSVORMEN = {
    "themagesprek": {
        "naam": "Themagesprek",
        "beschrijving": "De filosofen reageren op wat jij inbrengt.",
        "icoon": "🏛️",
        "filosofen": "pantheon",
        "gebruiker_rol": "deelnemer",
        "prompt_toevoeging": (
            "Dit is een themagesprek. De gebruiker is het middelpunt. "
            "Reageer op wat de gebruiker zegt, ga dieper, onderzoek. "
            "Stel vragen die voortkomen uit wat de gebruiker inbrengt."
        ),
    },
    "grote_dialoog": {
        "naam": "Grote dialoog",
        "beschrijving": "De filosofen praten met elkaar. Jij kunt bijsturen.",
        "icoon": "🎭",
        "filosofen": "pantheon",
        "gebruiker_rol": "gastheer",
        "prompt_toevoeging": (
            "Dit is een grote dialoog. De filosofen praten met elkaar, "
            "reageren op elkaars standpunten, en dagen elkaar uit. "
            "De gebruiker is een gastheer die af en toe iets inbrengt. "
            "Reageer in eerste instantie op de vorige filosoof, niet op de "
            "gebruiker. Als de gebruiker iets zegt, reageer daar dan op, "
            "en ga daarna weer met de andere filosofen in gesprek."
        ),
    },
    "tweegesprek": {
        "naam": "Tweegesprek",
        "beschrijving": "Jij en één filosoof. Diepgaand.",
        "icoon": "🤝",
        "filosofen": "één",
        "gebruiker_rol": "deelnemer",
        "prompt_toevoeging": (
            "Dit is een tweegesprek. Jij en de gebruiker, één op één. "
            "Er zijn geen andere filosofen. Ga diep, neem de tijd, "
            "onderzoek wat de gebruiker inbrengt grondig. "
            "Stel vragen die voortkomen uit wat de gebruiker zegt."
        ),
    },
    "vervolggesprek": {
        "naam": "Vervolggesprek",
        "beschrijving": "Bouwt voort op een eerdere sessie.",
        "icoon": "🔄",
        "filosofen": "pantheon",
        "gebruiker_rol": "deelnemer",
        "prompt_toevoeging": (
            "Dit is een vervolggesprek. De gebruiker bouwt voort op een "
            "eerdere sessie. Je hebt de context van die sessie gekregen. "
            "Verwijs waar zinvol naar wat er eerder gezegd is, en "
            "onderzoek wat er sindsdien veranderd is."
        ),
    },
    "groot_pantheon": {
        "naam": "Groot Pantheon",
        "beschrijving": "Alle filosofen. Wie het beste past, krijgt de beurt.",
        "icoon": "🌌",
        "filosofen": "alles",
        "gebruiker_rol": "deelnemer",
        "prompt_toevoeging": (
            "Dit is het Groot Pantheon. Alle filosofen doen mee. "
            "Reageer alleen als je iets hebt toe te voegen dat werkelijk "
            "nieuw is. Als een andere filosoof beter past bij wat de "
            "gebruiker zegt, laat hem dan het woord nemen. "
            "Je hoeft niet te reageren als je niets toe te voegen hebt."
        ),
    },
}


def kies_filosofen(vorm_naam, pantheon, voorzitter=None):
    """
    Bepaalt welke filosofen meedoen aan deze gespreksvorm.
    - 'pantheon': het hele pantheon
    - 'één': alleen de voorzitter (of de eerste filosoof)
    - 'alles': alle filosofen uit alle pantheons
    """
    vorm = GESPREKSVORMEN.get(vorm_naam)
    if not vorm:
        return pantheon

    if vorm["filosofen"] == "alles":
        from filosofen import FILOSOFEN
        return list(FILOSOFEN.keys())

    if vorm["filosofen"] == "één":
        if voorzitter and voorzitter in pantheon:
            return [voorzitter]
        return pantheon[:1]

    return pantheon


def bouw_vorm_prompt(vorm_naam, context=None):
    """
    Bouwt de prompt-toevoeging voor deze gespreksvorm.
    Wordt aan de system prompt toegevoegd.
    """
    vorm = GESPREKSVORMEN.get(vorm_naam)
    if not vorm:
        return ""

    prompt = vorm["prompt_toevoeging"]

    if context:
        prompt += f"\n\n[CONTEXT VAN EERDERE SESSIE]\n{context}"

    return prompt


def bouw_vervolg_context(sessie):
    """
    Bouwt de context van een eerdere sessie voor een vervolggesprek.
    Geeft een string terug die aan de prompt wordt toegevoegd.
    """
    if not sessie:
        return ""

    onderdelen = []

    # Het thema
    if sessie.get("thema"):
        onderdelen.append(f"Onderwerp: {sessie['thema']}")

    # De incheck
    incheck = sessie.get("incheck", {})
    if incheck:
        onderdelen.append(f"Wat speelde er: {incheck.get('openheid', '—')}")
        onderdelen.append(f"Emotie: {incheck.get('emotie', '—')}")
        onderdelen.append(f"Intentie: {incheck.get('intentie', '—')}")

    # De afsluiter (samenvatting van de vorige sessie)
    afsluiter = sessie.get("afsluiter", {})
    if afsluiter:
        onderdelen.append(
            f"Afsluiting door {afsluiter.get('naam', '?')}: "
            f"{afsluiter.get('tekst', '')}"
        )

    return "\n".join(onderdelen)


def is_beschikbaar(vorm_naam, profiel, heeft_eerdere_sessie=False):
    """
    Bepaalt of deze gespreksvorm beschikbaar is voor deze gebruiker.
    - Vervolggesprek: alleen als er een eerdere sessie is.
    - De andere: altijd beschikbaar.
    """
    if vorm_naam == "vervolggesprek":
        return heeft_eerdere_sessie
    return vorm_naam in GESPREKSVORMEN


def beschikbare_vormen(profiel, heeft_eerdere_sessie=False):
    """Geeft een lijst van beschikbare gespreksvormen."""
    return [
        naam for naam in GESPREKSVORMEN
        if is_beschikbaar(naam, profiel, heeft_eerdere_sessie)
    ]

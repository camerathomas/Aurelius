"""
Groot Pantheon — alle filosofen bij elkaar.
Kiest de filosoof die het beste past bij wat de gebruiker zegt.
"""


def kies_beste_filosoof(gebruiker_input, pantheon, profiel):
    """
    Kiest de filosoof die het beste past bij het onderwerp.
    - Kijkt naar de thema's van elke filosoof.
    - Geeft de filosoof met de hoogste score terug.
    - Als niemand past: de voorzitter.
    """
    from filosofen import FILOSOFEN

    if not gebruiker_input:
        return pantheon[0] if pantheon else "marcus_aurelius"

    invoer = gebruiker_input.lower()
    scores = {}

    for f in pantheon:
        filosoof = FILOSOFEN.get(f, {})
        themas = filosoof.get("themas", [])
        score = 0
        for thema in themas:
            if thema.lower() in invoer:
                score += 2
        scores[f] = score

    # Pak de filosoof met de hoogste score
    if scores:
        beste = max(scores, key=scores.get)
        if scores[beste] > 0:
            return beste

    # Als niemand past: de voorzitter
    voorzitter = profiel.get("voorzitter")
    if voorzitter and voorzitter in pantheon:
        return voorzitter

    return pantheon[0] if pantheon else "marcus_aurelius"

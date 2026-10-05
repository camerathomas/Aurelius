"""
evaluatie.py — het eindgesprek van de filosofen.

Dit bestand bevat:
- De prompts (ronde 1, ronde 2 en de afsluiter).
- De functie haal_reacties_op() die de AI aanroept en de JSON parseert.
- De functie bouw_context() die de context-string voor de prompts maakt.
- De functie bepaal_meest_gesproken() die uitzoekt wie het meest sprak.
- De functie verzamel_alle_reacties() die alles in de juiste volgorde zet.
- De functie bereken_leestijd() die de leestijd per reactie bepaalt.
"""

import json
from coach import chat


# ============================================================
# Prompts
# ============================================================

EVALUATIE_RONDE_1 = """
Je bent de regisseur van een filosofisch eindgesprek.

Je krijgt zo:
1. De laatste berichten van het gesprek.
2. Het pantheon: de filosofen die meedoen.

JOUW TAAK:
Laat elke filosoof in het pantheon reageren op wat de gebruiker heeft gezegd.
Dit is de EERSTE ronde. Elke filosoof reageert op de gebruiker, nog niet op
elkaar.

BELANGRIJK:
- De voorzitter van deze sessie doet NIET mee in deze ronde. 
  De voorzitter staat genoemd in de context onder --- VOORZITTER ---.
- Laat de andere filosofen reageren op wat de gebruiker heeft gezegd.

REGELS:
- Maximaal 3-4 zinnen per filosoof.
- In de stem en stijl van elke filosoof.
- Geen herhaling van wat al in het gesprek is gezegd.
- Elke filosoof heeft een eigen invalshoek.
- Geen therapeutisch, juridisch of financieel advies.

Sluit af met een JSON-blok tussen === JSON === en === EINDE JSON ===:

{
  "reacties": [
    {
      "filosoof": "plato",
      "naam": "Plato",
      "emoji": "🏛️",
      "tekst": "..."
    }
  ]
}

De volgorde van de reacties is de volgorde van het pantheon.
"""


EVALUATIE_RONDE_2 = """
Je bent de regisseur van een filosofisch eindgesprek.

Je krijgt zo:
1. De reacties uit de EERSTE ronde.
2. De laatste reacties uit het gesprek.

JOUW TAAK:
Laat elke filosoof reageren op wat de ANDERE filosofen in de eerste ronde
hebben gezegd. Dit is de TWEEDE ronde.

BELANGRIJK:
- De voorzitter doet NIET mee in deze ronde.
- Laat de andere filosofen reageren op wat in ronde 1 is gezegd.

REGELS:
- Maximaal 3 zinnen per filosoof.
- Ze mogen het oneens zijn, aanvullen, tegenspreken, of een nieuw
  perspectief toevoegen.
- In de stem en stijl van elke filosoof.
- Geen herhaling van wat al gezegd is.
- Geen therapeutisch, juridisch of financieel advies.

Sluit af met een JSON-blok tussen === JSON === en === EINDE JSON ===:

{
  "reacties": [
    {
      "filosoof": "socrates",
      "naam": "Socrates",
      "emoji": "🏛️",
      "tekst": "..."
    }
  ]
}
"""


EVALUATIE_AFSLUITER = """
Je bent de regisseur van een filosofisch eindgesprek.

Je krijgt zo:
1. De laatste berichten van het gesprek.
2. De twee rondes van het eindgesprek.
3. De naam van de filosoof die de afsluiting doet.

JOUW TAAK:
Laat die filosoof een afsluitend woord spreken. 4-6 zinnen.
Terugkijkend op wat er is gezegd, en met een laatste gedachte
voor de gebruiker.

REGELS:
- In de stem en stijl van die filosoof.
- Geen herhaling van wat al gezegd is.
- Geen therapeutisch, juridisch of financieel advies.

Sluit af met een JSON-blok tussen === JSON === en === EINDE JSON ===:

{
  "afsluiter": {
    "filosoof": "socrates",
    "naam": "Socrates",
    "emoji": "🏛️",
    "tekst": "..."
  }
}
"""


# ============================================================
# Hulpfuncties
# ============================================================

def haal_reacties_op(model, provider_key, prompt, context):
    """
    Vraagt de AI om een JSON-blok met reacties, en parseert het.
    Geeft een dict terug, of None bij een fout.
    """
    volledige_prompt = f"{prompt}\n\n--- CONTEXT ---\n{context}"

    antwoord = chat(
        model=model,
        messages=[{"role": "user", "content": volledige_prompt}],
        system_prompt="",
        provider=provider_key,
    )

    s = antwoord.find("=== JSON ===") + len("=== JSON ===")
    e = antwoord.find("=== EINDE JSON ===")
    if s > 0 and e > s:
        try:
            return json.loads(antwoord[s:e].strip())
        except Exception:
            return None
    return None


def bouw_context(profiel, geschiedenis, pantheon, extra=""):
    """
    Bouwt de context-string die aan de evaluatie-prompts wordt meegegeven.
    Zonder incheck. Alleen de laatste 12 berichten van het gesprek.
    """
    context = "--- GESPREK (laatste 12 berichten) ---\n"

    for b in geschiedenis[-12:]:
        rol = "Gebruiker" if b["naam"] == "Jij" else b["naam"]
        context += f"{rol}: {b['tekst']}\n\n"

    context += f"\n--- PANTHEON ---\n{', '.join(pantheon)}\n"

    if extra:
        context += f"\n--- EXTRA ---\n{extra}\n"

    return context


def bepaal_meest_gesproken(geschiedenis):
    """
    Bepaalt welke filosoof het vaakst aan het woord was in het gesprek.
    Geeft de naam terug (bijv. 'Socrates'), of None als er niets is.
    """
    tel = {}
    for b in geschiedenis:
        if b["naam"] != "Jij":
            tel[b["naam"]] = tel.get(b["naam"], 0) + 1

    if not tel:
        return None

    return max(tel, key=tel.get)


def verzamel_alle_reacties(rondes, afsluiter=None):
    """
    Zet alle reacties in één lijst, in de juiste volgorde:
    ronde 1, ronde 2, afsluiter.
    """
    alle = []

    for r in rondes.get("ronde_1", []):
        alle.append(("Ronde 1", r))
    for r in rondes.get("ronde_2", []):
        alle.append(("Ronde 2", r))

    if afsluiter:
        alle.append(("Afsluiting", afsluiter))

    return alle


def bereken_leestijd(tekst):
    """
    Berekent een redelijke leestijd in seconden voor een tekst.
    Uitgangspunt: 200 woorden per minuut, dus ~3 woorden per seconde.
    Met een minimum van 3 seconden en een maximum van 10 seconden.
    """
    if not tekst:
        return 3

    woorden = len(tekst.split())
    seconden = woorden / 3
    return max(3, min(10, seconden))

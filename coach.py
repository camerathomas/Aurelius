"""
De coach-logica: prompts bouwen, filosofen kiezen, en modellen aanroepen.
"""

import requests

OLLAMA_URL = "http://localhost:11434/api/chat"


def chat(model, messages, system_prompt=None, temperature=0.8, timeout=240):
    """Stuurt een chatverzoek naar Ollama."""
    msgs = []
    if system_prompt:
        msgs.append({"role": "system", "content": system_prompt})
    msgs.extend(messages)

    payload = {
        "model": model,
        "messages": msgs,
        "stream": False,
        "options": {"temperature": temperature},
        "think": False,
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
        r.raise_for_status()
        return r.json()["message"]["content"]
    except requests.exceptions.ReadTimeout:
        return "⚠️ Het model deed er te lang over. Probeer het opnieuw."
    except requests.exceptions.ConnectionError:
        return "⚠️ Geen verbinding met Ollama. Draait `ollama serve`?"
    except Exception as e:
        return f"⚠️ Fout: {e}"


def bouw_coach_prompt(filosoof, profiel, modus):
    """Bouwt de system prompt voor de coach."""
    basis = (
        "Je bent een filosofische coach. Je luistert meer dan je spreekt. "
        "Je oordeelt niet. Je geeft geen advies. Je stelt korte, open vragen. "
        "Je vleit niet. Geen 'wat een fascinerende visie'. Geen superlatieven. "
        "Antwoord in maximaal 3 zinnen."
    )

    stem = f"[DE STEM DIE JE NU SPREEKT]\n{filosoof['prompt']}"

    stijl = (
        "[STIJL]\n"
        "- Maximaal 3 zinnen.\n"
        "- Geen superlatieven.\n"
        "- Geen echo van labels.\n"
        "- Reageer op de gebruiker, niet op jezelf."
    )

    context = (
        f"[CONTEXT]\n"
        f"Modus: {modus}\n"
        f"Thema's van de gebruiker: {', '.join(profiel.get('themas', [])) or 'onbekend'}"
    )

    return f"{basis}\n\n{stem}\n\n{stijl}\n\n{context}"


def kies_filosoof(profiel, pantheon, gebruikers_input):
    """Kiest een filosoof op basis van het profiel en de input."""
    # Simpele versie: kies op basis van thema-match
    invoer = gebruikers_input.lower()
    for naam in pantheon:
        from filosofen import FILOSOFEN
        filosoof = FILOSOFEN[naam]
        for thema in filosoof.get("themas", []):
            if thema in invoer:
                return naam
    # Fallback: eerste uit het pantheon
    return pantheon[0] if pantheon else "aurelius"

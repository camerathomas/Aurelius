"""
De coach-logica: prompts bouwen, filosofen kiezen, en modellen aanroepen.
Ondersteunt Ollama (lokaal) en Gemini (online).
"""

import os
import requests

# ============================================================
# Configuratie
# ============================================================
OLLAMA_URL = "http://localhost:11434/api/chat"


def _laad_gemini_key():
    """Laadt de Gemini API-sleutel uit Streamlit secrets of omgeving.

    Zoekt op drie plekken:
    1. Onder [connections.aurelius] (nieuwe locatie)
    2. Op de root van secrets (oude locatie)
    3. In omgevingsvariabelen
    """
    # Probeer Streamlit secrets
    try:
        import streamlit as st

        # 1. Nieuwe locatie: onder connections.aurelius
        try:
            return st.secrets["connections"]["aurelius"]["GEMINI_API_KEY"]
        except (KeyError, Exception):
            pass

        # 2. Oude locatie: op de root
        try:
            return st.secrets["GEMINI_API_KEY"]
        except (KeyError, Exception):
            pass
    except Exception:
        pass

    # 3. Fallback: omgevingsvariabele
    return os.environ.get("GEMINI_API_KEY", "")


# ============================================================
# Ollama
# ============================================================
def chat_ollama(model, messages, system_prompt=None, temperature=0.8, timeout=240):
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


# ============================================================
# Gemini
# ============================================================
def chat_gemini(model, messages, system_prompt=None, temperature=0.8):
    """Stuurt een chatverzoek naar Gemini."""
    api_key = _laad_gemini_key()
    if not api_key:
        return "⚠️ Geen Gemini API-sleutel gevonden. Zet GEMINI_API_KEY in secrets."

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)

        # Bouw de inhoud op voor de nieuwe SDK
        contents = []
        for m in messages:
            rol = "user" if m["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=rol,
                    parts=[types.Part(text=m["content"])]
                )
            )

        config = types.GenerateContentConfig(
            temperature=temperature,
            system_instruction=system_prompt,
        )

        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=config,
        )

        return response.text

    except Exception as e:
        return f"⚠️ Gemini fout: {e}"


# ============================================================
# Algemene chat-functie
# ============================================================
def chat(model, messages, system_prompt=None, temperature=0.8, provider="ollama"):
    """Kiest tussen Ollama en Gemini op basis van de provider."""
    if provider == "gemini":
        return chat_gemini(model, messages, system_prompt, temperature)
    return chat_ollama(model, messages, system_prompt, temperature)


# ============================================================
# Prompt bouwen
# ============================================================

def bouw_coach_prompt(filosoof, profiel, modus, fase=None, vragen=None):
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

    fase_blok = ""
    if fase:
        fase_blok = f"\n\n[FASE]\nJe zit nu in de fase: {fase}."
        if vragen:
            fase_blok += (
                "\nHier zijn vragen die bij deze fase passen:\n"
                + "\n".join(f"- {v}" for v in vragen)
                + "\n\nGebruik deze vragen als richtlijn, maar pas ze aan op wat de gebruiker zegt."
            )

    return f"{basis}\n\n{stem}\n\n{stijl}\n\n{context}{fase_blok}"

# ============================================================
# Filosoof kiezen
# ============================================================
def kies_filosoof(profiel, pantheon, gebruikers_input):
    """Kiest een filosoof op basis van het profiel en de input."""
    from filosofen import FILOSOFEN

    invoer = gebruikers_input.lower()

    # Zoek een filosoof wiens thema's matchen
    for naam in pantheon:
        filosoof = FILOSOFEN[naam]
        for thema in filosoof.get("themas", []):
            if thema in invoer:
                return naam

    # Fallback: eerste uit het pantheon
    return pantheon[0] if pantheon else "aurelius"

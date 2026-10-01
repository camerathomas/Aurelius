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
    """Laadt de Gemini API-sleutel uit Streamlit secrets of omgeving."""
    try:
        import streamlit as st
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
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
        import google.generativeai as genai
        genai.configure(api_key=api_key)

        generation_config = genai.types.GenerationConfig(
            temperature=temperature,
        )

        model_instance = genai.GenerativeModel(
            model_name=model,
            system_instruction=system_prompt,
            generation_config=generation_config,
        )

        # Bouw de geschiedenis op
        history = []
        for m in messages[:-1]:
            history.append({
                "role": "user" if m["role"] == "user" else "model",
                "parts": [m["content"]],
            })

        chat_session = model_instance.start_chat(history=history)
        laatste = messages[-1]["content"] if messages else ""
        response = chat_session.send_message(laatste)
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

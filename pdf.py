"""
Aurelius — PDF-export.
Aurelius is een onderdeel van DenkKrant.
"""

import os
import re
from datetime import datetime

from weasyprint import HTML, CSS


# ---------- Constanten ----------

DISCLAIMER = (
    "Dit gesprek is een filosofische oefening. Het is geen therapie, "
    "geen advies, en geen diagnose. Het is een verslag van een gesprek "
    "tussen jou en een pantheon van filosofen."
)


# ---------- Emoji-filter ----------

_EMOJI_PATROON = re.compile(
    "["
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001F1E0-\U0001F1FF"
    "\U00002600-\U000026FF"
    "\U00002700-\U000027BF"
    "]+",
    flags=re.UNICODE,
)


def _verwijder_emojis(tekst):
    if not tekst:
        return ""
    return _EMOJI_PATROON.sub("", tekst).strip()


# ---------- Hulpfuncties ----------

def _esc(tekst):
    if tekst is None:
        return ""
    tekst = str(tekst)
    return (
        tekst.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
    )


def _alineas(tekst):
    if not tekst:
        return ""
    blokken = re.split(r"\n\s*\n", tekst.strip())
    return "".join(
        f"<p>{_esc(b).replace(chr(10), '<br>')}</p>" for b in blokken
    )


# ---------- Secties ----------

def _cover(datum, thema, pantheon_namen, duur):
    return f"""
    <div class="cover">
        <div class="merk">Aurelius</div>
        <h1>Gesprek met de filosofen</h1>
        <div class="subtitel">{_esc(thema) if thema else "Een sessie"}</div>
        <div class="accentlijn"></div>
        <div class="meta">
            {_esc(datum)}<br>
            {_esc(pantheon_namen)}<br>
            Duur: {_esc(duur)} minuten
        </div>
        <div class="disclaimer">
            {_esc(DISCLAIMER)}
        </div>
        <div class="sideline">
            Aurelius is een onderdeel van DenkKrant
        </div>
    </div>
    """


def _inhoudsopgave(hoofdstukken):
    items = "".join(
        f'<li>'
        f'<a href="#{anker}">'
        f'<span class="inhoud-nummer">{_esc(nummer)}</span>'
        f'{_esc(titel)}'
        f'</a>'
        f'</li>'
        for nummer, titel, anker in hoofdstukken
    )
    return f"""
    <section class="inhoud" id="inhoud">
        <h2>Inhoud</h2>
        <div class="hoofdstuk-lijn"></div>
        <ul>{items}</ul>
    </section>
    """


def _hoofdstuk(nummer, titel, inhoud_html, kleurklasse="h1", anker=None):
    if anker is None:
        anker = f"h{nummer}"
    return f"""
    <section class="hoofdstuk {kleurklasse}" id="{anker}">
        <div class="terug-naar-inhoud">
            <a href="#inhoud">↑ Inhoud</a>
        </div>
        <div class="hoofdstuk-nummer">{_esc(nummer)}</div>
        <h2>{_esc(titel)}</h2>
        <div class="hoofdstuk-lijn"></div>
        <div class="sectie">{inhoud_html}</div>
    </section>
    """


# ---------- Hoofdstuk-inhouden ----------

def _incheck_html(incheck):
    if not incheck:
        return "<p>Geen incheck gevonden.</p>"

    html = "<table class='velden'>"
    html += f"<tr><td>Wat speelt er</td><td>{_esc(incheck.get('openheid', '—'))}</td></tr>"
    html += f"<tr><td>Emotie</td><td>{_esc(incheck.get('emotie', '—'))}</td></tr>"
    html += f"<tr><td>Overzicht</td><td>{_esc(incheck.get('overzicht', '—'))}/10</td></tr>"
    html += f"<tr><td>Intentie</td><td>{_esc(incheck.get('intentie', '—'))}</td></tr>"

    volgorde = incheck.get("volgorde", [])
    if volgorde:
        html += f"<tr><td>Volgorde</td><td>{_esc(' → '.join(volgorde))}</td></tr>"

    html += f"<tr><td>Duur</td><td>{_esc(incheck.get('duur', '—'))}</td></tr>"
    html += "</table>"

    return html


def _gesprek_html(gesprek):
    if not gesprek:
        return "<p>Geen gesprek gevonden.</p>"

    html = ""
    for bericht in gesprek:
        naam = bericht.get("naam", "?")
        tekst = bericht.get("tekst", "")
        klasse = "bericht gebruiker" if naam == "Jij" else "bericht"

        tekst_html = _verwijder_emojis(_alineas(tekst))

        html += f"""
        <div class="{klasse}">
            <div class="spreker">{_esc(naam)}</div>
            <div class="tekst">{tekst_html}</div>
        </div>
        """
    return html


def _rondes_html(rondes):
    if not rondes:
        return "<p>Geen eindgesprek gevonden.</p>"

    html = ""
    ronde_labels = {
        "ronde_1": "Ronde 1",
        "ronde_2": "Ronde 2",
    }

    for ronde_naam, reacties in rondes.items():
        label = ronde_labels.get(ronde_naam, ronde_naam.replace("_", " ").title())
        html += f"<h3>{_esc(label)}</h3>"
        for r in reacties:
            naam = r.get("naam", "?")
            tekst = r.get("tekst", "")
            tekst_html = _verwijder_emojis(_alineas(tekst))
            html += f"""
            <div class="bericht">
                <div class="spreker">{_esc(naam)}</div>
                <div class="tekst">{tekst_html}</div>
            </div>
            """
    return html


def _afsluiter_html(afsluiter):
    if not afsluiter:
        return "<p>Geen afsluiting gevonden.</p>"

    naam = afsluiter.get("naam", "?")
    tekst = afsluiter.get("tekst", "")
    tekst_html = _verwijder_emojis(_alineas(tekst))

    return f"""
    <div class="citaat">
        {tekst_html}
        <span class="bron">— {_esc(naam)}</span>
    </div>
    """


# ---------- Hoofdfunctie ----------

def maak_pdf(
    *,
    sessie,
    uitvoerpad=None,
):
    """
    Maakt een PDF van een sessie.

    sessie is een dict zoals opgeslagen in de database:
    {
        'datum': '...',
        'thema': '...',
        'incheck': {...},
        'gesprek': [...],
        'rondes': {...},
        'afsluiter': {...},
        'duur_minuten': 10,
        'pantheon': [...],
    }
    """
    from filosofen import FILOSOFEN

    datum_str = str(sessie.get("datum", ""))[:16]
    try:
        dt = datetime.strptime(datum_str, "%Y-%m-%d %H:%M")
        datum = dt.strftime("%d %B %Y").lstrip("0")
    except Exception:
        datum = datum_str

    thema = sessie.get("thema", "") or ""
    duur = sessie.get("duur_minuten", 10)

    pantheon = sessie.get("pantheon") or []
    if not isinstance(pantheon, list):
        pantheon = []
    pantheon_namen = ", ".join(
        FILOSOFEN[f]["naam"]
        for f in pantheon
        if f in FILOSOFEN
    ) or "—"

    if uitvoerpad is None:
        os.makedirs("pdfs", exist_ok=True)
        stempel = datetime.now().strftime("%Y%m%d_%H%M%S")
        uitvoerpad = f"pdfs/aurelius_{stempel}.pdf"

    # ---- Hoofdstukken voorbereiden ----
    hoofdstukken = [
        ("1", "Incheck", "h1"),
        ("2", "Gesprek", "h2"),
        ("3", "Eindgesprek", "h3"),
        ("4", "Afsluiting", "h4"),
    ]

    inhoudsopgave_html = _inhoudsopgave(hoofdstukken)

    # ---- Hoofdstukken opbouwen ----
    delen = []

    delen.append(_hoofdstuk(
        "1", "Incheck",
        _incheck_html(sessie.get("incheck", {})),
        "h1",
    ))

    delen.append(_hoofdstuk(
        "2", "Gesprek",
        _gesprek_html(sessie.get("gesprek", [])),
        "h2",
    ))

    delen.append(_hoofdstuk(
        "3", "Eindgesprek",
        _rondes_html(sessie.get("rondes", {})),
        "h3",
    ))

    delen.append(_hoofdstuk(
        "4", "Afsluiting",
        _afsluiter_html(sessie.get("afsluiter", {})),
        "h4",
    ))

    body = "\n".join(delen)

    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Aurelius — Sessie</title>
</head>
<body>
{_cover(datum, thema, pantheon_namen, duur)}
<span id="inhoud"></span>
{inhoudsopgave_html}
{body}
</body>
</html>
    """

    hier = os.path.dirname(os.path.abspath(__file__))
    css_pad = os.path.join(hier, "pdf_stijl.css")

    if os.path.exists(css_pad):
        stylesheets = [CSS(filename=css_pad)]
    else:
        stylesheets = []

    HTML(string=html, base_url=hier).write_pdf(
        uitvoerpad, stylesheets=stylesheets
    )

    return uitvoerpad

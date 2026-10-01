"""
Database-module voor Aurelius.
Werkt met Turso (libsql) voor cloud-opslag, of SQLite voor lokaal testen.
"""

import json
import streamlit as st
from datetime import datetime


def _krijg_verbinding():
    """Maakt verbinding met de database via Streamlit secrets."""
    return st.connection("aurelius", type="sql")


def initialiseer():
    """Maakt de tabellen aan als ze nog niet bestaan."""
    conn = _krijg_verbinding()
    with conn.session as s:
        s.execute("""
            CREATE TABLE IF NOT EXISTS profielen (
                gebruiker_id TEXT PRIMARY KEY,
                waarden TEXT,
                laatste_incheck TEXT,
                themas TEXT,
                waarde_volgorde TEXT,
                bijgewerkt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        s.execute("""
            CREATE TABLE IF NOT EXISTS berichten (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gebruiker_id TEXT,
                filosoof TEXT,
                rol TEXT,
                tekst TEXT,
                fase TEXT,
                tijd TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (gebruiker_id) REFERENCES profielen(gebruiker_id)
            )
        """)
        s.execute("""
            CREATE TABLE IF NOT EXISTS sessies (
                gebruiker_id TEXT PRIMARY KEY,
                actief INTEGER DEFAULT 0,
                start_tijd TIMESTAMP,
                verstreken_minuten INTEGER DEFAULT 0,
                fase TEXT,
                laatste_filosoof TEXT,
                FOREIGN KEY (gebruiker_id) REFERENCES profielen(gebruiker_id)
            )
        """)
        s.commit()


def bewaar_profiel(profiel):
    """Slaat een profiel op."""
    conn = _krijg_verbinding()
    with conn.session as s:
        s.execute("""
            INSERT OR REPLACE INTO profielen
            (gebruiker_id, waarden, laatste_incheck, themas, waarde_volgorde, bijgewerkt)
            VALUES (:id, :waarden, :incheck, :themas, :volgorde, CURRENT_TIMESTAMP)
        """, {
            "id": profiel["gebruiker_id"],
            "waarden": json.dumps(profiel.get("waarden", {})),
            "incheck": json.dumps(profiel.get("laatste_incheck", {})),
            "themas": json.dumps(profiel.get("themas", [])),
            "volgorde": json.dumps(profiel.get("waarde_volgorde", [])),
        })
        s.commit()


def laad_profiel(gebruiker_id):
    """Laadt een profiel, of maakt een nieuw aan."""
    conn = _krijg_verbinding()
    try:
        rijen = conn.query(
            "SELECT * FROM profielen WHERE gebruiker_id = :id",
            params={"id": gebruiker_id},
            ttl=0
        )
        if not rijen.empty:
            rij = rijen.iloc[0]
            return {
                "gebruiker_id": rij["gebruiker_id"],
                "waarden": json.loads(rij["waarden"]) if rij["waarden"] else {},
                "laatste_incheck": json.loads(rij["laatste_incheck"]) if rij["laatste_incheck"] else {},
                "themas": json.loads(rij["themas"]) if rij["themas"] else [],
                "waarde_volgorde": json.loads(rij["waarde_volgorde"]) if rij["waarde_volgorde"] else [],
            }
    except Exception:
        pass

    # Nieuw profiel
    return {
        "gebruiker_id": gebruiker_id,
        "waarden": {"directheid": 5, "respect": 5, "vertrouwen": 5, "verbinding": 5, "analyse": 5},
        "laatste_incheck": {},
        "themas": [],
        "waarde_volgorde": [],
    }


def bewaar_bericht(gebruiker_id, filosoof, rol, tekst, fase=None):
    """Slaat een bericht op."""
    conn = _krijg_verbinding()
    with conn.session as s:
        s.execute("""
            INSERT INTO berichten (gebruiker_id, filosoof, rol, tekst, fase)
            VALUES (:id, :filosoof, :rol, :tekst, :fase)
        """, {
            "id": gebruiker_id,
            "filosoof": filosoof,
            "rol": rol,
            "tekst": tekst,
            "fase": fase,
        })
        s.commit()


def laad_gesprek(gebruiker_id, limiet=50):
    """Laadt de laatste berichten van een gebruiker."""
    conn = _krijg_verbinding()
    try:
        df = conn.query(
            "SELECT * FROM berichten WHERE gebruiker_id = :id ORDER BY tijd ASC LIMIT :limiet",
            params={"id": gebruiker_id, "limiet": limiet},
            ttl=0
        )
        return df.to_dict("records")
    except Exception:
        return []


def wis_gesprek(gebruiker_id):
    """Verwijdert alle berichten van een gebruiker."""
    conn = _krijg_verbinding()
    with conn.session as s:
        s.execute("DELETE FROM berichten WHERE gebruiker_id = :id", {"id": gebruiker_id})
        s.commit()

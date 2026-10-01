"""
Database-module voor Aurelius.
Gebruikt de officiële libsql-client voor Turso (cloud) of SQLite (lokaal).
"""

import json
import streamlit as st


def _krijg_verbinding():
    """Maakt verbinding met Turso via de officiële libsql-client."""
    import libsql

    url = st.secrets["connections"]["aurelius"]["url"]
    token = st.secrets["connections"]["aurelius"]["auth_token"]
    return libsql.connect(database=url, auth_token=token)


def initialiseer():
    """Maakt de tabellen aan als ze nog niet bestaan."""
    conn = _krijg_verbinding()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profielen (
            gebruiker_id TEXT PRIMARY KEY,
            waarden TEXT,
            laatste_incheck TEXT,
            themas TEXT,
            waarde_volgorde TEXT,
            bijgewerkt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS berichten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gebruiker_id TEXT,
            filosoof TEXT,
            rol TEXT,
            tekst TEXT,
            fase TEXT,
            tijd TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def bewaar_profiel(profiel):
    """Slaat een profiel op."""
    conn = _krijg_verbinding()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO profielen
        (gebruiker_id, waarden, laatste_incheck, themas, waarde_volgorde, bijgewerkt)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """, (
        profiel["gebruiker_id"],
        json.dumps(profiel.get("waarden", {})),
        json.dumps(profiel.get("laatste_incheck", {})),
        json.dumps(profiel.get("themas", [])),
        json.dumps(profiel.get("waarde_volgorde", [])),
    ))

    conn.commit()
    conn.close()


def laad_profiel(gebruiker_id):
    """Laadt een profiel, of maakt een nieuw aan."""
    try:
        conn = _krijg_verbinding()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM profielen WHERE gebruiker_id = ?",
            (gebruiker_id,)
        )
        rij = cursor.fetchone()
        conn.close()

        if rij:
            return {
                "gebruiker_id": rij[0],
                "waarden": json.loads(rij[1]) if rij[1] else {},
                "laatste_incheck": json.loads(rij[2]) if rij[2] else {},
                "themas": json.loads(rij[3]) if rij[3] else [],
                "waarde_volgorde": json.loads(rij[4]) if rij[4] else [],
            }
    except Exception:
        pass

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
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO berichten (gebruiker_id, filosoof, rol, tekst, fase)
        VALUES (?, ?, ?, ?, ?)
    """, (gebruiker_id, filosoof, rol, tekst, fase))

    conn.commit()
    conn.close()


def laad_gesprek(gebruiker_id, limiet=50):
    """Laadt de laatste berichten van een gebruiker."""
    try:
        conn = _krijg_verbinding()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM berichten
            WHERE gebruiker_id = ?
            ORDER BY tijd ASC
            LIMIT ?
        """, (gebruiker_id, limiet))

        kolommen = [d[0] for d in cursor.description]
        rijen = cursor.fetchall()
        conn.close()

        return [dict(zip(kolommen, rij)) for rij in rijen]
    except Exception:
        return []


def wis_gesprek(gebruiker_id):
    """Verwijdert alle berichten van een gebruiker."""
    conn = _krijg_verbinding()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM berichten WHERE gebruiker_id = ?", (gebruiker_id,))
    conn.commit()
    conn.close()

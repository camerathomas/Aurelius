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

    extra_kolommen = [
        ("sessie_duur", "INTEGER DEFAULT 10"),
        ("heeft_eerder_gesproken", "INTEGER DEFAULT 0"),
        ("sessie_tijd", "REAL DEFAULT 0"),
        ("sessie_start", "REAL DEFAULT 0"),
        ("laatste_bericht", "REAL DEFAULT 0"),
        ("level", "INTEGER DEFAULT 1"),
        ("tier", "TEXT DEFAULT 'sessie'"),
        ("favoriete_filosoof", "TEXT"),
        ("eigen_pantheon", "TEXT"),
        ("sessie_afgerond", "INTEGER DEFAULT 1"),
        ("gebruik_eigen_pantheon", "INTEGER DEFAULT 0"),
        ("proefsessie_geweest", "INTEGER DEFAULT 0"),
        ("incheck_gedaan", "INTEGER DEFAULT 0"),
        ("betaald", "INTEGER DEFAULT 0"),
        ("welkom_geweest", "INTEGER DEFAULT 0"),
        ("gesprekken_gehad", "INTEGER DEFAULT 0"),
        ("sessies_gekocht", "INTEGER DEFAULT 1"),
    ]

    for kolom_naam, kolom_def in extra_kolommen:
        try:
            cursor.execute(
                f"ALTER TABLE profielen ADD COLUMN {kolom_naam} {kolom_def}"
            )
        except Exception:
            pass

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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gebruiker_id TEXT,
            datum TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            thema TEXT,
            incheck TEXT,
            gesprek TEXT,
            rondes TEXT,
            afsluiter TEXT,
            duur_minuten INTEGER,
            pantheon TEXT
        )
    """)

    conn.commit()
    conn.close()


def bewaar_profiel(profiel):
    """Slaat een profiel op."""
    if profiel.get("_is_fallback"):
        print(
            f"WAARSCHUWING: fallback-profiel niet opgeslagen "
            f"voor {profiel.get('gebruiker_id')}"
        )
        return

    conn = _krijg_verbinding()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO profielen
        (gebruiker_id, waarden, laatste_incheck, themas, waarde_volgorde,
         bijgewerkt,
         sessie_duur, heeft_eerder_gesproken, sessie_tijd, sessie_start,
         laatste_bericht, level, tier, favoriete_filosoof,
         eigen_pantheon, sessie_afgerond, gebruik_eigen_pantheon,
         proefsessie_geweest, incheck_gedaan, betaald, welkom_geweest,
         gesprekken_gehad, sessies_gekocht)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?)
    """, (
        profiel["gebruiker_id"],
        json.dumps(profiel.get("waarden", {})),
        json.dumps(profiel.get("laatste_incheck", {})),
        json.dumps(profiel.get("themas", [])),
        json.dumps(profiel.get("waarde_volgorde", [])),
        profiel.get("sessie_duur", 10),
        1 if profiel.get("heeft_eerder_gesproken", False) else 0,
        profiel.get("sessie_tijd", 0),
        profiel.get("sessie_start", 0),
        profiel.get("laatste_bericht", 0),
        profiel.get("level", 1),
        profiel.get("tier", "sessie"),
        profiel.get("favoriete_filosoof"),
        json.dumps(profiel.get("eigen_pantheon", []), ensure_ascii=False),
        1 if profiel.get("sessie_afgerond", True) else 0,
        1 if profiel.get("gebruik_eigen_pantheon", False) else 0,
        1 if profiel.get("proefsessie_geweest", False) else 0,
        1 if profiel.get("incheck_gedaan", False) else 0,
        1 if profiel.get("betaald", False) else 0,
        1 if profiel.get("welkom_geweest", False) else 0,
        profiel.get("gesprekken_gehad", 0),
        profiel.get("sessies_gekocht", 1),
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
                "_is_fallback": False,
                "gebruiker_id": rij[0],
                "waarden": json.loads(rij[1]) if rij[1] else {},
                "laatste_incheck": json.loads(rij[2]) if rij[2] else {},
                "themas": json.loads(rij[3]) if rij[3] else [],
                "waarde_volgorde": json.loads(rij[4]) if rij[4] else [],
                "sessie_duur": int(rij[6]) if len(rij) > 6 and rij[6] else 10,
                "heeft_eerder_gesproken": bool(rij[7]) if len(rij) > 7 and rij[7] else False,
                "sessie_tijd": float(rij[8]) if len(rij) > 8 and rij[8] else 0,
                "sessie_start": float(rij[9]) if len(rij) > 9 and rij[9] else 0,
                "laatste_bericht": float(rij[10]) if len(rij) > 10 and rij[10] else 0,
                "level": int(rij[11]) if len(rij) > 11 and rij[11] else 1,
                "tier": rij[12] if len(rij) > 12 and rij[12] else "sessie",
                "favoriete_filosoof": rij[13] if len(rij) > 13 and rij[13] else None,
                "eigen_pantheon": (
                    json.loads(rij[14]) if len(rij) > 14 and rij[14] else []
                ),
                "sessie_afgerond": (
                    bool(rij[15]) if len(rij) > 15 and rij[15] is not None else True
                ),
                "gebruik_eigen_pantheon": (
                    bool(rij[16]) if len(rij) > 16 and rij[16] else False
                ),
                "proefsessie_geweest": (
                    bool(rij[17]) if len(rij) > 17 and rij[17] else False
                ),
                "incheck_gedaan": (
                    bool(rij[18]) if len(rij) > 18 and rij[18] else False
                ),
                "betaald": (
                    bool(rij[19]) if len(rij) > 19 and rij[19] else False
                ),
                "welkom_geweest": (
                    bool(rij[20]) if len(rij) > 20 and rij[20] else False
                ),
                "gesprekken_gehad": (
                    int(rij[21]) if len(rij) > 21 and rij[21] else 0
                ),
                "sessies_gekocht": (
                    int(rij[22]) if len(rij) > 22 and rij[22] else 1
                ),
            }
    except Exception as e:
        print(f"FOUT bij laden profiel '{gebruiker_id}': {e}")

    return {
        "_is_fallback": True,
        "gebruiker_id": gebruiker_id,
        "waarden": {"directheid": 5, "respect": 5, "vertrouwen": 5, "verbinding": 5, "analyse": 5},
        "laatste_incheck": {},
        "themas": [],
        "waarde_volgorde": [],
        "sessie_duur": 10,
        "heeft_eerder_gesproken": False,
        "sessie_tijd": 0,
        "sessie_start": 0,
        "laatste_bericht": 0,
        "level": 1,
        "tier": "sessie",
        "favoriete_filosoof": None,
        "eigen_pantheon": [],
        "sessie_afgerond": True,
        "gebruik_eigen_pantheon": False,
        "proefsessie_geweest": False,
        "incheck_gedaan": False,
        "betaald": False,
        "welkom_geweest": False,
        "gesprekken_gehad": 0,
        "sessies_gekocht": 1,
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


def bewaar_sessie(gebruiker_id, thema, incheck, gesprek, rondes, afsluiter,
                  duur_minuten, pantheon):
    """Slaat een volledige sessie op in het archief."""
    conn = _krijg_verbinding()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sessies
        (gebruiker_id, thema, incheck, gesprek, rondes, afsluiter,
         duur_minuten, pantheon)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        gebruiker_id,
        thema,
        json.dumps(incheck, ensure_ascii=False),
        json.dumps(gesprek, ensure_ascii=False),
        json.dumps(rondes, ensure_ascii=False),
        json.dumps(afsluiter, ensure_ascii=False),
        duur_minuten,
        json.dumps(pantheon, ensure_ascii=False),
    ))

    conn.commit()
    conn.close()


def laad_sessies(gebruiker_id, limiet=20):
    """Laadt de laatste N gearchiveerde sessies van een gebruiker."""
    try:
        conn = _krijg_verbinding()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, datum, thema, incheck, gesprek, rondes, afsluiter,
                   duur_minuten, pantheon
            FROM sessies
            WHERE gebruiker_id = ?
            ORDER BY datum DESC
            LIMIT ?
        """, (gebruiker_id, limiet))

        rijen = cursor.fetchall()
        conn.close()

        sessies = []
        for rij in rijen:
            sessies.append({
                "id": rij[0],
                "datum": rij[1],
                "thema": rij[2],
                "incheck": json.loads(rij[3]) if rij[3] else {},
                "gesprek": json.loads(rij[4]) if rij[4] else [],
                "rondes": json.loads(rij[5]) if rij[5] else {},
                "afsluiter": json.loads(rij[6]) if rij[6] else {},
                "duur_minuten": rij[7],
                "pantheon": json.loads(rij[8]) if rij[8] else [],
            })
        return sessies
    except Exception:
        return []


def laad_sessie(gebruiker_id, sessie_id):
    """Laadt één specifieke sessie op basis van het id."""
    try:
        conn = _krijg_verbinding()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, datum, thema, incheck, gesprek, rondes, afsluiter,
                   duur_minuten, pantheon
            FROM sessies
            WHERE gebruiker_id = ? AND id = ?
        """, (gebruiker_id, sessie_id))

        rij = cursor.fetchone()
        conn.close()

        if not rij:
            return None

        return {
            "id": rij[0],
            "datum": rij[1],
            "thema": rij[2],
            "incheck": json.loads(rij[3]) if rij[3] else {},
            "gesprek": json.loads(rij[4]) if rij[4] else [],
            "rondes": json.loads(rij[5]) if rij[5] else {},
            "afsluiter": json.loads(rij[6]) if rij[6] else {},
            "duur_minuten": rij[7],
            "pantheon": json.loads(rij[8]) if rij[8] else [],
        }
    except Exception:
        return None


def wis_sessie(gebruiker_id, sessie_id):
    """Verwijdert één gearchiveerde sessie."""
    conn = _krijg_verbinding()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM sessies WHERE gebruiker_id = ? AND id = ?",
        (gebruiker_id, sessie_id)
    )
    conn.commit()
    conn.close()


def wis_alle_sessies(gebruiker_id):
    """Verwijdert alle gearchiveerde sessies van een gebruiker."""
    conn = _krijg_verbinding()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessies WHERE gebruiker_id = ?", (gebruiker_id,))
    conn.commit()
    conn.close()

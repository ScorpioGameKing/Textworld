INIT_TILE = """
CREATE TABLE IF NOT EXISTS tiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    tile TEXT NOT NULL,
    cid INTEGER NOT NULL
)
"""

INIT_WORLD = """
CREATE TABLE IF NOT EXISTS worlds (
    save_name TEXT PRIMARY KEY,
    world BLOB)
"""

INIT_COLOR = """
    CREATE TABLE IF NOT EXISTS color (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        bbstring TEXT NOT NULL
    )
"""

REPLACE_WORLD = """
    REPLACE INTO worlds (
        save_name,
        world
    ) VALUES (?, ?)
"""

SELECT_ALL_WORLDS = """
    SELCT * FROM worlds
"""

SELECT_SPECIFIC_WORLD = """
    SELECT world FROM worlds WHERE save_name = ?
"""

SELECT_SPECIFIC_TILE = """
    SELECT tiles.tile, colors.bbstring FROM tiles JOIN colors USING (cid) WHERE id = ?
"""
class Tile:
    INIT = """
    CREATE TABLE IF NOT EXISTS tiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        tile TEXT NOT NULL,
        cid INTEGER NOT NULL
    )
    """
    
    SELECT_WITH_COLORS_BY_ID = """
    SELECT tiles.tile, colors.bbstring FROM tiles JOIN colors USING (cid) WHERE id = ?
    """
    
class World:
    
    
    INIT = """
    CREATE TABLE IF NOT EXISTS worlds (
        save_name TEXT PRIMARY KEY,
        world BLOB)
    """
    REPLACE_BY_NAME = """
    REPLACE INTO worlds (
        save_name,
        world
    ) VALUES (?, ?)
    """
    SELECT_ALL = """
    SELECT * FROM worlds
    """

    SELECT_BY_NAME = """
    SELECT world FROM worlds WHERE save_name = ?
    """

class Color:
    INIT = """
    CREATE TABLE IF NOT EXISTS color (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        bbstring TEXT NOT NULL
    )
    """
    
    SELECT_BY_ID = """
    SELECT * FROM colors WHERE cid = ?
    """










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
    INSERT OR REPLACE INTO worlds (
        save_name,
        store_world(world)
    ) VALUES (?, ?);
    """
    SELECT_ALL = """
    SELECT save_name, load_world(world) FROM worlds
    """
    
    SELECT_ALL_NAMES = """
    SELECT save_name FROM worlds
    """

    SELECT_BY_NAME = """
    SELECT load_world(world) FROM worlds WHERE save_name = ?
    """

class Color:
    INIT = """
    CREATE TABLE IF NOT EXISTS colors (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        bbstring TEXT NOT NULL
    )
    """
    
    FILL = """
    INSERT OR IGNORE INTO colors (name, bbstring) VALUES 
    ( "Purple", "553565"),
    ( "Light Blue", "aabbff"),
    ( "Mid Blue", "8895cc"),
    ( "Deep Blue", "667099"),
    ( "Light Yellow", "FFE8A3"),
    ( "Mid Green", "2A4F41"),
    ( "Brown", "693627"),
    ( "Dark Green", "45814C"),
    ( "Gray", "5C8084"),
    ( "White", "FFFFFF"),
    ( "Light Gray", "666666");
    """
    
    SELECT_BY_ID = """
    SELECT * FROM colors WHERE cid = ?
    """










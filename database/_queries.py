class Tile:
    INIT = """
    CREATE TABLE IF NOT EXISTS tiles (
        tile TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        min_noise REAL,
        max_noise REAL,
        cid INTEGER NOT NULL
    )
    """
    
    FILL = """
        INSERT INTO tiles (tile, name, min_noise, max_noise, cid) VALUES 
        ("X", "Background", NULL, NULL, 0),
        ("~", "Water", -1.0, -0.1, 1),
        ("s", "Sand", -0.1, 0.1, 4),
        ("g", "Grass", 0.1, 0.25, 5),
        ("d", "Dirt", 0.25, 0.35, 6),
        ("f", "Forest", 0.35, 0.5, 7),
        ("m", "Mountain", 0.5, 0.75, 8),
        ("w", "Snow", 0.75, 1.0, 9),
        ("p", "Path", NULL, NULL, 10) ON CONFLICT(tile) DO NOTHING
    """
    
    SELECT_WITH_COLORS_BY_TILE = """
    SELECT tiles.tile, colors.bbstring FROM tiles JOIN colors USING (cid) WHERE tile = ?
    """
    
    SELECT_WITH_COLORS_BY_NOISE = """
    SELECT tiles.tile, colors.bbstring FROM tiles JOIN Colors using (cid) WHERE min_noise <= ? AND max_noise > ?
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
        name TEXT NOT NULL UNIQUE,
        bbstring TEXT NOT NULL
    )
    """
    
    FILL = """
    INSERT INTO colors (name, bbstring) VALUES 
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
    ( "Light Gray", "666666") ON CONFLICT(name) DO NOTHING;
    """
    
    SELECT_BY_ID = """
    SELECT * FROM colors WHERE cid = ?
    """










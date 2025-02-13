class Tile:
    INIT = """
    CREATE TABLE IF NOT EXISTS tiles (
        tile TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        min_noise REAL,
        max_noise REAL,
        cid TEXT NOT NULL
    )
    """
    
    FILL = """
        INSERT INTO tiles (tile, name, min_noise, max_noise, cid) VALUES 

        ("~", "Water", -1.0, -0.1, 'Deep Blue'),
        ("s", "Sand", -0.1, 0.1, 'Light Yellow'),
        ("g", "Grass", 0.1, 0.25, 'Mid Green'),
        ("d", "Dirt", 0.25, 0.35, 'Brown'),
        ("f", "Forest", 0.35, 0.5, 'Dark Green'),
        ("m", "Mountain", 0.5, 0.75, 'Light Gray'),
        ("w", "Snow", 0.75, 1.0, 'White'),
        ('X', 'Background', NULL, NULL, 'Purple'),
        ('p', 'Path', NULL, NULL, 'Black') ON CONFLICT(tile) DO NOTHING
    """
    
    SELECT_WITH_COLORS = """
    SELECT tiles.tile, colors.bbstring, tiles.min_noise, tiles.max_noise FROM tiles JOIN colors USING (cid)
    """
    
    SELECT_WITH_COLORS_BY_TILE = """
    SELECT tiles.tile, colors.bbstring FROM tiles JOIN colors USING (cid) WHERE tile = ?
    """
    
    SELECT_WITH_COLORS_BY_NOISE = """
    SELECT tiles.tile, colors.bbstring FROM tiles JOIN colors USING (cid) WHERE min_noise <= ? AND max_noise > ? AND tile != 'X'
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
        cid TEXT PRIMARY KEY,
        bbstring TEXT NOT NULL
    )
    """
    
    FILL = """
    INSERT INTO colors (cid, bbstring) VALUES 
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
    ( "Light Gray", "666666"),
    ( "Black", "000000") ON CONFLICT(cid) DO NOTHING;
    """
    
    SELECT_BY_ID = """
    SELECT * FROM colors WHERE cid = ?
    """










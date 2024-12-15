from time import gmtime, strftime
from numpy import array, interp, random, rint
from opensimplex import OpenSimplex
from db_interface import TileDBInterface

# Temp DB for testing
TILEDBI = TileDBInterface()

# Color Class
class Color():
    def __init__(self, _rgb:str="000000"):
        self.rgb = _rgb
        self.bbstring = f'{self.rgb[0:1]}{self.rgb[2:3]}{self.rgb[4:5]}'

# Tile class
class TextworldTile():
    def __init__(self, _tile:str="X", _color:Color=Color()):
        self.tile = _tile
        self.color = _color
        self.tile_string = f'[color={self.color.bbstring}]{self.tile}[/color]'

    def setColor(self, _rgb:str="000000"):
        self.color = Color(_rgb)
        self.tile_string = f'[color={self.color.bbstring}]{self.tile}[/color]'

# Map class, made up of tiles
class TextworldMap():
    def __init__(self, _cols:int, _rows:int):
        self.cols = _cols
        self.rows = _rows
        self.map_tiles = []

    # Used for generation to finalize a row
    def addTileRow(self, row:list):
        self.map_tiles.append(row)

    # Used to find tiles by x,y coordinates
    def getMapTile(self, x:int, y:int):
        return self.map_tiles[y][x]

# World Generation Class
class TextworldGenerator():
    def __init__(self, seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.seed = seed
        self.height_noise = array([OpenSimplex(self.seed), OpenSimplex(self.seed * 2), OpenSimplex(self.seed * 4), OpenSimplex(self.seed * 8)])

    # Default Map Generation
    def generateMap(self, cols:int, rows:int, map_x:int, map_y:int, *seed:int):
        scale = 0.0625 * 0.5 # Step Scaler
        map = TextworldMap(cols, rows)
        for y in range(rows):
            map_row = []
            for x in range(cols):

                # Generate and save noise by sampling the average value in height fields at 1, 1/2, 1/4, 1/8 weights finally mapping from -1, 1 to 0, 1
                noise_val = interp(
                    (self.height_noise[0].noise2((x + (map_x * cols)) * scale, (y + (map_y * rows)) * scale) +
                    (self.height_noise[1].noise2((x + (map_x * cols)) * scale, (y + (map_y * rows)) * scale * 0.5)) +
                    (self.height_noise[2].noise2((x + (map_x * cols)) * scale, (y + (map_y * rows)) * scale * 0.25)) +
                    (self.height_noise[3].noise2((x + (map_x * cols)) * scale, (y + (map_y * rows)) * scale * 0.125))) / 2,
                     [-1,1], [0,1])

                # Set TileDBI Index
                tile_index = 0
                match noise_val:
                    case val if val >= 0.9: # Snow
                        tile_index = 7
                    case val if 0.9 > noise_val >= 0.75: # Mountains
                        tile_index = 6
                    case val if 0.75 > noise_val >= 0.6: # Forests
                        tile_index = 5
                    case val if 0.6 > noise_val >= 0.55: # Dirt
                        tile_index = 4
                    case val if 0.55 > noise_val >= 0.35: # Grass
                        tile_index = 3
                    case val if .35 > noise_val >= 0.2: # Sand
                        tile_index = 2
                    case val if .2 > noise_val: # Water
                        tile_index = 1
                    case _:
                        tile_index = 0

                # Create and add tile to current map row
                db_tile:tuple = TILEDBI.getTile(tile_index)
                tile_color = Color(db_tile[3])
                new_tile = TextworldTile(db_tile[2], tile_color)
                map_row.append(new_tile)
            map.addTileRow(map_row)

        # Return for use
        return map

# Textworld World Class
class TextworldWorld():
    def __init__(self, _width:int, _height:int, _cols:int, _rows:int, generator:TextworldGenerator, _name:str = f'DEFAULT_NAME {round(random.random() * 1000000, 0)}'):
        self.dimensions = [_width, _height, _width * _cols, _height * _rows, _cols, _rows] # Num of maps Horizontally, Num of maps Vertically, Num of tiles Horizontally, Num of tiles Vertically,
        self.world_maps = []
        self.save_count = 0
        self.world_name = _name
        self.position = [0, 0]
        self.buildWorld(generator, _cols, _rows)

    # Same as maps, we build by row
    def addWorldMapRow(self, map_row:list):
        self.world_maps.append(map_row)

    # Take in a generator to use and create the maps in the world
    def buildWorld(self, generator:TextworldGenerator, cols:int, rows:int):
        for x in range(self.dimensions[0]):
            map_row = []
            for y in range(self.dimensions[1]):
                map = generator.generateMap(cols, rows, x, y)
                map_row.append(map)
            self.addWorldMapRow(map_row)

    def getMap(self, x:int, y:int):
        return self.world_maps[y][x]

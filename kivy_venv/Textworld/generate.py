from time import gmtime, strftime
from numpy import array, interp, rint
from opensimplex import OpenSimplex
from db_interface import TileDBInterface # type: ignore

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

# Map class, made up of tiles
class TextworldMap():
    def __init__(self, _cols:int, _rows:int):
        self.cols = _cols
        self.height = _rows
        self.map_tiles = []
        self.map_string = ""

    # Used for generation to finalize a row
    def addTileRow(self, row:list):
        self.map_tiles.append(row)

    # Used to "Render" updates to the Map String
    def updateMapString(self):
        for y in range(len(self.map_tiles)):
            for x in range(len(self.map_tiles[y])):
                self.map_string += self.map_tiles[y][x].tile_string
            self.map_string += "\n"

    # Used to find tiles by x,y coordinates
    def getMapTile(self, x:int, y:int):
        return self.map_tiles[y][x]

# World Generation Class
class TextworldGenerator():

    def generateMap(self, cols:int, rows:int, seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        map = TextworldMap(cols, rows)
        height_noise = OpenSimplex(seed)
        y_range, x_range = array(range(0, rows)), array(range(0, cols))
        heightmap = height_noise.noise2array(x=x_range, y=y_range)
        for y in range(rows):
            map_row = []
            for x in range(cols):
                db_tile:tuple = TILEDBI.getTile(int(rint(interp(heightmap[y][x],[-1.0, 1.0],[0, len(TILEDBI.tile_db) - 1]))))
                print(db_tile)
                tile_color = Color(db_tile[3])
                new_tile = TextworldTile(db_tile[2], tile_color)
                map_row.append(new_tile)
            map.addTileRow(map_row)
        map.updateMapString()
        return map

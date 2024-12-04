from random import randint, choices
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
    # Used for testing
    def testGen(self, cols:int, rows:int):
        map = TextworldMap(cols, rows)
        for y in range(rows):
            map_row = []
            for x in range(cols):
                db_tile:tuple = TILEDBI.getTile(randint(0, len(TILEDBI.tile_db) - 1))
                if len(db_tile) >= 1:
                    tile_color = Color(db_tile[2])
                    new_tile = TextworldTile(db_tile[1], tile_color)
                    map_row.append(new_tile)
                else:
                    print("It's all gone wrong!")
                    tile_color = Color()
                    new_tile = TextworldTile(")", tile_color)
                    map_row.append(new_tile)
            map.addTileRow(map_row)
        map.updateMapString()
        return map

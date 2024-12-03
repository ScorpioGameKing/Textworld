from random import randint, choices

# Color Class
class Color():
    def __init__(self, _rgb=[hex(0),hex(0),hex(0)]):
        self.rgb = _rgb
        self.bbstring = f'{str(self.rgb[0])[2:]}{str(self.rgb[1])[2:]}{str(self.rgb[2])[2:]}'

# Tile class
class TextworldTile():
    def __init__(self, _tile="X", _color=Color()):
        self.tile = _tile
        self.color = _color
        self.tile_string = f'[color={self.color.bbstring}]{self.tile}[/color]'

# Map class, made up of tiles
class TextworldMap():
    def __init__(self, _cols, _rows):
        self.cols = _cols
        self.height = _rows
        self.map_tiles = []
        self.map_string = ""
    
    def addTileRow(self, row):
        self.map_tiles.append(row)

    def updateMapString(self):
        for y in range(len(self.map_tiles)):
            for x in range(len(self.map_tiles[y])):
                self.map_string += self.map_tiles[y][x].tile_string
            self.map_string += "\n"

    def getMapTile(self, x, y):
        return self.map_tiles[y][x]

class TextworldGenerator():
    def testGen(self, cols, rows):
        map = TextworldMap(cols, rows)
        for y in range(rows):
            map_row = []
            for x in range(cols):
                tile_color = Color([hex(randint(17, 255)), hex(randint(17, 255)), hex(randint(17, 255))])
                new_tile = TextworldTile(choices(
                    ["X", "~", "f", "d", "s", "g", "m", "w"]
                )[0], tile_color)
                map_row.append(new_tile)
            map.addTileRow(map_row)
        map.updateMapString()

        return map

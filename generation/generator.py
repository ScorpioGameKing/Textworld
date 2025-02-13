from time import gmtime, strftime
import numpy as np
from opensimplex import OpenSimplex

from generation.map import TextworldMap
from models import Size, Tile, Coords
from database import TileDatabase

class TextworldGenerator():
    def __init__(self, seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.seed = seed
        self.height_noise = np.array([OpenSimplex(self.seed), OpenSimplex(self.seed * 2), OpenSimplex(self.seed * 4), OpenSimplex(self.seed * 8)])

        

    # Default Map Generation
    def get_chunk(self, size:Size[int], chunk_coords: Coords) -> TextworldMap:
        scale = 0.5 * 0.0625
        chunk = TextworldMap(size)

        
        with TileDatabase() as db:
        
            for y in range(size.height):
                
                for x in range(size.width):
                    noise_val =(self.height_noise[0].noise2((x + (chunk_coords.x * size.width)) * scale, (y + (chunk_coords.y * size.height)) * scale) +
                    (self.height_noise[1].noise2((x + (chunk_coords.x * size.width)) * scale, (y + (chunk_coords.y * size.height)) * scale * 0.5)) +
                    (self.height_noise[2].noise2((x + (chunk_coords.x * size.width)) * scale, (y + (chunk_coords.y * size.height)) * scale * 0.25)) +
                    (self.height_noise[3].noise2((x + (chunk_coords.x * size.width)) * scale, (y + (chunk_coords.y * size.height)) * scale * 0.125))) / 2
                    db_tile = db.get_tile_by_noise(noise_val)

                    if not db_tile:
                        db_tile = db.get_tile('X')
                    chunk[x,y] = db_tile

        # Return for use
        return chunk
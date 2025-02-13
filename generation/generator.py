from time import gmtime, strftime
import numpy as np
from opensimplex import OpenSimplex
from noise import snoise3

from generation.map import TextworldMap
from models import Size, Tile, Coords
from database import TileDatabase

class TextworldGenerator():
    
    __seed: int
    
    def __init__(self, seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.__seed = seed % np.random.default_rng(seed).integers(10000, 100000)

        

    # Default Map Generation
    def get_chunk(self, size:Size[int], chunk_coords: Coords) -> TextworldMap:
        scale = (0.5 * 0.0625) / 2
        chunk = TextworldMap(size)

        
        with TileDatabase() as db:
            for y in range(size.height):
                
                noise_y = ((y + (chunk_coords.y * size.height)) * scale) + self.__seed
                for x in range(size.width):
                    noise_val = 0
                    noise_x = ((x + (chunk_coords.x * size.width)) * scale) + self.__seed
                    for z in range(4):
                        noise_val += snoise3(noise_x, noise_y, z + self.__seed) / ( z + 1)
                    
                    db_tile = db.get_tile_by_noise(noise_val / 2)
                    if not db_tile:
                        db_tile = db.get_tile('X')
                    chunk[x,y] = db_tile

        # Return for use
        return chunk
from time import gmtime, strftime
import numpy as np
from noise import snoise2

from generation.map import TextworldMap
from models import Size, Coords
from database import TileDatabase

class TextworldGenerator():

    __db: TileDatabase
    __seed: int
    
    def __init__(self, seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.__seed = seed % (np.random.default_rng(seed % ((32 ** 2)-1)).integers(1000, 10000))


    def __enter__(self):
        self.__db = TileDatabase()
        self.__db.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__db.close()

    # Default Map Generation
    def get_chunk(self, size:Size[int], chunk_coords: Coords) -> TextworldMap:
        scale = (0.5 * 0.0625) / 3
        chunk = TextworldMap(size)

        for y in range(size.height):
            
            noise_y = ((y + (chunk_coords.y * size.height)) * scale)  + self.__seed
            for x in range(size.width):
                noise_val = 0
                noise_x = ((x + (chunk_coords.x * size.width)) * scale) + self.__seed
                for z in range(4):
                    noise_val += snoise2(noise_x, noise_y) / ( z + 1)
                noise_val /= 2
                
                db_tile = self.__db.get_tile_by_noise(noise_val)
                if not db_tile:
                    db_tile = self.__db.get_tile('X')
                chunk[x,y] = db_tile

        # Return for use
        return chunk
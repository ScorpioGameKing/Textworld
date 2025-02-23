import logging
from time import gmtime, strftime
# import numpy as np
# from noise import snoise2

from generation.map import TextworldMap
from models import Size, Coords
from database import TileDatabase
from opensimplex import OpenSimplex
import numpy as np

class TextworldGenerator():

    __db: TileDatabase
    __seed: int
    __noise_generator: OpenSimplex
    
    def __init__(self, seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        # self.__seed = seed % (np.random.default_rng(seed % ((32 ** 2)-1)).integers(1, 10000))
        self.__noise_generator = OpenSimplex(seed)

    def __enter__(self):
        self.__db = TileDatabase()
        self.__db.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__db.close()

    # Default Map Generation
    def get_chunk(self, size:Size[int], chunk_coords: Coords) -> TextworldMap:
        scale = (0.5 * 0.0625)
        chunk = TextworldMap(size)

        for y in range(size.height):
            for x in range(size.width):
                noise_val = 0
                for z in range(4):
                    noise_x = ((x + (chunk_coords.x * size.width)) * scale)
                    noise_y = ((y + (chunk_coords.y * size.height)) * scale)
                    noise_val += self.__noise_generator.noise3(noise_x, noise_y, z)
                noise_val = np.clip(noise_val, -1, 1)
                
                db_tile = self.__db.get_tile_by_noise(noise_val)
                if db_tile == None:
                    db_tile = self.__db.get_tile('X')
                chunk[x,y] = db_tile
                #logging.debug(f"Chunk: {x, y} Tile: {db_tile} Noise: {noise_val}")

        # Return for use
        return chunk
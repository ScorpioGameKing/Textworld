import logging
from time import gmtime, strftime
from engine.generation.map import TextworldMap
from models import Size, Coords
from engine.database import TileDatabase
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
        chunk = TextworldMap(size, position=chunk_coords)

        _w = np.array([((x + (chunk_coords.x * size.width)) * scale) for x in range(size.height)])
        _h = np.array([((y + (chunk_coords.y * size.height)) * scale) for y in range(size.height)])
        
        noise_field = self.__noise_generator.noise2array(_w, _h)

        for y in range(size.height):
            for x in range(size.width):
                noise_val = noise_field[y][x]
                db_tile = self.__db.get_tile_by_noise(noise_val)
                chunk[x,y] = db_tile

        # Return for use
        return chunk
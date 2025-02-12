from time import gmtime, strftime
import numpy as np
from opensimplex import OpenSimplex

from models import Size, Tile, Coords
from database import TileDatabase

class TextworldGenerator():
    def __init__(self, seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.seed = seed
        self.height_noise = np.array([OpenSimplex(self.seed), OpenSimplex(self.seed * 2), OpenSimplex(self.seed * 4), OpenSimplex(self.seed * 8)])

        

    # Default Map Generation
    def get_chunk(self, size:Size[int], chunk_coords: Coords):
        scale = 0.0625 * 0.5 # Step Scaler
        (chunk_x, chunk_y) = (chunk_coords.to_tuple())
        chunk = []
        
        for y in range(size.height):
            map_row = []
            for x in range(size.width):

                # Generate and save noise by sampling the average value in height fields at 1, 1/2, 1/4, 1/8 weights finally mapping from -1, 1 to 0, 1
                noise_val =(self.height_noise[0].noise2((x + (chunk_x * size.width)) * scale, (y + (chunk_y * size.height)) * scale) +
                    (self.height_noise[1].noise2((x + (chunk_x * size.width)) * scale, (y + (chunk_y * size.height)) * scale * 0.5)) +
                    (self.height_noise[2].noise2((x + (chunk_x * size.width)) * scale, (y + (chunk_y * size.height)) * scale * 0.25)) +
                    (self.height_noise[3].noise2((x + (chunk_x * size.width)) * scale, (y + (chunk_y * size.height)) * scale * 0.125))) / 2
                
                with TileDatabase() as db:
                    db_tile = db.get_tile_by_noise(noise_val)
                    
                    if not db_tile:
                        db_tile = db.get_tile('X')

                # Create and add tile to current map row
                
                map_row.append(db_tile)
            chunk.append(map_row)

        # Return for use
        return chunk
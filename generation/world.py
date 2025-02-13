
import logging
from time import gmtime, strftime, sleep
from typing import Callable
from database import TileDatabase
from models.coords import Coords
from models.size import Size
from generation.generator import TextworldGenerator
import numpy as np
import threading
import math

class TextworldWorld():
    __chunks: dict[Coords, np.array] = {}

    _chunk_count: Size[int]
    def __init__(self, chunk_count: Size[int], chunk_size: Size[int], seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.chunk_count = chunk_count
        self.chunk_size = chunk_size
        self.generator = TextworldGenerator(seed)
        self.lock = threading.Lock()
        
    def __generate_chunk(self, coords: Coords):
        logging.debug(f"Thread for Chunk [{coords.x}, {coords.y}] started")
        
        chunk = self.generator.get_chunk(self.chunk_size, coords)
        with self.lock:
            self.__chunks[coords] = chunk
            
        logging.debug(f"Thread for Chunk [{coords.x}, {coords.y}] closing")
        
    
    def generate_map(self, progress_callback: Callable[[],None] = (lambda x:logging.debug(f"Progress: {math.floor(x*100)}%"))):
        half_height = round(self.chunk_count.height / 2) or 1
        half_width = round(self.chunk_count.width / 2) or 1
        
        logging.debug(f'Height values {0-half_height} - {half_height}')
        logging.debug(f'Width values {0 - half_width} - {half_width}')
        
        threads: list[threading.Thread] = []
        for x in range(0 - half_height, half_height ):
            for y in range(0 - half_width, half_width):
                threads.append(
                    threading.Thread(None, self.__generate_chunk, f'Chunk {x} {y}', (Coords(x,y),), daemon=True)
                )
                
        for t in threads:
            t.start()
            
        def progress():
            
            logging.debug("Progress thread started")
            while any([t.is_alive() for t in threads]):
                _progress =  len(self.__chunks.keys()) / self.chunk_count.area()
                progress_callback(_progress)
                sleep(3)

            
        progress_thread = threading.Thread(target=progress, name='progress thread' )
        progress_thread.start()
        progress_thread.join()

    def __getitem__(self, coords: tuple[int,int]) -> np.typing.NDArray:
        return self.__chunks[Coords(*coords)]
    
    def __setitem__(self, _: Coords, __:np.array):
        raise NotImplementedError('TextworldWorld object does not support setting indecies')
            
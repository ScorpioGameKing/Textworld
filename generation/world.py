import logging
from time import gmtime, strftime, sleep
from typing import Callable
from database import TileDatabase
from models.coords import Coords
from models.size import Size
from generation.generator import TextworldGenerator
import pickle, gzip, threading, math, logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)

class TextworldWorld():
    __chunks: dict[Coords, np.array] = {}
    _chunk_count: Size[int]
    __seed: int
    def __init__(self, chunk_count: Size[int], chunk_size: Size[int], seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.chunk_count = chunk_count
        self.chunk_size = chunk_size
        self.lock = threading.Lock()
        self.__seed = seed
        
    def __generate_chunk(self, coords: Coords, generator: TextworldGenerator):
        logging.debug(f"Generation for Chunk [{coords.x}, {coords.y}] started")
        
        chunk = generator.get_chunk(self.chunk_size, coords)
        with self.lock:
            self.__chunks[coords] = chunk
        logging.debug(f"Generation for Chunk [{coords.x}, {coords.y}] finished")
        
    def __generate_chunks(self):
        logging.debug('Chunk generation started')
        
        with TextworldGenerator(self.__seed) as generator:
            half_height = self.chunk_count.height // 2
            half_width =  self.chunk_count.width // 2
            
            
            logging.debug(f'Height values {0 - half_height} , {half_height}')
            logging.debug(f'Width values {0 - half_width} , {half_width}')
            logging.debug(f'Chunk area {self.chunk_count.area()}')
            for x in range(0-half_height, half_height if half_height != 0 else 1 ):
                for y in range(0-half_width, half_width if half_width != 0 else 1):
                    self.__generate_chunk(Coords(x,y), generator)
                
        logging.debug('Chunk generation finished')     
    
    def generate_map(self, progress_callback: Callable[[],None] = (lambda x:logging.debug(f"Progress: {math.floor(x*100)}%"))):

        t = threading.Thread(target=self.__generate_chunks)
        t.start()
        
        def progress():
            
            logging.debug("Progress thread started")
            while t.is_alive():
                sleep(3)
                _progress =  len(self.__chunks.keys()) / self.chunk_count.area()
                progress_callback(_progress)
        
        progress_thread = threading.Thread(target=progress, name='progress thread' )
        progress_thread.start()
        progress_thread.join()

    def save_world(self):
        data = pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL)
        return gzip.compress(data)
        
    def __getitem__(self, coords: tuple[int,int]) -> np.typing.NDArray:
        return self.__chunks[Coords(*coords)]
    
    def __setitem__(self, _: Coords, __:np.array):
        raise NotImplementedError('TextworldWorld object does not support setting indecies')
    
    def __getstate__(self):
        self.lock = None
        return (self.chunk_count, self.chunk_size, self.__chunks)
    
    def __setstate__(self, state):
        (self.chunk_count, self.chunk_size, self.__chunks) = state
        self.lock = threading.Lock()
            
    def __repr__(self) -> str:
        return f'Chunks: {len(self.__chunks.keys())}'
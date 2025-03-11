from time import gmtime, strftime, sleep
from typing import Callable
from models import Coords, Size, Tile
from engine.generation.generator import TextworldGenerator
import pickle, gzip, threading, math, logger
import numpy as np
from engine.entities import Entity
import logger
import os

class TextworldWorld():
    __chunks: dict[Coords, np.array] = {}
    chunk_count: Size[int]
    chunk_size: Size[int]
    __seed: int
    _players: dict[int, Entity]

    def __init__(self, chunk_count: Size[int], chunk_size: Size[int], seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.chunk_count = chunk_count
        self.chunk_size = chunk_size
        self.lock = threading.Lock()
        self.__seed = seed
        self.players = {}
        
    def __generate_chunk(self, coords: Coords, generator: TextworldGenerator):
        logger.debug(f"Generation for Chunk [{coords.x}, {coords.y}] started")
        
        chunk = generator.get_chunk(self.chunk_size, coords)
        with self.lock:
            self.__chunks[coords] = chunk
        logger.debug(f"Generation for Chunk [{coords.x}, {coords.y}] finished")
        
    def __generate_chunks(self):
        logger.debug('Chunk generation started')
        
        with TextworldGenerator(self.__seed) as generator:
            half_height = self.chunk_count.height // 2
            half_width =  self.chunk_count.width // 2
            
            logger.debug(f'Height values {0} , {self.chunk_count.height}')
            logger.debug(f'Width values {0} , {self.chunk_count.width}')
            logger.debug(f'Spawn Coords {half_width} , {half_height}')
            logger.debug(f'Chunk area {self.chunk_count.area()}')
            for y in range(0, self.chunk_count.height):
                for x in range(0, self.chunk_count.width):
                    self.__generate_chunk(Coords(x,y), generator)
                
        logger.debug('Chunk generation finished')     
    
    def generate_map(self, progress_callback: Callable[[],None] = (lambda x:logger.debug(f"Progress: {math.floor(x*100)}%"))):
        logger.debug('Generating map with size {self._chunk_count} and chunk size {self.chunk_size}')
        t = threading.Thread(target=self.__generate_chunks)
        t.start()
        
        def progress():
            
            logger.debug("Progress thread started")
            while t.is_alive():
                sleep(3)
                _progress =  len(self.__chunks.keys()) / self.chunk_count.area()
                progress_callback(_progress)
        
        progress_thread = threading.Thread(target=progress, name='progress thread' )
        progress_thread.start()
        progress_thread.join()

    def dump_chunk(self, coords: tuple[int, int]):
        logger.debug(f"Dumping chunk {coords}")
        try:
            path = './dumps/chunk_{coords.x}_{coords.y}.txt'
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as _d:
                chunk = self[coords.x, coords.y]
                for y in range(chunk.rows):
                    for x in range(chunk.columns):
                        _d.write(f"{chunk[x,y].tile_char}")
                    _d.write("\n")
        except Exception as e:
            logger.error(f"Failed to dump chunk {coords} with error {e}")

    def save_world(self):
        logger.debug(f'Saving world with {len(self.__chunks.keys())} chunks')
        data = pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL)
        return gzip.compress(data)
        
    def __getitem__(self, coords: tuple[int,int]) -> np.typing.NDArray | None:
        try:
            return self.__chunks[Coords(*coords)]
        except:
            return None
    
    def __setitem__(self, _: Coords, __:np.array):
        raise NotImplementedError('TextworldWorld object does not support setting indecies')
    
    def __getstate__(self):
        self.lock = None
        return (self.chunk_count, self.chunk_size, self.__chunks, self.players)
    
    def __setstate__(self, state):
        (self.chunk_count, self.chunk_size, self.__chunks, self.players) = state
        self.lock = threading.Lock()
            
    def __repr__(self) -> str:
        return f'Chunks: {len(self.__chunks.keys())}'
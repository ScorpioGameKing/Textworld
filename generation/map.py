
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
    __db: TileDatabase
    def __init__(self, chunk_count: Size[int], chunk_size: Size[int], seed:int = int(strftime("%Y%m%d%H%M%S", gmtime()))):
        self.chunk_count = chunk_count
        self.chunk_size = chunk_size
        self.generator = TextworldGenerator(seed)
        self.lock = threading.Lock()
        self.__db = TileDatabase()
        
    def __generate_chunk(self, coords: Coords):
        
        chunk = self.generator.get_chunk(self.chunk_size, coords)
        with self.lock:
            self.__chunks[coords] = chunk
    
    def generate_map(self, progress_callback: Callable[[],None] = (lambda x:print(f"Progress: {math.floor(x*100)}%"))):
        half_height = math.ceil(self.chunk_count.height / 2)
        half_width = math.ceil(self.chunk_count.width / 2)
        threads: list[threading.Thread] = []
        for x in range((half_height-1)*-1, half_height ):
            for y in range((half_width-1) * -1, half_width):
                threads.append(
                    threading.Thread(None, self.__generate_chunk, f'Chunk {x} {y}', (Coords(x,y),), daemon=True)
                )
                
        for t in threads:
            t.start()
            
        def progress():
            while any([t.is_alive() for t in threads]):
                _progress =  len(self.__chunks.keys()) / self.chunk_count.area()
                progress_callback(_progress)
                sleep(5)

            
        progress_thread = threading.Thread(target=progress, name='progress thread' )
        progress_thread.start()
        progress_thread.join()

    def __getitem__(self, coords: Coords) -> np.typing.NDArray:
        return self.__chunks.get(coords, None)
    
    def __setitem__(self, _: Coords, __:np.array):
        raise NotImplementedError('TextworldWorld object does not support setting indecies')
            
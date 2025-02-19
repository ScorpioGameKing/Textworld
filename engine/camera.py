from generation import TextworldMap
from models import Coords, Size
import math as m

class TextworldCamera():
    def __init__(self, _view_size:Size, _chunk_size:Size):
        self.resize_viewport(_view_size, _chunk_size)
        self.position = Coords(m.floor(self.chunk_size.width / 2), m.floor(self.chunk_size.height / 2))

    def resize_viewport(self, _view_size:Size, _chunk_size:Size):
        self.viewport_size = _view_size
        self.chunk_size = _chunk_size
        self.viewport_dim_offset = [
            m.floor(0 - (self.viewport_size.width * 0.5)), #left
            m.floor(0 + (self.viewport_size.width * 0.5)), #right
            m.floor(0 - (self.viewport_size.height * 0.5)), #up
            m.floor(0 + (self.viewport_size.height * 0.5))] #down

    def selectViewportArea(self, _position:Coords, main_chunk:TextworldMap, surrounding_8):
        view_string = ""
        world_position = [(self.chunk_size.width * _position.x) + self.position.x, (self.chunk_size.height * _position.y) + self.position.y]
        borders = [(self.viewport_dim_offset[0] + self.position.x), (self.viewport_dim_offset[1] + self.position.x), (self.viewport_dim_offset[2] + self.position.y), (self.viewport_dim_offset[3] + self.position.y)]
        #print(f'chunk pos: {_position} cam pos: {self.position} world pos: {world_position} Borders: {borders}')

        print(f"Chunk: {main_chunk} Max Cols: {main_chunk.columns} Max Rows: {main_chunk.rows} Cam Pos: {self.position} Tile: {main_chunk[self.position.x,self.position.y]}")

        return view_string

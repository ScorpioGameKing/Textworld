from generation import TextworldMap
from models import Coords
import math as m

class TextworldCamera():
    def __init__(self, _view_w, _view_h, _max_cols, _max_rows):
        self.resize_viewport(_view_w, _view_h, _max_cols, _max_rows)
        self.position = Coords(m.floor(self.chunk_dims[0] / 2), m.floor(self.chunk_dims[1] / 2))

    def resize_viewport(self, _view_w, _view_h, _max_cols, _max_rows):
        self.viewport_size = [_view_w, _view_h]
        self.chunk_dims = [_max_cols, _max_rows]
        self.viewport_size = [_view_w, _view_h]
        self.viewport_dim_offset = [
            int(round(0 - (self.viewport_size[0]/2), 0)), #left
            int(round(0 + (self.viewport_size[0]/2), 0)), #right
            int(round(0 - (self.viewport_size[1]/2), 0)), #up
            int(round(0 + (self.viewport_size[1]/2), 0))] #down

    def selectViewportArea(self, _position, main_chunk:TextworldMap, surrounding_8):
        view_string = ""
        world_position = [(self.chunk_dims[0] * _position[0]) + self.position.x, (self.chunk_dims[1] * _position[1]) + self.position.y]
        borders = [(self.viewport_dim_offset[0] + self.position.x), (self.viewport_dim_offset[1] + self.position.x), (self.viewport_dim_offset[2] + self.position.y), (self.viewport_dim_offset[3] + self.position.y)]
        #print(f'chunk pos: {_position} cam pos: {self.position} world pos: {world_position} Borders: {borders}')

        print(f"Chunk: {main_chunk} Cols: {main_chunk.columns} Rows: {main_chunk.rows} Pos: {self.position} Tile: {main_chunk[self.position.x,self.position.y]}")

        return view_string

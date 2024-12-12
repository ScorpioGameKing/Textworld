from numpy import array
from generate import TextworldWorld, TextworldMap, TextworldTile

class TextworldCamera():
    def __init__(self, _view_w, _view_h, _max_cols, _max_rows):
        self.chunk_dims = [_max_cols, _max_rows]
        self.viewport_size = [_view_w, _view_h]
        self.viewport_dim_offset = [
            round(0 - (self.viewport_size[0]/2)), #left
            round(0 + (self.viewport_size[0]/2)), #right
            round(0 - (self.viewport_size[1]/2)), #up
            round(0 + (self.viewport_size[1]/2))] #down

    def selectViewportArea(self, position, main_chunk:TextworldMap, surrounding_8):
        print(position, main_chunk, surrounding_8)

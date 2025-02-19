from generation import TextworldMap
from models import Coords, Size
import math as m

class TextworldCamera():
    def __init__(self, _view_size:Size, _chunk_size:Size) -> None:
        self.resize_viewport(_view_size, _chunk_size)
        self.position = Coords(m.floor(self.chunk_size.width / 2), m.floor(self.chunk_size.height / 2))

    def resize_viewport(self, _view_size:Size, _chunk_size:Size) -> None:
        self.viewport_size = _view_size
        self.chunk_size = _chunk_size
        self.viewport_dim_offset = [
            m.floor(0 - (self.viewport_size.width * 0.5)), #left
            m.floor(0 + (self.viewport_size.width * 0.5)), #right
            m.floor(0 - (self.viewport_size.height * 0.5)), #up
            m.floor(0 + (self.viewport_size.height * 0.5))] #down

    def selectViewportArea(self, chunk_pos:Coords, main_chunk:TextworldMap, surrounding_8) -> str:
        view_string = ""
        world_position = [(self.chunk_size.width *chunk_pos.x) + self.position.x, (self.chunk_size.height *chunk_pos.y) + self.position.y]
        borders = [(self.viewport_dim_offset[0] + self.position.x), (self.viewport_dim_offset[1] + self.position.x), (self.viewport_dim_offset[2] + self.position.y), (self.viewport_dim_offset[3] + self.position.y)]
        #print(f'chunk pos: {_position} cam pos: {self.position} world pos: {world_position} Borders: {borders}')

        #print(f"Borders: {borders} R-L: {borders[1] - borders[0]} B-T: {borders[3] - borders[2]} Max Cols: {main_chunk.columns} Max Rows: {main_chunk.rows} Cam Pos: {self.position} Tile: {main_chunk[self.position.x,self.position.y]}")

        for _y in range(borders[2], borders[3]):
            _row = ""
            for _x in range(borders[0], borders[1]):
                view_string += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"

        return view_string

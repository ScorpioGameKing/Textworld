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

        #print(surrounding_8)
        print(f"Borders: {borders} Cam Pos: {self.position} TM: {borders[2] < 0}")

        # Main & Top
        if borders[2] < 0:
            print("TopMain")
            # None Failsafe
            if surrounding_8[0][1] == None:
                print("Failsafe")
                for _y in range(0, borders[3]):
                    _row = ""
                    for _x in range(borders[0], borders[1]):
                        _row += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
                    view_string += f"{_row}\n"
            else:
                # Top
                for _y in range(self.chunk_size.height + borders[2], self.chunk_size.height):
                    _row = ""
                    for _x in range(borders[0], borders[1]):
                        _row += f"[color=#{surrounding_8[0][1][_x, _y].color}]{surrounding_8[0][1][_x, _y].tile_char}[/color]"
                    view_string += f"{_row}\n"

                # Main
                for _y in range(0, borders[3]):
                    _row = ""
                    for _x in range(borders[0], borders[1]):
                        _row += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
                    view_string += f"{_row}\n"

        # Main & Bottom
        elif borders[3] > self.chunk_size.height:
            print("MainBottom")
            # None Failsafe
            if surrounding_8[2][1] == None:
                print("Failsafe")
                for _y in range(borders[2], self.chunk_size.height):
                    _row = ""
                    for _x in range(borders[0], borders[1]):
                        _row += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
                    view_string += f"{_row}\n"
            else:
                # Main
                for _y in range(borders[2], self.chunk_size.height):
                    _row = ""
                    for _x in range(borders[0], borders[1]):
                        _row += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
                    view_string += f"{_row}\n"

                # Bottom
                for _y in range(0, borders[3] - self.chunk_size.height):
                    _row = ""
                    for _x in range(borders[0], borders[1]):
                        _row += f"[color=#{surrounding_8[2][1][_x, _y].color}]{surrounding_8[2][1][_x, _y].tile_char}[/color]"
                    view_string += f"{_row}\n"

        # Main Chunk
        else:
            print("Main")
            for _y in range(borders[2], borders[3]):
                _row = ""
                for _x in range(borders[0], borders[1]):
                    _row += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
                view_string += f"{_row}\n"
        return view_string

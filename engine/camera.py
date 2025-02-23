from generation import TextworldMap
from models import Coords, Size
import math as m
import logging

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
        borders = [  # MIN | MAX, MIN | MAX
            (self.viewport_dim_offset[0] + self.position.x), (self.viewport_dim_offset[1] + self.position.x),
            (self.viewport_dim_offset[2] + self.position.y), (self.viewport_dim_offset[3] + self.position.y)
            ]

        # Main & Top
        if borders[2] < 0:
            #logging.debug(f"TopMain Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos} Top Range: {self.chunk_size.height + borders[2], self.chunk_size.height} Main Range: {0, borders[3]}")

            # Top
            if surrounding_8[0][1] != None:
                for _y in range(self.chunk_size.height + borders[2], self.chunk_size.height):
                    for _x in range(borders[0], borders[1]):
                        view_string += f"[color=#{surrounding_8[0][1][_x, _y].color}]{surrounding_8[0][1][_x, _y].tile_char}[/color]"

            # Main
            for _y in range(0, borders[3]):
                for _x in range(borders[0], borders[1]):
                    view_string += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"

        # Main & Right
        elif borders[1] > self.chunk_size.width:
            #logging.debug(f"MainRight Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos} Main Range: {borders[0], self.chunk_size.width} Right Range: {0, borders[1] - self.chunk_size.width}")
            
            main_h = []
            right_h = []

            # Main
            for _y in range(borders[2], borders[3]):
                _row = ""
                for _x in range(borders[0], self.chunk_size.width):
                    _row += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
                main_h.append(_row)

            # Right
            if surrounding_8[1][1] != None:
                for _y in range(borders[2], borders[3]):
                    _row = ""
                    for _x in range(0, borders[1] - self.chunk_size.width):
                        _row += f"[color=#{surrounding_8[1][1][_x, _y].color}]{surrounding_8[1][1][_x, _y].tile_char}[/color]"
                    right_h.append(_row)
                
            if len(main_h) == len(right_h):
                for strings in zip(main_h, right_h):
                    view_string += f"{strings[0]}{strings[1]}"
            else:
                for string in main_h:
                    view_string += f"{string}"
        
        # Left & Main
        elif borders[0] < 0:
            #logging.debug(f"MainLeft Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos} Left Range: {self.chunk_size.width + borders[0], self.chunk_size.width} Main Range: {0, borders[1]} ")

            left_h = []
            main_h = []

            # Left
            if surrounding_8[1][0] != None:
                for _y in range(borders[2], borders[3]):
                    _row = ""
                    for _x in range(self.chunk_size.width + borders[0], self.chunk_size.width):
                        _row += f"[color=#{surrounding_8[1][0][_x, _y].color}]{surrounding_8[1][0][_x, _y].tile_char}[/color]"
                    left_h.append(_row)
                
            # Main
            for _y in range(borders[2], borders[3]):
                _row = ""
                for _x in range(0, borders[1]):
                    _row += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
                main_h.append(_row)
            
            if len(main_h) == len(left_h):
                for strings in zip(main_h, left_h):
                    view_string += f"{strings[1]}{strings[0]}"
            else:
                for string in main_h:
                    view_string += f"{string}"


        # Main & Bottom
        elif borders[3] > self.chunk_size.height:
            #logging.debug(f"MainBottom Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos} Main Range: {borders[2], self.chunk_size.height} Bottom Range: {0, borders[3] - self.chunk_size.height}")

            # Main
            for _y in range(borders[2], self.chunk_size.height):
                for _x in range(borders[0], borders[1]):
                    view_string += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"
            
            # Bottom
            if surrounding_8[2][1] != None:
                for _y in range(0, borders[3] - self.chunk_size.height):
                    for _x in range(borders[0], borders[1]):
                        view_string += f"[color=#{surrounding_8[2][1][_x, _y].color}]{surrounding_8[2][1][_x, _y].tile_char}[/color]"

        # Main Only
        else:
            #logging.debug(f"Main Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

            for _y in range(borders[2], borders[3]):
                for _x in range(borders[0], borders[1]):
                    view_string += f"[color=#{main_chunk[_x, _y].color}]{main_chunk[_x, _y].tile_char}[/color]"

        return view_string

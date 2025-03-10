from engine.generation import TextworldMap
from models import Coords, Size
import math as m
import logger

class TextworldCamera():
    def __init__(self, _view_size:Size, _chunk_size:Size) -> None:
        self.resize_viewport(_view_size, _chunk_size)
        self.position = Coords(m.floor(self.chunk_size.width / 2), m.floor(self.chunk_size.height / 2))
        self.log = False

    def set_logging(self, state:bool):
        self.log = state

    def resize_viewport(self, _view_size:Size, _chunk_size:Size) -> None:
        self.viewport_size = _view_size
        self.chunk_size = _chunk_size
        self.viewport_dim_offset = [
            m.floor(0 - (self.viewport_size.width * 0.5)), #left
            m.floor(0 + (self.viewport_size.width * 0.5)), #right
            m.floor(0 - (self.viewport_size.height * 0.5)), #up
            m.floor(0 + (self.viewport_size.height * 0.5))] #down

    def select_viewport_area(self, chunk_pos:Coords, main_chunk:TextworldMap, surrounding_8) -> str:
        view_string = ""
        borders = [  # MIN | MAX, MIN | MAX
            (self.viewport_dim_offset[0] + self.position.x), (self.viewport_dim_offset[1] + self.position.x),
            (self.viewport_dim_offset[2] + self.position.y), (self.viewport_dim_offset[3] + self.position.y)
            ]

        # Top Checks
        if borders[2] < 0:

            # Top Left + Top & Left + Main
            if borders[0] < 0:
                if self.log: logger.debug(f"TopLCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
                if surrounding_8[0][0] != None:
                    for _y in range(abs(borders[2])):
                        for _c in surrounding_8[0][0][slice([self.chunk_size.width + borders[0], self.chunk_size.height + borders[2]], [self.chunk_size.width, self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[0][0].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in surrounding_8[0][1][slice([0, self.chunk_size.height + borders[2]], [borders[1], self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[0][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"
                    for _y in range(borders[3]):
                        for _c in surrounding_8[1][0][slice([self.chunk_size.width + borders[0], 0], [self.chunk_size.width, borders[3]])][_y]:
                            try:
                                view_string += surrounding_8[1][0].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in main_chunk[slice([0, 0], [borders[1], borders[3]])][_y]:
                            try:
                                view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"

            # Top + Top Right & Main + Right
            elif borders[1] > self.chunk_size.width:
                if self.log: logger.debug(f"TopRCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
                if surrounding_8[0][2] != None:
                    for _y in range(abs(borders[2])):
                        for _c in surrounding_8[0][1][slice([borders[0], self.chunk_size.height + borders[2]], [self.chunk_size.width, self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[0][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in surrounding_8[0][2][slice([0, self.chunk_size.height + borders[2]], [borders[1] - self.chunk_size.width, self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[0][2].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"
                    for _y in range(borders[3]):
                        for _c in main_chunk[slice([borders[0], 0], [self.chunk_size.width, borders[3]])][_y]:
                            try:
                                view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in surrounding_8[1][1][slice([0, 0], [borders[1] - self.chunk_size.width, borders[3]])][_y]:
                            try:
                                view_string += surrounding_8[1][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"

            # Top & Main
            else:
                if self.log: logger.debug(f"TopMain Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
                if surrounding_8[0][1] != None:
                    for _r in surrounding_8[0][1][slice([borders[0], self.chunk_size.height + borders[2]], [borders[1], self.chunk_size.height])]:
                        for _c in _r:
                            try:
                                view_string += surrounding_8[0][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"
                for _r in main_chunk[slice([borders[0], 0], [borders[1], borders[3]])]:
                    for _c in _r:
                        try:
                            view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                        except:
                            view_string += _c.get_markdown()
                    view_string += "\n"

        # Bottom Checks
        elif borders[3] > self.chunk_size.height:
            
            # Left + Main & Bottom Left + Bottom
            if borders[0] < 0:
                if self.log: logger.debug(f"BotLCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
                if surrounding_8[2][0] != None:
                    for _y in range(self.chunk_size.height - borders[2]):
                        for _c in surrounding_8[1][0][slice([self.chunk_size.width + borders[0], borders[2]], [self.chunk_size.width, self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[1][0].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in main_chunk[slice([0, borders[2]], [borders[1], self.chunk_size.height])][_y]:
                            try:
                                view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"
                    for _y in range(borders[3] - self.chunk_size.height):
                        for _c in surrounding_8[2][0][slice([self.chunk_size.width + borders[0], 0], [self.chunk_size.width, borders[3] - self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[2][0].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in surrounding_8[2][1][slice([0, 0], [borders[1], borders[3] - self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[2][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"

            # Main + Right & Bottom + Bottom Right
            elif borders[1] > self.chunk_size.width:
                if self.log: logger.debug(f"BotRCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
                if surrounding_8[2][2] != None:
                    for _y in range(self.chunk_size.height - borders[2]):
                        for _c in main_chunk[slice([borders[0], borders[2]], [self.chunk_size.width, self.chunk_size.height])][_y]:
                            try:
                                view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in surrounding_8[1][1][slice([0,borders[2]], [borders[1] - self.chunk_size.width, self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[1][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"
                    for _y in range(borders[3] - self.chunk_size.height):
                        for _c in surrounding_8[2][1][slice([borders[0], 0], [self.chunk_size.width, borders[3] - self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[2][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        for _c in surrounding_8[2][2][slice([0, 0], [borders[1] - self.chunk_size.width, borders[3] - self.chunk_size.height])][_y]:
                            try:
                                view_string += surrounding_8[2][2].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"

            # Main & Bottom
            else:
                if self.log: logger.debug(f"MainBottom Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")                
                for _r in main_chunk[slice([borders[0], borders[2]], [borders[1], self.chunk_size.height])]:
                    for _c in _r:
                        try:
                            view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                        except:
                            view_string += _c.get_markdown()
                    view_string += "\n"
                if surrounding_8[2][1] != None:
                    for _r in surrounding_8[2][1][slice([borders[0], 0], [borders[1], borders[3] - self.chunk_size.height])]:
                        for _c in _r:
                            try:
                                view_string += surrounding_8[2][1].entities.get(_c.position).tile.get_markdown()
                            except:
                                view_string += _c.get_markdown()
                        view_string += "\n"

        # Main & Right
        elif borders[1] > self.chunk_size.width:
            if self.log: logger.debug(f"MainRight Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
            for _y in range(self.viewport_size.height):
                for _c in main_chunk[slice([borders[0] , borders[2]] , [self.chunk_size.width , borders[3]])][_y]:
                    try:
                        view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                    except:
                        view_string += _c.get_markdown()
                if surrounding_8[1][1] != None: 
                    for _c in surrounding_8[1][1][slice([0, borders[2]], [borders[1] - self.chunk_size.width, borders[3]])][_y]:
                        try:
                            view_string += surrounding_8[1][1].entities.get(_c.position).tile.get_markdown()
                        except:
                            view_string += _c.get_markdown()
                view_string += "\n"
        
        # Left & Main
        elif borders[0] < 0:
            if self.log: logger.debug(f"MainLeft Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
            for _y in range(self.viewport_size.height):
                if surrounding_8[1][0] != None: 
                    for _c in surrounding_8[1][0][slice([self.chunk_size.width + borders[0], borders[2]], [self.chunk_size.width, borders[3]])][_y]:
                        try:
                            view_string += surrounding_8[1][0].entities.get(_c.position).tile.get_markdown()
                        except:
                            view_string += _c.get_markdown()
                for _c in main_chunk[slice([0, borders[2]], [borders[1] ,borders[3]])][_y]:
                    try:
                        view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                    except:
                        view_string += _c.get_markdown()
                view_string += "\n"

        # Main Only
        else:
            if self.log: logger.debug(f"Main Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
            for _r in main_chunk[slice([borders[0], borders[2]], [borders[1],borders[3]])]:
                for _c in _r:
                    try:
                        view_string += main_chunk.entities.get(_c.position).tile.get_markdown()
                    except:
                        view_string += _c.get_markdown()
                view_string += "\n"

        return view_string

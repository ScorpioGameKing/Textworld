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

        # Top Checks
        if borders[2] < 0:

            # Top Left + Top & Left + Main
            if borders[0] < 0:
                logging.debug(f"TopLCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

                tl_h, t_h, l_h, m_h = [], [], [], []

                # Top Left
                if surrounding_8[0][0] != None:
                    for _y in range(self.chunk_size.height + borders[2], self.chunk_size.height):
                        _row = ""
                        for _x in range(self.chunk_size.width + borders[0], self.chunk_size.width):
                            _row += surrounding_8[0][0][_x, _y].get_markdown()
                        tl_h.append(_row)
                
                # Top
                if surrounding_8[0][1] != None:
                    for _y in range(self.chunk_size.height + borders[2], self.chunk_size.height):
                        _row = ""
                        for _x in range(0, borders[1]):
                            _row += surrounding_8[0][1][_x, _y].get_markdown()
                        t_h.append(_row)

                # Left
                if surrounding_8[1][0] != None:
                    for _y in range(0, borders[3]):
                        _row = ""
                        for _x in range(self.chunk_size.width + borders[0], self.chunk_size.width):
                            _row += surrounding_8[1][0][_x, _y].get_markdown()
                        l_h.append(_row)
                    
                # Main
                for _y in range(0, borders[3]):
                    _row = ""
                    for _x in range(0, borders[1]):
                        _row += main_chunk[_x, _y].get_markdown()
                    m_h.append(_row)
                
                # Stitching
                if len(tl_h) == len(t_h) and len(l_h) == len(m_h):
                    for strings in zip(tl_h, t_h):
                        view_string += f"{strings[0]}{strings[1]}"
                    for strings in zip(l_h, m_h):
                        view_string += f"{strings[0]}{strings[1]}"
                else:
                    for string in m_h:
                        view_string += f"{string}"

            # Top + Top Right & Main + Right
            elif borders[1] > self.chunk_size.width:
                logging.debug(f"TopRCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

                t_h, tr_h, r_h, m_h = [], [], [], []

                # Top
                if surrounding_8[0][1] != None:
                    for _y in range(self.chunk_size.height + borders[2], self.chunk_size.height):
                        _row = ""
                        for _x in range(borders[0], self.chunk_size.width):
                            _row += surrounding_8[0][1][_x, _y].get_markdown()
                        t_h.append(_row)
                
                # Top Right
                if surrounding_8[0][2] != None:
                    for _y in range(self.chunk_size.height + borders[2], self.chunk_size.height):
                        _row = ""
                        for _x in range(0, borders[1] - self.chunk_size.width):
                            _row += surrounding_8[0][2][_x, _y].get_markdown()
                        tr_h.append(_row)

                # Main
                for _y in range(0, borders[3]):
                    _row = ""
                    for _x in range(borders[0], self.chunk_size.width):
                        _row += main_chunk[_x, _y].get_markdown()
                    m_h.append(_row)
                    
                # Right
                if surrounding_8[1][1] != None:
                    for _y in range(0, borders[3]):
                        _row = ""
                        for _x in range(0, borders[1] - self.chunk_size.width):
                            _row += surrounding_8[1][1][_x, _y].get_markdown()
                        r_h.append(_row)
                
                # Stitching
                if len(t_h) == len(tr_h) and len(m_h) == len(r_h):
                    for strings in zip(t_h, tr_h):
                        view_string += f"{strings[0]}{strings[1]}"
                    for strings in zip(m_h, r_h):
                        view_string += f"{strings[0]}{strings[1]}"
                else:
                    for string in m_h:
                        view_string += f"{string}"
            
            # Top & Main
            else:
                logging.debug(f"TopMain Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

                # Top
                if surrounding_8[0][1] != None:
                    for _y in range(self.chunk_size.height + borders[2], self.chunk_size.height):
                        for _x in range(borders[0], borders[1]):
                            view_string += surrounding_8[0][1][_x, _y].get_markdown()

                # Main
                for _y in range(0, borders[3]):
                    for _x in range(borders[0], borders[1]):
                        view_string += main_chunk[_x, _y].get_markdown()

        # Bottom Checks
        elif borders[3] > self.chunk_size.height:
            
            # Left + Main & Bottom Left + Bottom
            if borders[0] < 0:
                logging.debug(f"BotLCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

                l_h, m_h, bl_h, b_h = [], [], [], []

                # Left
                if surrounding_8[1][0] != None:
                    for _y in range(borders[2], self.chunk_size.height):
                        _row = ""
                        for _x in range(self.chunk_size.width + borders[0], self.chunk_size.width):
                            _row += surrounding_8[1][0][_x, _y].get_markdown()
                        l_h.append(_row)
                
                # Main
                for _y in range(borders[2], self.chunk_size.height):
                    _row = ""
                    for _x in range(0, borders[1]):
                        _row += main_chunk[_x, _y].get_markdown()
                    m_h.append(_row)

                # Bottom Left
                if surrounding_8[2][0] != None:
                    for _y in range(0, borders[3] - self.chunk_size.height):
                        _row = ""
                        for _x in range(self.chunk_size.width + borders[0], self.chunk_size.width):
                            _row += surrounding_8[2][0][_x, _y].get_markdown()
                        bl_h.append(_row)
                    
                # Bottom
                if surrounding_8[2][1] != None:
                    for _y in range(0, borders[3] - self.chunk_size.height):
                        _row = ""
                        for _x in range(0, borders[1]):
                            _row += surrounding_8[2][1][_x, _y].get_markdown()
                        b_h.append(_row)
                
                if len(l_h) == len(m_h) and len(bl_h) == len(b_h):
                    for strings in zip(l_h, m_h):
                        view_string += f"{strings[0]}{strings[1]}"
                    for strings in zip(bl_h, b_h):
                        view_string += f"{strings[0]}{strings[1]}"
                else:
                    for string in m_h:
                        view_string += f"{string}"

            # Main + Right & Bottom + Bottom Right
            elif borders[1] > self.chunk_size.width:
                logging.debug(f"BotRCorner Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

                m_h, r_h, b_h, br_h = [], [], [], []

                # Main
                for _y in range(borders[2], self.chunk_size.height):
                    _row = ""
                    for _x in range(borders[0], self.chunk_size.width):
                        _row += main_chunk[_x, _y].get_markdown()
                    m_h.append(_row)
                
                # Right
                if surrounding_8[0][1] != None:
                    for _y in range(borders[2], self.chunk_size.height):
                        _row = ""
                        for _x in range(0, borders[1] - self.chunk_size.width):
                            _row += surrounding_8[0][1][_x, _y].get_markdown()
                        r_h.append(_row)

                # Bottom
                if surrounding_8[2][1] != None:
                    for _y in range(0, borders[3] - self.chunk_size.height):
                        _row = ""
                        for _x in range(borders[0], self.chunk_size.width):
                            _row += surrounding_8[2][1][_x, _y].get_markdown()
                        b_h.append(_row)
                    
                # Bottom Right
                if surrounding_8[2][2] != None:
                    for _y in range(0, borders[3] - self.chunk_size.height):
                        _row = ""
                        for _x in range(0, borders[1] - self.chunk_size.width):
                            _row += surrounding_8[2][2][_x, _y].get_markdown()
                        br_h.append(_row)
                
                # Stitching
                if len(m_h) == len(r_h) and len(b_h) == len(br_h):
                    for strings in zip(m_h, r_h):
                        view_string += f"{strings[0]}{strings[1]}"
                    for strings in zip(b_h, br_h):
                        view_string += f"{strings[0]}{strings[1]}"
                else:
                    for string in m_h:
                        view_string += f"{string}"
            

            # Main & Bottom
            else:
                logging.debug(f"MainBottom Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

                # Main
                for _y in range(borders[2], self.chunk_size.height):
                    for _x in range(borders[0], borders[1]):
                        view_string += main_chunk[_x, _y].get_markdown()
                
                # Bottom
                if surrounding_8[2][1] != None:
                    for _y in range(0, borders[3] - self.chunk_size.height):
                        for _x in range(borders[0], borders[1]):
                            view_string += surrounding_8[2][1][_x, _y].get_markdown()

        # Main & Right
        elif borders[1] > self.chunk_size.width:
            logging.debug(f"MainRight Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
            
            main_h, right_h = [], []

            # Main
            for _y in range(borders[2], borders[3]):
                _row = ""
                for _x in range(borders[0], self.chunk_size.width):
                    _row += main_chunk[_x, _y].get_markdown()
                main_h.append(_row)

            # Right
            if surrounding_8[1][1] != None:
                for _y in range(borders[2], borders[3]):
                    _row = ""
                    for _x in range(0, borders[1] - self.chunk_size.width):
                        _row += surrounding_8[1][1][_x, _y].get_markdown()
                    right_h.append(_row)

            # Stitching  
            if len(main_h) == len(right_h):
                for strings in zip(main_h, right_h):
                    view_string += f"{strings[0]}{strings[1]}"
            else:
                for string in main_h:
                    view_string += f"{string}"
        
        # Left & Main
        elif borders[0] < 0:
            logging.debug(f"MainLeft Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")

            left_h, main_h = [], []

            # Left
            if surrounding_8[1][0] != None:
                for _y in range(borders[2], borders[3]):
                    _row = ""
                    for _x in range(self.chunk_size.width + borders[0], self.chunk_size.width):
                        _row += surrounding_8[1][0][_x, _y].get_markdown()
                    left_h.append(_row)
                
            # Main
            for _y in range(borders[2], borders[3]):
                _row = ""
                for _x in range(0, borders[1]):
                    _row += main_chunk[_x, _y].get_markdown()
                main_h.append(_row)
            
            # Stitching
            if len(left_h) == len(main_h):
                for strings in zip(left_h, main_h):
                    view_string += f"{strings[0]}{strings[1]}"
            else:
                for string in main_h:
                    view_string += f"{string}"

        # Main Only
        else:
            logging.debug(f"Main Borders: {borders} Cam Pos: {self.position} Chunk Pos: {chunk_pos}")
            for _y in range(borders[2], borders[3]):
                for _x in range(borders[0], borders[1]):
                    view_string += main_chunk[_x, _y].get_markdown()

        return view_string

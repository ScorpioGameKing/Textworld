from numpy import array
from generate import TextworldWorld, TextworldMap, TextworldTile

class TextworldCamera():
    def __init__(self, _view_w, _view_h, _max_cols, _max_rows):
        self.resize_viewport(_view_w, _view_h, _max_cols, _max_rows)
        self.position = [int(round(self.chunk_dims[0] / 2, 0)), int(round(self.chunk_dims[1] / 2, 0))]

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
        world_position = [(self.chunk_dims[0] * _position[0]) + self.position[0], (self.chunk_dims[1] * _position[1]) + self.position[1]]
        borders = [(self.viewport_dim_offset[0] + self.position[0]), (self.viewport_dim_offset[1] + self.position[0]), (self.viewport_dim_offset[2] + self.position[1]), (self.viewport_dim_offset[3] + self.position[1])]
        #print(f'chunk pos: {_position} cam pos: {self.position} world pos: {world_position} Borders: {borders}')

        #[[TL, T], [L, M]]
        if borders[2] < 0:
            if borders[0] < 0:
                view_string += '[[TL, T], [L, M]]'

            elif borders[1] > main_chunk.cols - 1:
                view_string = "[[T, TR], [M, R]]"

            # Top Middle
            else:
                mid_view = []
                top_view = []
                for mid_row_slice in main_chunk.map_tiles[0:borders[3]]:
                    mid_row = ""
                    for tile in mid_row_slice[borders[0]:borders[1]]:
                        mid_row += tile.tile_string
                    mid_view.append(mid_row)
                if surrounding_8[0][1] != None:
                    for top_row_slice in surrounding_8[0][1].map_tiles[(self.chunk_dims[1] - 1) + borders[2]:(self.chunk_dims[1] - 1)]:
                        top_row = ""
                        for tile in top_row_slice[borders[0]:borders[1]]:
                            top_row += tile.tile_string
                        top_view.append(top_row)
                for row in mid_view:
                    top_view.append(row)
                for row in top_view:
                    view_string += f'{row}\n'

        elif borders[3] > main_chunk.rows - 1:
            if borders[0] < 0:
                view_string = "[[L, M], [BL, B]]"

            elif borders[1] > main_chunk.cols - 1:
                view_string = "[[M, R], [B, BR]]"

            # Middle Bottom
            else:
                mid_view = []
                bottom_view = []
                for mid_row_slice in main_chunk.map_tiles[borders[2]:self.chunk_dims[1]]:
                    mid_row = ""
                    for tile in mid_row_slice[borders[0]:borders[1]]:
                        mid_row += tile.tile_string
                    mid_view.append(mid_row)
                if surrounding_8[2][1] != None:
                    for bottom_row_slice in surrounding_8[2][1].map_tiles[0:self.viewport_size[1] - (self.chunk_dims[1] - borders[2])]:
                        bot_row = ""
                        for tile in bottom_row_slice[borders[0]:borders[1]]:
                            bot_row += tile.tile_string
                        bottom_view.append(bot_row)
                    for row in bottom_view:
                        mid_view.append(row)
                for row in mid_view:
                    view_string += f'{row}\n'


        # Left Chunk
        elif borders[0] < 0:
            mid_view = []
            left_view = []
            for mid_row_slice in main_chunk.map_tiles[borders[2]:borders[3]]:
                mid_row = ""
                for tile in mid_row_slice[0:borders[1]]:
                    mid_row += tile.tile_string
                mid_view.append(mid_row)
            if surrounding_8[1][0] != None:
                for left_row_slice in surrounding_8[1][0].map_tiles[borders[2]:borders[3]]:
                    left_row = ""
                    for tile in left_row_slice[(self.chunk_dims[0]) + (self.viewport_dim_offset[0] + self.position[0]):(self.chunk_dims[0])]:
                        left_row += tile.tile_string
                    left_view.append(left_row)
                for row in range(self.viewport_size[1] - 1):
                    view_string += f'{left_view[row]}{mid_view[row]}\n'
            else:
                for row in mid_view:
                    view_string += f'{row}\n'

        # Right Chunk
        elif borders[1] > main_chunk.cols - 1:
            mid_view = []
            right_view = []
            for mid_row_slice in main_chunk.map_tiles[borders[2]:borders[3]]:
                mid_row = ""
                for tile in mid_row_slice[borders[0]:borders[1]]:
                    mid_row += tile.tile_string
                mid_view.append(mid_row)
            if surrounding_8[1][1] != None:
                for right_row_slice in surrounding_8[1][1].map_tiles[borders[2]:borders[3]]:
                    right_row = ""
                    for tile in right_row_slice[0:self.viewport_size[0] - (self.chunk_dims[0] - borders[0])]:
                        right_row += tile.tile_string
                    right_view.append(right_row)
                for row in range(self.viewport_size[1] - 1):
                    view_string += f'{mid_view[row]}{right_view[row]}\n'
            else:
                for row in mid_view:
                    view_string += f'{row}\n'

        # Main Chunk
        else:
            for row_slice in main_chunk.map_tiles[borders[2]:borders[3]]:
                for tile in row_slice[borders[0]:borders[1]]:
                    view_string += tile.tile_string
                view_string += '\n'
        return view_string

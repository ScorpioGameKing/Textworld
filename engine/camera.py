from generation import TextworldMap

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

    def selectViewportArea(self, _position, main_chunk, surrounding_8):
        view_string = ""
        world_position = [(self.chunk_dims[0] * _position[0]) + self.position[0], (self.chunk_dims[1] * _position[1]) + self.position[1]]
        borders = [(self.viewport_dim_offset[0] + self.position[0]), (self.viewport_dim_offset[1] + self.position[0]), (self.viewport_dim_offset[2] + self.position[1]), (self.viewport_dim_offset[3] + self.position[1])]
        #print(f'chunk pos: {_position} cam pos: {self.position} world pos: {world_position} Borders: {borders}')

        print(main_chunk[1,1])

        return view_string

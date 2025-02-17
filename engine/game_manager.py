from kivy.uix.widget import Widget
from kivy.core.window import Window, Keyboard
from generation import TextworldGenerator, TextworldMap, TextworldWorld
from engine.camera import TextworldCamera

# Management system. This is the center for most data, Map, World, Active NPC lists, etc
class TextworldGameManagementSystem(Widget):
    # Using Super and Class type Widget to hack in Keyboard Support
    def __init__(self, **kwargs):
        super(TextworldGameManagementSystem, self).__init__(**kwargs)
        self._keyboard:Keyboard
        self.get_focus()
        self.world_position = [0,0]
        self.chunk_position = [75, 75]

    def get_focus(self):
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

    # Clear out keyboard bindings, doesn't like being forced to none but it's fine for now
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None #type: ignore

    # Determin input and if movement is possible for temp camera
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        # keycode is a tuple (integer, string)
        #print(keycode[1])
        match keycode[1]:
            case 'left':
                pass
            case 'right':
                pass
            case 'up':
                pass
            case 'down':
                pass
        return True

    # Does nothing at the moment
    def _on_key_up(self, keyboard, keycode):
        return True

    def buildCamera(self, _view_w=106, _view_h=25, _max_cols=150, _max_rows=150):
        self.camera = TextworldCamera(_view_w, _view_h, _max_cols, _max_rows)

    # Takes an overload of either an existing world or the settings to create a world
    def loadWorld(self, *world):
        if len(world) == 1:
            self.active_world = world[0]
            self.setMap(self.world_position[0], self.world_position[1])
        else:
            self.active_world = TextworldWorld(world[0][0], world[0][1], world[0][2], world[0][3], world[1], world[0][7])
            self.setMap(world[0][4], world[0][5])

    # Set the active World Map, Default gens new map
    def setMap(self, map_x:int, map_y:int):
        self.active_map = self.active_world[map_x, map_y]

    # Get a World Map, none if oob
    def getMap(self, map_x:int, map_y:int) -> TextworldMap | None:
        if map_x < 0 or map_x > self.active_world.chunk_size.width - 1 or map_y < 0 or map_y > self.active_world.chunk_size.height - 1:
            return None
        else:
            return self.active_world[map_x, map_y]
        
    # Display Render Loop
    def update_display(self, display, command_input, dt):
        view_text = self.camera.selectViewportArea(
            self.world_position, # Position
            self.active_map, # Center Chunk Seperated for faster viewport
            [ # Surrounding 8 list, Only look at those in the veiwport based on how it overflows the main chunk
            [self.getMap(self.world_position[0] - 1, self.world_position[1] - 1), # Top Left
            self.getMap(self.world_position[0]    , self.world_position[1] - 1), # Top
            self.getMap(self.world_position[0] + 1, self.world_position[1] - 1)], # Top Left
            [self.getMap(self.world_position[0] - 1, self.world_position[1]    ), # Left
            self.getMap(self.world_position[0] + 1, self.world_position[1]    )], # Right
            [self.getMap(self.world_position[0] - 1, self.world_position[1] + 1), # Bottom Left
            self.getMap(self.world_position[0]    , self.world_position[1] + 1), # Bottom
            self.getMap(self.world_position[0] + 1, self.world_position[1] + 1)], # Bottom Right
        ])
        display.update_text(view_text)
        if command_input.typing:
            pass
        else:
            self.get_focus()
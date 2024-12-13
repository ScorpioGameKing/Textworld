from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Keyboard, Window
from kivy.uix.widget import Widget
from Textworld.camera import TextworldCamera
from game_ui import TextworldGameLayout
from generate import TextworldGenerator, TextworldWorld
from db_interface import TileDBInterface

# Management system. This is the center for most data, Map, World, Active NPC lists, etc
class TextworldGameManagementSystem(Widget):
    # Using Super and Class type Widget to hack in Keyboard Support
    def __init__(self, _width:int, _height:int, _cols:int, _rows:int, spawn_x:int, spawn_y:int, *seed:int, **kwargs):
        super(TextworldGameManagementSystem, self).__init__(**kwargs)
        self._keyboard:Keyboard
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        # Check if a custom generator was given, will be given during world settings step later
        if len(seed) == 1:
            self.world_generator = TextworldGenerator(seed[0])
        else:
            self.world_generator = TextworldGenerator()
        # Load or Create a world, set inital map position and active map
        self.loadWorld(_width, _height, _cols, _rows)
        self.world_position = [spawn_x, spawn_y]
        self.setActiveMap(self.world_position[0], self.world_position[1])

    # Clear out keyboard bindings, doesn't like being forced to none but it's fine for now
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None #type: ignore

    # Determin input and if movement is possible for temp camera
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        # keycode is a tuple (integer, string)
        match keycode[1]:
            case 'left':
                match self.world_position[0]:
                    case x if x - 1 < 0:
                        #self.world_position[0] = 0
                        self.camera.position[0] -= 1
                    case _:
                        #self.world_position[0] -= 1
                        self.camera.position[0] -= 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
            case 'right':
                match self.world_position[0]:
                    case x if x + 1 > self.active_world.dimensions[0] - 1:
                        #self.world_position[0] = self.world_position[0]
                        self.camera.position[0] += 1
                    case _:
                        #self.world_position[0] += 1
                        self.camera.position[0] += 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
            case 'up':
                match self.world_position[1]:
                    case y if y - 1 < 0:
                        #self.world_position[1] = 0
                        self.camera.position[1] -= 1
                    case _:
                        #self.world_position[1] -= 1
                        self.camera.position[1] -= 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
            case 'down':
                match self.world_position[1]:
                    case y if y + 1 > self.active_world.dimensions[1] - 1:
                        #self.world_position[1] = self.world_position[1]
                        self.camera.position[1] += 1
                    case _:
                        #self.world_position[1] += 1
                        self.camera.position[1] += 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
        return True

    # Does nothing at the moment
    def _on_key_up(self, keyboard, keycode):
        return True

    def buildCamera(self, _view_w, _view_h, _max_cols, _max_rows):
        self.camera = TextworldCamera(_view_w, _view_h, _max_cols, _max_rows)

    # Takes an overload of either an existing world or the settings to create a world
    def loadWorld(self, *world):
        if len(world) == 1:
            self.active_world = world[0]
        else:
            self.active_world = TextworldWorld(world[0], world[1], world[2], world[3], self.world_generator)

    # Set the active World Map, Default gens new map
    def setActiveMap(self, map_x:int, map_y:int):
        self.active_map = self.active_world.world_maps[map_x][map_y]

    # Set the active World Map, Default gens new map
    def getActiveMap(self, map_x:int, map_y:int):
        if map_x < 0 or map_x > self.active_world.dimensions[0] - 1 or map_y < 0 or map_y > self.active_world.dimensions[1] - 1:
            return None
        else:
            return self.active_world.world_maps[map_x][map_y]

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(App):
    # This Runs everything
    def build(self):
        # Window Defaults
        Window.size = (1438,720)
        # Default Settings
        self._defaults = [5, 5, 106, 25, 1, 1, 42069]
        # Init UI and Management System
        self.game = TextworldGameLayout()
        self.management_system = TextworldGameManagementSystem(
            self._defaults[0], # World Width
            self._defaults[1], # World Height
            self._defaults[2], # Characters in map row
            self._defaults[3], # Number of map rows
            self._defaults[4], # Spawn Map X
            self._defaults[5], # Spawn Map Y
            self._defaults[6]) # Generation Seed
        # Schedule Display Render Call
        Clock.schedule_interval(self.update_display, 1/30)
        self.management_system.buildCamera(20, 20, self._defaults[2], self._defaults[3])
        # Return App to be run
        return self.game
    # Display Render Loop
    def update_display(self, dt):
        self.game.left_panel.display.update_text(self.management_system.active_map.map_string)
        self.management_system.camera.selectViewportArea(
            self.management_system.world_position, # Position
            self.management_system.active_map, # Center Chunk Seperated for faster viewport
            [ # Surrounding 8 list, Only look at those in the veiwport based on how it overflows the main chunk
            self.management_system.getActiveMap(self.management_system.world_position[0] - 1, self.management_system.world_position[1] - 1), # Top Left
            self.management_system.getActiveMap(self.management_system.world_position[0]    , self.management_system.world_position[1] - 1), # Top
            self.management_system.getActiveMap(self.management_system.world_position[0] + 1, self.management_system.world_position[1] - 1), # Top Left
            self.management_system.getActiveMap(self.management_system.world_position[0] - 1, self.management_system.world_position[1]    ), # Left
            self.management_system.getActiveMap(self.management_system.world_position[0] + 1, self.management_system.world_position[1]    ), # Right
            self.management_system.getActiveMap(self.management_system.world_position[0] - 1, self.management_system.world_position[1] + 1), # Bottom Left
            self.management_system.getActiveMap(self.management_system.world_position[0]    , self.management_system.world_position[1] + 1), # Bottom
            self.management_system.getActiveMap(self.management_system.world_position[0] + 1, self.management_system.world_position[1] + 1), # Bottom Right
        ])

# Config Write settings to be moved
if __name__ == '__main__':
    TextworldApp().run()

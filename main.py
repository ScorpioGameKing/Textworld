from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Keyboard, Window
from kivy.uix.widget import Widget
from time import gmtime, strftime
from datetime import timedelta
from timeit import timeit, default_timer
from camera import TextworldCamera
from game_ui import TextworldGameLayout
from generate import TextworldGenerator, TextworldMap, TextworldWorld
from database import WorldDatabase, Database
from database import Color, World, Tile


class Timer:
    """Measure time used."""
    # Ref: https://stackoverflow.com/a/57931660/

    def __init__(self, round_ndigits: int = 0):
        self._round_ndigits = round_ndigits
        self._start_time = default_timer()

    def __call__(self) -> float:
        return default_timer() - self._start_time

    def __str__(self) -> str:
        return str(timedelta(seconds=round(self(), self._round_ndigits)))

# Management system. This is the center for most data, Map, World, Active NPC lists, etc
class TextworldGameManagementSystem(Widget):

    # Using Super and Class type Widget to hack in Keyboard Support
    def __init__(self, *seed:int, **kwargs):
        super(TextworldGameManagementSystem, self).__init__(**kwargs)
        self._keyboard:Keyboard
        self.get_focus()

        # Temp DBI Interfaces
        self.save_system = WorldDatabase()
        self.save_system.open()

        # Check if a custom generator was given, will be given during world settings step later
        if len(seed) == 1:
            self.world_generator = TextworldGenerator(seed[0])
        else:
            self.world_generator = TextworldGenerator()

        # Load or Create a world, set inital map position and active map
        self.world_position = [0,0]
        
    def __del__(self):
        self.save_system.close()

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
                match self.camera.position[0]:
                    case x if x - 1 < 0 :
                        match self.world_position[0]:
                            case x if x - 1 < 0:
                                self.world_position[0] = self.world_position[0]
                                self.active_world.position[0] = self.active_world.position[0]
                                self.camera.position[0] = self.camera.position[0]
                            case _:
                                self.world_position[0] -= 1
                                self.active_world.position[0] -= 1
                                self.camera.position[0] = self.active_world.dimensions[4] - 1
                    case _:
                        self.camera.position[0] -= 1
                self.setMap(self.world_position[0], self.world_position[1])
                if self.getMap(self.world_position[0], self.world_position[1]):
                    #self.getMap(self.world_position[0], self.world_position[1]).getMapTile(self.camera.position[0] ,self.camera.position[1]).setColor("FFFFFF")
                    pass
            case 'right':
                match self.camera.position[0]:
                    case x if x + 1 > self.camera.chunk_dims[0] - 1:
                        match self.world_position[0]:
                            case x if x + 1 > self.active_world.dimensions[0] - 1:
                                self.world_position[0] = self.world_position[0]
                                self.active_world.position[0] = self.active_world.position[0]
                                self.camera.position[0] = self.camera.position[0]
                            case _:
                                self.world_position[0] += 1
                                self.active_world.position[0] += 1
                                self.camera.position[0] = 0
                    case _:
                        self.camera.position[0] += 1
                self.setMap(self.world_position[0], self.world_position[1])
                if self.getMap(self.world_position[0], self.world_position[1]):
                    #self.getMap(self.world_position[0], self.world_position[1]).getMapTile(self.camera.position[0] ,self.camera.position[1]).setColor("FFFFFF")
                    pass
            case 'up':
                match self.camera.position[1]:
                    case y if y - 1 < 0:
                        match self.world_position[1]:
                            case y if y - 1 < 0:
                                self.world_position[1] = self.world_position[1]
                                self.active_world.position[1] = self.active_world.position[1]
                                self.camera.position[1] = self.camera.position[1]
                            case _:
                                self.world_position[1] -= 1
                                self.active_world.position[1] -= 1
                                self.camera.position[1] = self.active_world.dimensions[5] - 1
                    case _:
                        self.camera.position[1] -= 1
                self.setMap(self.world_position[0], self.world_position[1])
                if self.getMap(self.world_position[0], self.world_position[1]):
                    #self.getMap(self.world_position[0], self.world_position[1]).getMapTile(self.camera.position[0] ,self.camera.position[1]).setColor("FFFFFF")
                    pass
            case 'down':
                match self.camera.position[1]:
                    case y if y + 1 > self.camera.chunk_dims[1] - 1:
                        match self.world_position[1]:
                            case y if y + 1 > self.active_world.dimensions[1] - 1:
                                self.world_position[1] = self.world_position[1]
                                self.active_world.position[1] = self.active_world.position[1]
                                self.camera.position[1] = self.camera.position[1]
                            case _:
                                self.world_position[1] += 1
                                self.active_world.position[1] += 1
                                self.camera.position[1] = 0
                    case _:
                        self.camera.position[1] += 1
                self.setMap(self.world_position[0], self.world_position[1])
                if self.getMap(self.world_position[0], self.world_position[1]):
                    #self.getMap(self.world_position[0], self.world_position[1]).getMapTile(self.camera.position[0] ,self.camera.position[1]).setColor("FFFFFF")
                    pass
        return True

    # Does nothing at the moment
    def _on_key_up(self, keyboard, keycode):
        return True

    def buildCamera(self, _view_w, _view_h, _max_cols, _max_rows):
        self.camera = TextworldCamera(_view_w, _view_h, _max_cols, _max_rows)

    # Takes an overload of either an existing world or the settings to create a world
    def loadWorld(self, *world):
        load_time = Timer()
        start = load_time()
        print(f'Loading: {start}')
        if len(world) == 1:
            self.active_world = world[0]
            self.setMap(self.active_world.position[0], self.active_world.position[1])
        else:
            self.active_world = TextworldWorld(world[0][0], world[0][1], world[0][2], world[0][3], world[1], world[0][7])
            self.setMap(world[0][4], world[0][5])
        end = load_time()
        print(f'Load Time: {end - start}')

    # Set the active World Map, Default gens new map
    def setMap(self, map_x:int, map_y:int):
        self.active_map = self.active_world.world_maps[map_x][map_y]

    # Get a World Map, none if oob
    def getMap(self, map_x:int, map_y:int) -> TextworldMap | None:
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
        self._defaults = [4, 4, 150, 150, 2, 2, 42069, "Testing World 2"]

        # Init UI and Management System
        self.game = TextworldGameLayout()
        self.management_system = TextworldGameManagementSystem(self._defaults[6])

        load_world = self.management_system.save_system.load_world_from_db("Testing Save 1")
        if not load_world:
            return self.game
        self.management_system.loadWorld(load_world)
        #self.management_system.loadWorld(self._defaults,self.management_system.world_generator)

        # Schedule Display Render Call
        Clock.schedule_interval(self.update_display, 1/30)
        self.management_system.buildCamera(106, 25, self._defaults[2], self._defaults[3])

        save_time = Timer()
        start = save_time()
        print(f'Saving: {start}')
        #self.management_system.save_system.saveWorldToDB(self.management_system.active_world, "Testing Save 1")
        end = save_time()
        print(f'Done: {end - start}')


        # Return App to be run
        return self.game

    # Display Render Loop
    def update_display(self, dt):
        view_text = self.management_system.camera.selectViewportArea(
            self.management_system.world_position, # Position
            self.management_system.active_map, # Center Chunk Seperated for faster viewport
            [ # Surrounding 8 list, Only look at those in the veiwport based on how it overflows the main chunk
            [self.management_system.getMap(self.management_system.world_position[0] - 1, self.management_system.world_position[1] - 1), # Top Left
            self.management_system.getMap(self.management_system.world_position[0]    , self.management_system.world_position[1] - 1), # Top
            self.management_system.getMap(self.management_system.world_position[0] + 1, self.management_system.world_position[1] - 1)], # Top Left
            [self.management_system.getMap(self.management_system.world_position[0] - 1, self.management_system.world_position[1]    ), # Left
            self.management_system.getMap(self.management_system.world_position[0] + 1, self.management_system.world_position[1]    )], # Right
            [self.management_system.getMap(self.management_system.world_position[0] - 1, self.management_system.world_position[1] + 1), # Bottom Left
            self.management_system.getMap(self.management_system.world_position[0]    , self.management_system.world_position[1] + 1), # Bottom
            self.management_system.getMap(self.management_system.world_position[0] + 1, self.management_system.world_position[1] + 1)], # Bottom Right
        ])
        self.game.left_panel.display.update_text(view_text)
        if self.game.left_panel.command_input.typing:
            pass
        else:
            self.management_system.get_focus()

# Config Write settings to be moved
if __name__ == '__main__':
    with Database() as db:
        db.init_db(Color.INIT, Color.FILL, Tile.INIT, World.INIT)
    TextworldApp().run()

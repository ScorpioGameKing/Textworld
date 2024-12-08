from kivy.app import App
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Keyboard, Window
from kivy.uix.widget import Widget
from generate import TextworldGenerator, TextworldMap, TextworldWorld # type: ignore
from db_interface import TileDBInterface # type: ignore

# Container for Display, Terminal and Input
class TextworldLeftLayout(BoxLayout):
    display = ObjectProperty(None)
    command_terminal = ObjectProperty(None)
    command_input = ObjectProperty(None)

# Container for Menus
class TextworldRightLayout(BoxLayout):
    game_menu = ObjectProperty(None)

# Container for Status Bars and Menu Buttons
class TextworldMiddleLayout(BoxLayout):
    status_bars = ObjectProperty(None)
    menu_buttons = ObjectProperty(None)

# Display Class
class TextworldDisplay(Label):
    def update_text(self, text:str):
        self.text = text

# Terminal Input class, the main interface a play uses to interact with the game
class TextworldCommandInput(TextInput):
    # Nothing on focus, Update and clear text on focus loss
    def on_focus(self, instance, value, *largs):
        if value:
            return
        else:
            instance.parent.command_terminal.updateText(self.text)
            self.text = ""

# Terminal to hold old player inputs and game outputs
class TextworldCommandTerminal(Label):
    command_queue = []
    max_queue = 10
    # Take in some text, add it to the queue and display it
    def updateText(self, text:str):
        if text == "":
            return
        else:
            self.command_queue.append(text)
            self.text += f'{text}\n'
        if len(self.command_queue) > self.max_queue:
            self.clearQueue('AGED')

    # Take in a clearing mode and the queue will clear per mode
    def clearQueue(self, mode:str):
        match mode:
            # Remove everything
            case 'CLEAR':
                self.text = ""
                self.command_queue = []
            # Remove messages outside queue max size
            case 'AGED':
                self.command_queue.pop(0)
                self.text = ""
                for cmd in self.command_queue:
                    self.text += f'{cmd}\n'

# The right side menu for Stats, Equipment, Spells, etc
class TextworldGameMenu(Label):
    text = "Place holder Text"

# Game Container
class TextworldGameLayout(BoxLayout):
    left_panel = ObjectProperty(None)
    right_panel = ObjectProperty(None)

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
        self._keyboard = None

    # Determin input and if movement is possible for temp camera
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        # keycode is a tuple (integer, string)
        match keycode[1]:
            case 'left':
                match self.world_position[0]:
                    case x if x - 1 < 0:
                        self.world_position[0] = 0
                    case _:
                        self.world_position[0] -= 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
            case 'right':
                match self.world_position[0]:
                    case x if x + 1 > self.active_world.dimensions[0] - 1:
                        self.world_position[0] = self.world_position[0]
                    case _:
                        self.world_position[0] += 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
            case 'up':
                match self.world_position[1]:
                    case y if y - 1 < 0:
                        self.world_position[1] = 0
                    case _:
                        self.world_position[1] -= 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
            case 'down':
                match self.world_position[1]:
                    case y if y + 1 > self.active_world.dimensions[1] - 1:
                        self.world_position[1] = self.world_position[1]
                    case _:
                        self.world_position[1] += 1
                self.setActiveMap(self.world_position[0], self.world_position[1])
        return True

    # Does nothing at the moment
    def _on_key_up(self, keyboard, keycode):
        return True

    # Takes an overload of either an existing world or the settings to create a world
    def loadWorld(self, *world):
        if len(world) == 1:
            self.active_world = world[0]
        else:
            self.active_world = TextworldWorld(world[0], world[1], world[2], world[3], self.world_generator)

    # Set the active World Map, Default gens new map
    def setActiveMap(self, map_x:int, map_y:int):
        self.active_map = self.active_world.world_maps[map_x][map_y]
        print(f'X: {map_x} Y: {map_y}')

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(App):

    # This Runs everything
    def build(self):

        # Window Defaults
        Window.size = (1280,720)
        Window.maximize()

        # Init UI and Management System
        self.game = TextworldGameLayout()
        self.management_system = TextworldGameManagementSystem(5, 5, 140, 38, 2, 2, 42069)

        # Schedule Display Render Call
        Clock.schedule_interval(self.update_display, 1/30)

        # Return App to be run
        return self.game

    # Display Render Loop
    def update_display(self, dt):
        self.game.left_panel.display.text = self.management_system.active_map.map_string

# Config Write settings to be moved
if __name__ == '__main__':
    TextworldApp().run()

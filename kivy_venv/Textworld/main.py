from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
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

# Game Container
class TextworldGameLayout(BoxLayout):
    left_panel = ObjectProperty(None)
    right_panel = ObjectProperty(None)

# Display Class
class TextworldDisplay(Label):
    pass

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

# Management system. This is the center for most data, Map, World, Active NPC lists, etc
class TextworldGameManagementSystem():
    def __init__(self, _width:int, _height:int, _cols:int, _rows:int, *seed:int):
        if len(seed) == 1:
            self.world_generator = TextworldGenerator(seed[0])
        else:
            self.world_generator = TextworldGenerator()
        self.loadWorld(_width, _height, _cols, _rows)

    def loadWorld(self, *world):
        if len(world) == 1:
            self.active_world = world[0]
        else:
            self.active_world = TextworldWorld(world[0], world[1], world[2], world[3], self.world_generator)

    # Set the active World Map, Default gens new map
    def setActiveMap(self, map_x:int, map_y:int):
        self.active_map = self.active_world.world_maps[map_x][map_y]

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(App):
    def build(self):
        Window.size = (1280,720)
        Window.maximize()
        management_system = TextworldGameManagementSystem(1, 1, 140, 38, 42069)
        game = TextworldGameLayout()
        management_system.setActiveMap(0, 0)
        game.left_panel.display.text = management_system.active_map.map_string
        return game

# Config Write settings to be moved
if __name__ == '__main__':
    TextworldApp().run()

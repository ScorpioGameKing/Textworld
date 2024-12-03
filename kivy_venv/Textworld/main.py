from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config
from generate import TextworldGenerator, TextworldMap # type: ignore

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
    def updateText(self, text):
        if text == "":
            return
        else:
            self.command_queue.append(text)
            self.text += f'{text}\n'
        if len(self.command_queue) > self.max_queue:
            self.clearQueue('AGED')
    
    # Take in a clearing mode and the queue will clear per mode
    def clearQueue(self, mode):
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
    def __init__(self):
        self.world_generator = TextworldGenerator()
    
    # Set the active World Map, Default gens new map 
    def setActiveMap(self, map=None):
        if map == None:
            self.active_map = self.world_generator.TestGen(38, 16)
        else:
            self.active_map = map

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(App):
    def build(self):
        management_system = TextworldGameManagementSystem()
        game = TextworldGameLayout()
        management_system.setActiveMap(management_system.world_generator.testGen(37, 14))
        print(management_system.active_map.getMapTile(0, 0).tile_string)
        game.left_panel.display.text = management_system.active_map.map_string
        return game
    
# Config Write settings to be moved
if __name__ == '__main__':
    Config.set('graphics','resizable', True)
    Config.write()
    TextworldApp().run()
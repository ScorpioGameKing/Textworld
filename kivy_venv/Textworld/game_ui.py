from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from camera import TextworldCamera
from generate import TextworldMap

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
    def buildCamera(self, _view_w, _view_h, _max_cols, _max_rows):
        self.camera = TextworldCamera(_view_w, _view_h, _max_cols, _max_rows)

    def update_text(self, text:str, position, main_chunk:TextworldMap, surrounding_8):
        self.text = text
        self.camera.selectViewportArea(position, main_chunk, surrounding_8)

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

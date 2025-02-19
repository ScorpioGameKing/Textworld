from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from engine.handbook import HandbookLang
from engine.game_manager import TextworldGameManagementSystem
from functools import partial

# Container for Display, Terminal and Input
class TextworldLLayout(BoxLayout):
    display = ObjectProperty(None)
    command_terminal = ObjectProperty(None)
    command_input = ObjectProperty(None)

# Container for Menus
class TextworldRLayout(BoxLayout):
    game_menu = ObjectProperty(None)

# Container for Status Bars and Menu Buttons
class TextworldMiddleLayout(BoxLayout):
    status_bars = ObjectProperty(None)
    menu_buttons = ObjectProperty(None)

# Display Class
class TextworldGDisplay(Label):
    def update_text(self, text:str):
        self.text = text

# Terminal Input class, the main interface a play uses to interact with the game
class TextworldGInput(TextInput):
    def __init__(self, **kwargs):
        super(TextworldGInput, self).__init__(**kwargs)
        self.typing = False

    # Nothing on focus, Update and clear text on focus loss
    def on_focus(self, instance, value, *largs):
        if value:
            self.typing = True
        else:
            instance.parent.command_terminal.updateText(self.text)
            self.text = ""
            self.typing = False

# Terminal to hold old player inputs and game outputs
class TextworldGTerminal(Label):
    handbook:HandbookLang
    command_queue = []
    max_queue = 10
    # Take in some text, add it to the queue and display it
    def updateText(self, text:str):
        if text == "":
            return
        else:
            self.handbook.lexer.lexRawString(text)
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
class TextworldGMenu(Label):
    text = "DEBUG CONTROLS:\nARROWS: Move Camera\nCLICK COMMAND INPUT: Enable Typing"

# Game Container
class TextworldGLayout(BoxLayout):
    left_panel = ObjectProperty(None)
    right_panel = ObjectProperty(None)

# Wraps everything in a screen
class TextworldGScreen(Screen):
    game_layout = ObjectProperty(None)
    game_manager = TextworldGameManagementSystem()

    def on_pre_enter(self, *args):
        self.displayUpdates = Clock.schedule_interval(partial(self.game_manager.update_display, self.game_layout.left_panel.display, self.game_layout.left_panel.command_input), 0.0125)
        self.game_layout.left_panel.command_terminal.handbook = HandbookLang()
        return super().on_enter(*args)

    def on_pre_leave(self, *args):
        self.displayUpdates.cancel()
        return super().on_leave(*args)
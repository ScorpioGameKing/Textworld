from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class TextworldMMTitle(Label):
    pass

class TextworldMMNew(Button):
    pass

class TextworldMMLoad(Button):
    pass

class TextworldMMTools(Button):
    pass

class TextworldMMExit(Button):
    pass

# Container for Title and Menu Buttons
class TextworldMMLayout(BoxLayout):
    title = ObjectProperty(None)
    btn_new = ObjectProperty(None)
    btn_load = ObjectProperty(None)
    btn_tools = ObjectProperty(None)
    btn_exit = ObjectProperty(None)

# Wraps the Layout into a screen
class TextworldMMScreen(Screen):
    layout = ObjectProperty(None)

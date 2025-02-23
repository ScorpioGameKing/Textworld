from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
import logging

class TextworldNGTitle(Label):
    pass

class TextworldNGNameRow(BoxLayout):
    pass

class TextworldNGSizeRow(BoxLayout):
    pass

class TextworldNGCountRow(BoxLayout):
    pass

class TextworldNGButtonRow(BoxLayout):
    pass

class TextworldNGProgressBar(ProgressBar):
    def update_progress(self, _value:float):
        logging.debug(f"Updating: {_value}")
        self.value = _value

class TextworldNGLayout(BoxLayout):
    title = ObjectProperty(None)
    name_row = ObjectProperty(None)
    size_row = ObjectProperty(None)
    count_row = ObjectProperty(None)
    button_row = ObjectProperty(None)
    progress = ObjectProperty(None)

class TextworldNGScreen(Screen):
    layout = ObjectProperty(None)
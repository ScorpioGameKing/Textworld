from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database import WorldDatabase

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

class TextworldNGLayout(BoxLayout):
    title = ObjectProperty(None)
    name_row = ObjectProperty(None)
    size_row = ObjectProperty(None)
    count_row = ObjectProperty(None)
    button_row = ObjectProperty(None)

class TextworldNGScreen(Screen):
    layout = ObjectProperty(None)
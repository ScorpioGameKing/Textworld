from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class TextworldTLTitle(Label):
    pass

class TextworldTLTileBtn(Button):
    pass

class TextworldTLItemBtn(Button):
    pass

class TextworldTLClassBtn(Button):
    pass

class TextworldTLNPCBtn(Button):
    pass

class TextworldTLObjBtn(Button):
    pass

class TextworldTLQstBtn(Button):
    pass

class TextworldTLBackBtn(Button):
    pass

class TextworldTLLayout(BoxLayout):
    title = ObjectProperty(None)
    tile_builder_btn = ObjectProperty(None)
    item_builder_btn = ObjectProperty(None)
    class_builder_btn = ObjectProperty(None)
    npc_builder_btn = ObjectProperty(None)
    object_builder_btn = ObjectProperty(None)
    quest_builder_btn = ObjectProperty(None)
    back_btn = ObjectProperty(None)

class TextworldTLScreen(Screen):
    layout = ObjectProperty(None)
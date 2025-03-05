from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivymd.app import MDApp
from kivymd.uix.transition.transition import MDSlideTransition
from kivy.properties import ObjectProperty

class TextworldTLTitle(MDLabel):
    pass

class TextworldTLTileBtn(MDButton):
    pass

class TextworldTLItemBtn(MDButton):
    pass

class TextworldTLClassBtn(MDButton):
    pass

class TextworldTLNPCBtn(MDButton):
    pass

class TextworldTLObjBtn(MDButton):
    pass

class TextworldTLQstBtn(MDButton):
    pass

class TextworldTLBackBtn(MDButton):
    def on_press(self):
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='right')
        MDApp.get_running_app().game.current = 'main_menu_ui'

class TextworldTLLayout(MDBoxLayout):
    title = ObjectProperty(None)
    tile_builder_btn = ObjectProperty(None)
    item_builder_btn = ObjectProperty(None)
    class_builder_btn = ObjectProperty(None)
    npc_builder_btn = ObjectProperty(None)
    object_builder_btn = ObjectProperty(None)
    quest_builder_btn = ObjectProperty(None)
    back_btn = ObjectProperty(None)

class TextworldTLScreen(MDScreen):
    layout = ObjectProperty(None)
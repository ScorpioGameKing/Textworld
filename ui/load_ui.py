from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class TextworldLdSaveView(ScrollView):
    pass

class TextworldLdBackBtn(Button):
    pass

class TextworldLdLeftPanel(BoxLayout):
    save_view = ObjectProperty(None)
    back_btn = ObjectProperty(None)

class TextworldLdDeleteBtn(Button):
    pass

class TextworldLdLoadBtn(Button):
    pass

class TextworldLdOptions(BoxLayout):
    delete = ObjectProperty(None)
    load = ObjectProperty(None)

class TextworldLdInfoPanel(BoxLayout):
    pass

class TextworldLdRightPanel(BoxLayout):
    info_panel = ObjectProperty(None)
    options = ObjectProperty(None)

class TextworldLdMenuLayout(BoxLayout):
    left_panel = ObjectProperty(None)
    right_panel = ObjectProperty(None)

class TextworldLdScreen(Screen):
    layout = ObjectProperty(None)

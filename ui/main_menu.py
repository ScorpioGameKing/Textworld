from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.transition.transition import MDSlideTransition
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton
from kivy.properties import ObjectProperty

class TextworldMMTitle(MDLabel):
    pass

class TextworldMMNew(MDButton):
    def on_press(self):
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='down')
        MDApp.get_running_app().game.current = 'new_gen_ui'
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='up')

class TextworldMMLoad(MDButton):
    def on_press(self):
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='up')
        MDApp.get_running_app().game.current = 'load_ui'
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='down')

class TextworldMMTools(MDButton):
    def on_press(self):
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='left')
        MDApp.get_running_app().game.current = 'tools_ui'

class TextworldMMExit(MDButton):
    def on_press(self):
        MDApp.get_running_app().stop()

# Container for Title and Menu Buttons
class TextworldMMLayout(MDBoxLayout):
    title = ObjectProperty(None)
    btn_new = ObjectProperty(None)
    btn_load = ObjectProperty(None)
    btn_tools = ObjectProperty(None)
    btn_exit = ObjectProperty(None)

# Wraps the Layout into a screen
class TextworldMMScreen(MDScreen):
    layout = ObjectProperty(None)

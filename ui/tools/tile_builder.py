from database import TileDatabase, Tile
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivymd.uix.transition.transition import MDSlideTransition

class TileBuilder():
    def load_tile_db(self):
        with TileDatabase() as db:
            db.open()
            self.sys_tiles = db.execute_one(Tile.SELECT_ALL)
        print(self.sys_tiles)

class TileBuilderTitle(MDLabel):
    pass

class TileBuilderBackBtn(MDButton):
    def on_press(self):
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='right')
        MDApp.get_running_app().game.current = 'tools_ui'

class TileBuilderLayout(MDBoxLayout):
    title = ObjectProperty(None)
    back_btn = ObjectProperty(None)

class TileBuilderScreen(MDScreen):
    layout = ObjectProperty(None)

    def __init__(self, **kw):
        super(TileBuilderScreen, self).__init__(**kw)
        self.tb = TileBuilder()

    def on_enter(self):
        self.tb.load_tile_db()

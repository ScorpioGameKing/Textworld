from engine.database import TileDatabase, Tile
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton
from kivymd.uix.transition.transition import MDSlideTransition

class TileBuilder:
    def load_tile_db(self, button_panel):
        button_panel.clear_widgets()
        with TileDatabase() as db:
            db.open()
            self.sys_tiles = db.execute_many(Tile.SELECT_ALL)
            print(self.sys_tiles)
            for _tile in self.sys_tiles:
                button_panel.add_widget(LoadedTile(_tile[0]))

class TileBuilderTitle(MDLabel):
    pass

class TileBuilderBackBtn(MDButton):
    def on_press(self):
        MDApp.get_running_app().game.transition = MDSlideTransition(direction='right')
        MDApp.get_running_app().game.current = 'tools_ui'

class LoadedTile(MDButton):
    char = ObjectProperty(None)

    def __init__(self, char:str, **kwargs):
        super(LoadedTile, self).__init__(**kwargs)
        self.char.text = char

    def on_press(self):
        print(self.char.text)

class TileBuilderLoadedTiles(MDBoxLayout):
    pass

class TileBuilderTileWeights(MDBoxLayout):
    pass

class TileBuilderTileProps(MDBoxLayout):
    pass

class TileBuilderLeftPanel(MDBoxLayout):
    loaded_tiles = ObjectProperty(None)
    back_btn = ObjectProperty(None)

class TileBuilderCenterPanel(MDBoxLayout):
    title = ObjectProperty(None)
    tile_weights = ObjectProperty(None)

class TileBuilderRightPanel(MDBoxLayout):
    tile_props = ObjectProperty(None)

class TileBuilderLayout(MDBoxLayout):
    left_panel = ObjectProperty(None)
    center_panel = ObjectProperty(None)
    right_panel = ObjectProperty(None)

class TileBuilderScreen(MDScreen):
    layout = ObjectProperty(None)

    def __init__(self, **kw):
        super(TileBuilderScreen, self).__init__(**kw)
        self.tb = TileBuilder()

    def on_enter(self):
        self.tb.load_tile_db(self.layout.left_panel.loaded_tiles)

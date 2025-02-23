from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from ui.game_ui import TextworldGScreen
from ui.main_menu import TextworldMMScreen
from ui.load_ui import TextworldLdScreen
from ui.new_game_ui import TextworldNGScreen
from generation import TextworldWorld
from models import Size
from database import WorldDatabase

class TextworldUIManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = (1438,720)

        Builder.load_file(".\\ui\\kv\\new_game_ui.kv")
        Builder.load_file(".\\ui\\kv\\load_ui.kv")
        Builder.load_file(".\\ui\\kv\\mod_tools_ui.kv")
        Builder.load_file(".\\ui\\kv\\main_menu.kv")
        Builder.load_file(".\\ui\\kv\\game_ui.kv")

        self.add_widget(TextworldMMScreen(name='main_menu_ui'))
        self.add_widget(TextworldGScreen(name='game_ui'))
        self.add_widget(TextworldLdScreen(name='load_ui'))
        self.add_widget(TextworldNGScreen(name='new_gen_ui'))

    def loadSaveMenuCall(self, world):
        self.current = 'game_ui'
        self.screens[1].game_manager.loadWorld(world)
        self.screens[1].game_manager.buildCamera()
    
    def newGenMenuCall(self):
        _save_name = self.get_screen(self.current).layout.name_row.save_name.text
        _chunk_size = self.get_screen(self.current).layout.size_row.chunk_size.text
        _chunk_count = self.get_screen(self.current).layout.count_row.chunk_count.text
        try:
            _chunk_size = int(_chunk_size)
        except:
            print("Size is not a number!")
            pass
        try:
            _chunk_count = int(_chunk_count)
        except:
            print("count is not a number!")
            pass
        if type(_chunk_size) == int and type(_chunk_count) == int:
            world = TextworldWorld(chunk_count=Size(_chunk_count,_chunk_count), chunk_size=Size(_chunk_size,_chunk_size))
            world.generate_map()
            with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), _save_name)
            self.current = 'game_ui'
            self.screens[1].game_manager.loadWorld(world)
            self.screens[1].game_manager.buildCamera()

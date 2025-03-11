from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from engine.ui import TextworldGScreen
from engine.ui import TextworldMMScreen
from engine.ui import TextworldLdScreen
from engine.ui import TextworldNGScreen
from engine.ui import TextworldTLScreen
from engine.ui import TileBuilderScreen
from engine.generation import TextworldWorld
from models import Size, Coords, Tile
from engine.entities import Player
from engine.database import WorldDatabase
from functools import partial
import logger
import math as m

class TextworldUIManager(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = (1438,720)

        Builder.load_file("./engine/ui/kv/new_game_ui.kv")
        Builder.load_file("./engine/ui/kv/load_ui.kv")
        Builder.load_file("./engine/ui/kv/tools_ui.kv")
        Builder.load_file("./engine/ui/kv/main_menu.kv")
        Builder.load_file("./engine/ui/kv/game_ui.kv")
        Builder.load_file("./engine/ui/kv/tools/tile_builder.kv")

        self.add_widget(TextworldMMScreen(name='main_menu_ui'))
        self.add_widget(TextworldGScreen(name='game_ui'))
        self.add_widget(TextworldLdScreen(name='load_ui'))
        self.add_widget(TextworldNGScreen(name='new_gen_ui'))
        self.add_widget(TextworldTLScreen(name='tools_ui'))
        self.add_widget(TileBuilderScreen(name='tile_builder'))
    
    def update_gen_progess(self, val:float):
        Clock.schedule_once(partial(self.get_screen('new_gen_ui').layout.progress.update, val), 0)

    def load_save_menu_call(self, world, save_name):
        self.current = 'game_ui'

        # HACK
        self.player = world.players[1]

        self.screens[1].game_manager.save_name = save_name
        self.screens[1].game_manager.load_world(self.player, world)
        self.screens[1].game_manager.build_camera(self.screens[1].game_manager.player.tile.position, Size(24, 104), self.screens[1].game_manager.active_world.chunk_size)
    
    def new_gen_menu_call(self):
        _save_name = self.get_screen(self.current).layout.name_row.save_name.text
        _chunk_size = self.get_screen(self.current).layout.size_row.chunk_size.text
        _chunk_count = self.get_screen(self.current).layout.count_row.chunk_count.text
        
        try:
            _chunk_size = int(_chunk_size)
        except:
            logger.debug("Size is not a number!")
            pass

        try:
            _chunk_count = int(_chunk_count)
        except:
            logger.debug("Count is not a number!")
            pass

        if type(_chunk_size) == int and type(_chunk_count) == int:
            world = TextworldWorld(chunk_count=Size(_chunk_count,_chunk_count), chunk_size=Size(_chunk_size,_chunk_size))
            world.generate_map(progress_callback=self.update_gen_progess)
            with WorldDatabase() as db:
                db.save_world_to_db(world.save_world(), _save_name)
            self.current = 'game_ui'
            
            # HACK
            self.player = Player(Tile("P", "ffffff", "Player", Coords(m.floor(world.chunk_size.width / 2), m.floor(world.chunk_size.height / 2))), Coords(world.chunk_count.width // 2, world.chunk_count.height // 2), Size(1, 1), 10, 10, 1, 3)

            self.screens[1].game_manager.save_name = _save_name
            self.screens[1].game_manager.load_world(self.player, world)
            self.screens[1].game_manager.build_camera(Coords(self.screens[1].game_manager.active_world.chunk_count.width // 2, self.screens[1].game_manager.active_world.chunk_count.height // 2), Size(24, 104), self.screens[1].game_manager.active_world.chunk_size)

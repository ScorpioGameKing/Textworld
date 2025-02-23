from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from ui.game_ui import TextworldGScreen
from ui.main_menu import TextworldMMScreen
from ui.load_ui import TextworldLdScreen
from ui.new_game_ui import TextworldNGScreen

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
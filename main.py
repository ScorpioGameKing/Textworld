from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from ui.game_ui import TextworldGScreen
from ui.main_menu import TextworldMMScreen
from ui.load_ui import TextworldLdScreen

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(App):

    # This Runs everything
    def build(self):

        Builder.load_file(".\\ui\\new_game_ui.kv")
        Builder.load_file(".\\ui\\load_ui.kv")
        Builder.load_file(".\\ui\\mod_tools_ui.kv")
        Builder.load_file(".\\ui\\main_menu.kv")
        Builder.load_file(".\\ui\\game_ui.kv")

        # Window Defaults
        Window.size = (1438,720)

        # Init UI and Management System
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(TextworldMMScreen(name='main_menu_ui'))
        self.screen_manager.add_widget(TextworldGScreen(name='game_ui'))
        self.screen_manager.add_widget(TextworldLdScreen(name='load_ui'))
        self.game = self.screen_manager

        # Return App to be run
        return self.game


# Config Write settings to be moved
if __name__ == '__main__':
    TextworldApp().run()

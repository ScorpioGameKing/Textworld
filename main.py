from kivy.app import App
from engine.ui_manager import TextworldUIManager

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(App):

    # This Runs everything
    def build(self):

        # Init UI and Management System
        self.game = TextworldUIManager()

        # Return App to be run
        return self.game

# Config Write settings to be moved
if __name__ == '__main__':
    TextworldApp().run()

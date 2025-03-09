from kivy.config import Config


Config.set('kivy', 'log_level', 'error')
Config.write()

from kivy.app import App
from engine.ui_manager import TextworldUIManager
from database import Database
from database import Color, World, Tile
import logger

logger.trace("Logger configured")

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
    logger.trace('Initializing Application')

    with Database() as db:
        db.init_db(Color.INIT, Color.FILL, Tile.INIT, Tile.FILL, World.INIT)
    logger.Config.set_log_level(logger.Level.INFO)
    logger.debug('check if level updated')
    TextworldApp().run()

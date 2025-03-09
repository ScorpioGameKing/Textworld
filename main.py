from kivy.config import Config


Config.set('kivy', 'log_level', 'error')
Config.write()

from kivy.core.text import LabelBase
from kivy.metrics import sp
from kivy.utils import hex_colormap
from kivymd.app import MDApp
from engine.ui_manager import TextworldUIManager
from engine.database import Database, Color, World, Tile
import logger

logger.trace("Logger configured")

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(MDApp):

    # This Runs everything
    def build(self):

        LabelBase.register(
            name="monocraft-ui", 
            fn_regular="./Assets/Fonts/Monocraft.ttf"
        )
        LabelBase.register(
            name="monocraft-game", 
            fn_regular="./Assets/Fonts/Monocraft.ttf"
        )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.backgroundColor = '#505050'

        self.theme_cls.font_styles["monocraft-ui"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "monocraft-ui",
                "font-size": sp(64)
            },
            "medium": {
                "line-height": 1.52,
                "font-name": "monocraft-ui",
                "font-size": sp(28)
            },
            "small": {
                "line-height": 1,
                "font-name": "monocraft-ui",
                "font-size": sp(18)
            }
        }

        self.theme_cls.font_styles["monocraft-game"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "monocraft-game",
                "font-size": sp(64)
            },
            "medium": {
                "line-height": 1.52,
                "font-name": "monocraft-game",
                "font-size": sp(28)
            },
            "small": {
                "line-height": 1,
                "font-name": "monocraft-game",
                "font-size": sp(12)
            }
        }

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

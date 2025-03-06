from kivy.core.text import LabelBase
from kivy.metrics import sp
from kivy.utils import hex_colormap
from kivymd.app import MDApp
from engine.ui_manager import TextworldUIManager
from database import Database
from database import Color, World, Tile

# The main kivy App, build the required parts, schedule the loops and return
class TextworldApp(MDApp):

    # This Runs everything
    def build(self):

        LabelBase.register(
            name="monocraft", 
            fn_regular="./Fonts/Monocraft.ttf"
        )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.backgroundColor = '#505050'

        self.theme_cls.font_styles["monocraft"] = {
            "large": {
                "line-height": 1.64,
                "font-name": "monocraft",
                "font-size": sp(64)
            },
            "medium": {
                "line-height": 1.52,
                "font-name": "monocraft",
                "font-size": sp(28)
            },
            "small": {
                "line-height": 1,
                "font-name": "monocraft",
                "font-size": sp(12)
            }
        }

        # Init UI and Management System
        self.game = TextworldUIManager()

        # Return App to be run
        return self.game

# Config Write settings to be moved
if __name__ == '__main__':
    with Database() as db:
        db.init_db(Color.INIT, Color.FILL, Tile.INIT, Tile.FILL, World.INIT)
    TextworldApp().run()

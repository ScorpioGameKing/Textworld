from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.progressindicator import MDLinearProgressIndicator
from kivy.properties import ObjectProperty
import logger

class TextworldNGTitle(MDLabel):
    pass

class TextworldNGNameRow(MDBoxLayout):
    pass

class TextworldNGSizeRow(MDBoxLayout):
    pass

class TextworldNGCountRow(MDBoxLayout):
    pass

class TextworldNGButtonRow(MDBoxLayout):
    pass

class TextworldNGProgressBar(MDLinearProgressIndicator):  
    def update(self, _value:float, dt):
        logger.debug(f"Updating: {self._get_value()} To: {_value}")
        self.value = _value

class TextworldNGLayout(MDBoxLayout):
    title = ObjectProperty(None)
    name_row = ObjectProperty(None)
    size_row = ObjectProperty(None)
    count_row = ObjectProperty(None)
    button_row = ObjectProperty(None)
    progress = ObjectProperty(None)

class TextworldNGScreen(MDScreen):
    layout = ObjectProperty(None)
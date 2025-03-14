from kivy.uix.widget import Widget
from kivy.core.window import Window, Keyboard
from kivy.app import App
from engine.generation import TextworldMap, TextworldWorld
from engine.camera import TextworldCamera
from models import Size, Coords
import logging

# Management system. This is the center for most data, Map, World, Active NPC lists, etc
class TextworldGameManagementSystem(Widget):

    def __init__(self, **kwargs) -> None:
        super(TextworldGameManagementSystem, self).__init__(**kwargs)
        self._keyboard:Keyboard
        self.get_focus()
        self.world_position = Coords(0, 0)
        self.save_name = ""

    def get_focus(self) -> None:
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _on_keyboard_closed(self) -> None:
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None #type: ignore

    # Keyboard Parsing, May move to standalone class and just pass keys
    def _on_key_down(self, keyboard, keycode, text, modifiers) -> None:
        if App.get_running_app().game.current == 'game_ui':
            #logging.debug(keycode)
            match keycode[1]:
                case 'left':
                    self.camera.position.x -= 1
                    if self.camera.position.x < 0:
                        self.setMap(self.world_position, x_dir=-1)
                        self.camera.position.x = self.camera.chunk_size.width - 1
                case 'right':
                    self.camera.position.x += 1
                    if self.camera.position.x > self.camera.chunk_size.width:
                        self.setMap(self.world_position, x_dir=1)
                        self.camera.position.x = 1
                case 'up':
                    self.camera.position.y -= 1
                    if self.camera.position.y < 0:
                        self.setMap(self.world_position, y_dir=-1)
                        self.camera.position.y = self.camera.chunk_size.height - 1
                case 'down':
                    self.camera.position.y += 1
                    if self.camera.position.y > self.camera.chunk_size.height:
                        self.setMap(self.world_position, y_dir=1)
                        self.camera.position.y = 1

    def buildCamera(self, _view_size:Size, _chunk_size:Size) -> None:
        self.camera = TextworldCamera(_view_size, _chunk_size)

    # Takes an existing world
    def loadWorld(self, *world) -> None:
        self.active_world = world[0]
        self.world_position = Coords(self.active_world.chunk_count.width // 2, self.active_world.chunk_count.height // 2)
        self.setMap(self.world_position)

    def setMap(self, pos:Coords, x_dir:int = 0, y_dir:int = 0) -> None:
        self.world_position.x += x_dir
        self.world_position.y += y_dir
        self.active_map = self.active_world[pos.x, pos.y]
        
    # Display Render Loop
    def update_display(self, display, command_input, dt) -> None:
        #logging.debug(f"TL: {self.world_position.x - 1, self.world_position.y - 1} T: {self.world_position.x, self.world_position.y - 1} TR: {self.world_position.x + 1, self.world_position.y - 1} \n R: {self.world_position.x - 1, self.world_position.y} M: {self.world_position.x, self.world_position.y} L: {self.world_position.x + 1, self.world_position.y}\n BL: {self.world_position.x - 1, self.world_position.y + 1} B: {self.world_position.x, self.world_position.y + 1} BR: {self.world_position.x + 1, self.world_position.y + 1}")
        view_text = self.camera.selectViewportArea(
            self.world_position,
            self.active_map, # Center Chunk Seperated for faster viewport
            [ # Surrounding 8 list, Only look at those in the veiwport based on how it overflows the main chunk
            [self.active_world[self.world_position.x - 1, self.world_position.y - 1] , # Top Left [0][0]
             self.active_world[self.world_position.x, self.world_position.y - 1] , # Top [0][1]
             self.active_world[self.world_position.x + 1, self.world_position.y - 1]], # Top Right [0][2]
            [self.active_world[self.world_position.x - 1, self.world_position.y] , # Left [1][0]
             self.active_world[self.world_position.x + 1, self.world_position.y]], # Right [1][1]
            [self.active_world[self.world_position.x - 1, self.world_position.y + 1] , # Bottom Left [2][0]
             self.active_world[self.world_position.x, self.world_position.y + 1] , # Bottom [2][1]
             self.active_world[self.world_position.x + 1, self.world_position.y + 1]], # Bottom Right [2][2]
        ])
        display.update_text(view_text)
        if command_input.typing:
            pass
        else:
            self.get_focus()
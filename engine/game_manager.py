from kivy.uix.widget import Widget
from kivy.core.window import Window, Keyboard
from generation import TextworldGenerator, TextworldMap, TextworldWorld
from engine.camera import TextworldCamera
from models import Size, Coords

# Management system. This is the center for most data, Map, World, Active NPC lists, etc
class TextworldGameManagementSystem(Widget):

    def __init__(self, **kwargs) -> None:
        super(TextworldGameManagementSystem, self).__init__(**kwargs)
        self._keyboard:Keyboard
        self.get_focus()
        self.world_position = Coords(0,0)
        self.chunk_position = Coords(75, 75)

    def get_focus(self) -> None:
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _on_keyboard_closed(self) -> None:
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None #type: ignore

    # Keyboard Parsing, May move to standalone class and just pass keys
    def _on_key_down(self, keyboard, keycode, text, modifiers) -> None:
        # keycode is a tuple (integer, string)
        #print(keycode[1])
        match keycode[1]:
            case 'left':
                self.camera.position.x -= 1
            case 'right':
                self.camera.position.x += 1
            case 'up':
                self.camera.position.y -= 1
            case 'down':
                self.camera.position.y += 1

    def buildCamera(self, _view_size:Size = Size(25, 106), _chunk_size:Size = Size(150, 150)) -> None:
        self.camera = TextworldCamera(_view_size, _chunk_size)

    # Takes an overload of either an existing world or the settings to create a world
    def loadWorld(self, *world) -> None:
        if len(world) == 1:
            self.active_world = world[0]
            self.setMap(self.world_position)
        else:
            self.active_world = TextworldWorld(world[0], world[1], world[2])
            self.setMap(world[3])

    def setMap(self, pos:Coords) -> None:
        self.active_map = self.active_world[pos.x, pos.y]

    # Get a World Map, none if OOB currently, eventually proc new generation
    def getMap(self, pos:Coords) -> TextworldMap | None:
        if pos.x < 0 or pos.y > self.active_world.chunk_size.width - 1 or pos.y < 0 or pos.y > self.active_world.chunk_size.height - 1:
            return None
        else:
            return self.active_world[pos.x, pos.y]
        
    # Display Render Loop
    def update_display(self, display, command_input, dt) -> None:
        view_text = self.camera.selectViewportArea(
            self.world_position,
            self.active_map, # Center Chunk Seperated for faster viewport
            [ # Surrounding 8 list, Only look at those in the veiwport based on how it overflows the main chunk
            [self.getMap(Coords(self.world_position.x - 1, self.world_position.y - 1)) , # Top Left
             self.getMap(Coords(self.world_position.x    , self.world_position.y - 1)) , # Top
             self.getMap(Coords(self.world_position.x + 1, self.world_position.y - 1))], # Top Left
            [self.getMap(Coords(self.world_position.x - 1, self.world_position.y    )) , # Left
             self.getMap(Coords(self.world_position.x + 1, self.world_position.y    ))], # Right
            [self.getMap(Coords(self.world_position.x - 1, self.world_position.y + 1)) , # Bottom Left
             self.getMap(Coords(self.world_position.x    , self.world_position.y + 1)) , # Bottom
             self.getMap(Coords(self.world_position.x + 1, self.world_position.y + 1))], # Bottom Right
        ])
        display.update_text(view_text)
        if command_input.typing:
            pass
        else:
            self.get_focus()
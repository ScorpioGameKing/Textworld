
from engine.entities._entity import Entity
from models import Coords, Size, Tile
from models.direction import Direction

class Mover(Entity):
    movement_speed: int
    
    def __init__(self, tile: Tile, size: Size[int], health: int, defense: int, movement_speed: int):
        Entity.__init__(self, tile, size, health, defense)

        self.movement_speed = movement_speed
    
    def move(self, direction: Direction ):
        
        (x,y) = self.tile.position
        
        if direction == Direction.NORTH:
            y-= self.movement_speed
        elif direction == Direction.EAST:
            x += self.movement_speed
        elif direction == Direction.SOUTH:
            y += self.movement_speed
        elif direction == Direction.WEST:
            x -= self.movement_speed
            
        self.tile.position = Coords(x,y)
    
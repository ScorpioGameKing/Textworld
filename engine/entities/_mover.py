
from engine.entities._entity import Entity
from models import Coords, Size
from models.direction import Direction

class Mover(Entity):
    movement_speed: int
    
    def __init__(self, name: str, position: Coords, size: Size[int], health: int, defense: int, movement_speed: int):
        Entity.__init__(self, name, position, size, health, defense)

        self.movement_speed = movement_speed
    
    def move(self, direction: Direction ):
        
        (x,y) = self.position
        
        if direction == Direction.NORTH:
            y-= self.movement_speed
        elif direction == Direction.EAST:
            x += self.movement_speed
        elif direction == Direction.SOUTH:
            y += self.movement_speed
        elif direction == Direction.WEST:
            x -= self.movement_speed
            
        self.position = Coords(x,y)
    
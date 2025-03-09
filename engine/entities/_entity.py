from models import Coords, Size

class Entity():
    position: Coords
    name: str
    size: Size[int]
    health: int
    defense: int
    is_dead: bool = False
    
    def __init__(self, name: str, position: Coords, size: Size[int], health: int, defense: int):
        self.name = name
        self.position = Coords(*position)
        self.size = size
        self.health = health
        self.defense = defense
        
    def damage(self, amount: int):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            self.is_dead = True
    
    
    def __repr__(self):
        return f"Entity {self.name} at {self.position} with size {self.size} and health {self.health}"
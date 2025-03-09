from models import Coords, Size, Tile

class Entity():
    position: Coords
    tile: Tile
    size: Size[int]
    health: int
    defense: int
    is_dead: bool = False
    
    def __init__(self, tile: Tile, size: Size[int], health: int, defense: int):
        self.tile = tile
        self.size = size
        self.health = health
        self.defense = defense
        
    def damage(self, amount: int):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            self.is_dead = True
    
    def __repr__(self):
        return f"Entity {self.tile.name} at {self.tile.position} with size {self.size} and health {self.health}"
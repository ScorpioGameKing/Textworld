from engine.entities._mob import Mob
from models import Coords, Size, Tile

class Player(Mob):

    def __init__(self, tile: Tile, chunk_pos:Coords, size: Size[int], health: int, defense: int, movement_speed: int, attack_power: int):
        Mob.__init__(self, tile, chunk_pos, size, health, defense, movement_speed, attack_power)
        self.id = 1
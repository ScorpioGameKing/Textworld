from engine.entities._mob import Mob
from models import Coords, Size, Tile

class Player(Mob):

    def __init__(self, tile: Tile, size: Size[int], health: int, defense: int, movement_speed: int, attack_power: int):
        Mob.__init__(self, tile, size, health, defense, movement_speed, attack_power)
       
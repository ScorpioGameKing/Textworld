
from engine.entities._mob import Mob
from models import Coords, Size


class Player(Mob):

    def __init__(self, name: str, position: Coords, size: Size[int], health: int, defense: int, movement_speed: int, attack_power: int):
        Mob.__init__(self, name, position, size, health, defense, movement_speed, attack_power)
       
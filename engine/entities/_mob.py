
from engine.entities._attacker import Attacker
from engine.entities._mover import Mover
from models import Coords, Size



class Mob(Attacker, Mover):
    
    level: int = 1
    intelligence: int = 5
    attack_speed: int = 5
    luck: int = 5
    demoinc_engergy: int = 0
    holy_power: int = 0
    internal_engergy: int = 0
    unity: int = 0

    def __init__(self, name: str, position: Coords, size: Size[int], health: int, defense: int, movement_speed: int, attack_power: int):
        Attacker.__init__(self, name, position, size, health, defense, attack_power)
        Mover.__init__(self, name, position, size, health, defense, movement_speed)
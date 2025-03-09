
from engine.entities._entity import Entity
from models import Coords, Size

class Attacker(Entity):
    attack_power: int
    mana_points: int = 0
    
    def __init__(self, name: str, position: Coords, size: Size[int], health: int, defense: int, attack_power: int):
        Entity.__init__(self, name, position, size, health, defense)
        self.attack_power = attack_power
    
    def attack(self, target: Entity):
        if not target.is_dead:
            target.damage(self.attack_power)
from typing import Tuple
from simulation_classes.entity import Entity
from abc import abstractmethod

class Creature(Entity):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self):
        pass

class Herbivore(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position, speed, hp)

    def make_move(self):
        pass

    def get_symbol(self):
        return '🦕'


class Predator(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int, attack_power):
        super().__init__(position, speed, hp)
        self.attack_power = attack_power

    def make_move(self):
        pass

    def get_symbol(self):
        return '🦖'
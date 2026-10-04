from abc import ABC, abstractmethod
from typing import Tuple

class Entity(ABC):
    def __init__(self, position: Tuple[int, int]):
        self.position = position
    @abstractmethod
    def get_symbol(self):
        pass

class Grass(Entity):
    def __init__(self, position: Tuple[int, int], nutritional_value: int = 10):
        super().__init__(position)
        self.nutritional_value = nutritional_value

    def get_symbol(self):
        return '🌿'

class Rock(Entity):
    def __init__(self, position: Tuple[int, int]):
        super().__init__(position)

    def get_symbol(self):
        return '🪨'

class Tree(Entity):
    def __init__(self, position: Tuple[int, int]):
        super().__init__(position)

    def get_symbol(self):
        return '🌳'

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
        pass

class Predator(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int, attack_power):
        super().__init__(position, speed, hp)
        self.attack_power = attack_power

    def make_move(self):
        pass

    def get_symbol(self):
        pass






class Action:
    def init_actions(self):
        pass

    def turn_actions(self):
        pass

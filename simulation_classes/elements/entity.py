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
        return "🌿"


class Rock(Entity):
    def __init__(self, position: Tuple[int, int]):
        super().__init__(position)

    def get_symbol(self):
        return "🪨"


class Tree(Entity):
    def __init__(self, position: Tuple[int, int]):
        super().__init__(position)

    def get_symbol(self):
        return "🌳"

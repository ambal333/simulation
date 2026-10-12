from simulation_classes.elements.entities.entity import Entity
from typing import Tuple


class Grass(Entity):
    def __init__(self, position: Tuple[int, int], nutritional_value: int = 10):
        super().__init__(position)
        self.nutritional_value = nutritional_value

    def get_symbol(self):
        return "🌿"

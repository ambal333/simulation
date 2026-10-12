from simulation_classes.elements.entities.entity import Entity
from typing import Tuple


class Tree(Entity):
    def __init__(self, position: Tuple[int, int]):
        super().__init__(position)

    def get_symbol(self):
        return "🌳"

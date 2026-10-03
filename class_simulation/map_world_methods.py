from typing import Tuple

class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.entities = {}

    def add_entity(self, position: Tuple[int, int], entity: 'Entity'):
        cell = self.is_empty(position)
        if cell and self.is_within_bounds(position):
            self.entities[position] = entity # обьект класса Entity
            return True
        return False

    def move_entity(self, entity: 'Entity', new_position: Tuple[int, int]):
        old_position = entity.position
        if not self.is_within_bounds(new_position) or not self.is_empty(new_position):
            return False
        self.remove_entity(old_position)
        entity.position = new_position
        self.entities[new_position] = entity
        return True

    def get_entity(self, position: Tuple[int, int]):
        return self.entities.get(position)

    def is_within_bounds(self, position: Tuple[int, int]):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def remove_entity(self, position: Tuple[int, int]):
        pos = self.is_empty(position)
        if not pos:
            del self.entities[position]
            return True
        else:
            return False

    def is_empty(self, position: Tuple[int, int]):
        return self.entities.get(position) is None
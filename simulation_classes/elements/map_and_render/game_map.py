from typing import Tuple


class Map:
    def __init__(self, width: int, height: int):
        self.width = width  # ширина
        self.height = height  # высота
        self.__entities = {}

    def add_entity(self, entity: "Entity"):
        cell = self.is_empty(entity.position)
        if cell and self.is_within_bounds(entity.position):
            self.__entities[entity.position] = entity  # обьект класса Entity
            return True
        return False

    def move_entity(self, entity: "Entity", new_position: Tuple[int, int]):
        old_position = entity.position
        if not self.is_within_bounds(new_position) or not self.is_empty(new_position):
            return False
        self.remove_entity(old_position)
        entity.position = new_position
        self.__entities[new_position] = entity
        return True

    def get_entity(self, position: Tuple[int, int]):
        return self.__entities.get(position)

    def is_within_bounds(self, position: Tuple[int, int]):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def remove_entity(self, position: Tuple[int, int]):
        pos = self.is_empty(position)
        if not pos:
            del self.__entities[position]
            return True
        else:
            return False

    def is_empty(self, position: Tuple[int, int]):
        return self.__entities.get(position) is None

    def count_entity(self, entity: "Entity"):
        count = 0
        for i in self.__entities.values():
            if isinstance(i, entity.__class__):
                count += 1
            else:
                continue
        return count

    def get_full_entities(self):
        all_entities = self.__entities.copy()
        return all_entities
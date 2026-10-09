from typing import Tuple
from simulation_classes.elements.entity import Entity
from abc import abstractmethod
from simulation_classes.elements.game_map import Map


class Creature(Entity):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, game_map: "Map"):
        pass

    def _find_entity(self, game_map: "Map", grade):
        closest_grass_pos = None
        min_distance = float("inf")
        # Перебираем все объекты на карте
        for pos, entity in game_map.entities.items():
            if isinstance(entity, grade):
                distance = abs(self.position[0] - pos[0]) + abs(
                    self.position[1] - pos[1]
                )
                if distance < min_distance:
                    min_distance = distance
                    closest_grass_pos = pos
        return closest_grass_pos

    def _is_adjacent(self, target_pos):
        dx = abs(self.position[0] - target_pos[0])
        dy = abs(self.position[1] - target_pos[1])
        return dx <= 1 and dy <= 1 and (dx + dy) > 0

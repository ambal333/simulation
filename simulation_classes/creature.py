from typing import Tuple
from simulation_classes.entity import Entity, Grass
from abc import abstractmethod
from simulation_classes.bfs import bfs_find_path
from simulation_classes.game_map import Map

class Creature(Entity):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, game_map: 'Map'):
        pass

class Herbivore(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position, speed, hp)

    def make_move(self, game_map: 'Map'):
        target_position = self.__find_grass(game_map)
        print(f"Найдена трава в {target_position}")
        path = bfs_find_path(game_map, self.position, target_position)
        print(f"Путь: {path}")
        if path and len(path) > 1:
            next_step = path[1]
            print(f"Иду в {next_step}")
            game_map.move_entity(self, next_step)

    def __find_grass(self, game_map: 'Map'):
        closest_grass_pos = None
        min_distance = float('inf')
        # Перебираем все объекты на карте
        for pos, entity in game_map.entities.items():
            if isinstance(entity, Grass):
                distance = abs(self.position[0] - pos[0]) + abs(self.position[1] - pos[1])
                if distance < min_distance:
                    min_distance = distance
                    closest_grass_pos = pos
        return closest_grass_pos

    def get_symbol(self):
        return '🦕'


class Predator(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int, attack_power):
        super().__init__(position, speed, hp)
        self.attack_power = attack_power

    def make_move(self, game_map: 'Map'):
        pass

    def get_symbol(self):
        return '🦖'
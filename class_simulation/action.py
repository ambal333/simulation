from abc import ABC, abstractmethod
import random
from map_world_methods import Map
from class_work import Rock
class Action(ABC):
    @abstractmethod
    def execute(self, game_map: 'Map') -> None:
        pass

class SpawnRock(Action):
    def execute(self, game_map: 'Map') -> None:
        x = [i for i in range(game_map.width)]
        y = [i for i in range(game_map.height)]
        while True:
            spawn_position = (random.choice(x), random.choice(y))
            if game_map.is_empty(spawn_position):
                rock = Rock(spawn_position)
                game_map.add_entity(rock)
                break
            else:
                continue

class SpawnTree(Action):
    def execute(self, game_map: 'Map') -> None:
        pass

class SpawnGrass(Action):
    def execute(self, game_map: 'Map') -> None:
        pass



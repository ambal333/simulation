from abc import ABC, abstractmethod
import random
from simulation_classes.actions.action import Action


class SpawnAction(Action):
    @abstractmethod
    def create_entity(self, position):
        pass

    def execute(self, game_map: "Map") -> None:
        x = [i for i in range(game_map.width)]
        y = [i for i in range(game_map.height)]
        while True:
            spawn_position = (random.choice(x), random.choice(y))
            if game_map.is_empty(spawn_position):
                entity = self.create_entity(spawn_position)
                if game_map.count_entity(entity) < 7:
                    game_map.add_entity(entity)
                    break
                else:
                    break

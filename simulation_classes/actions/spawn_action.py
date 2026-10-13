from abc import ABC, abstractmethod
import random
from simulation_classes.actions.action import Action
from simulation_classes.elements.entities.dynamic_obj.herbivore import Herbivore
from simulation_classes.elements.entities.dynamic_obj.predator import Predator


class SpawnAction(Action):
    @abstractmethod
    def get_entity(self, position):
        pass

    def execute(self, game_map: "Map") -> None:
        x = [i for i in range(game_map.width)]
        y = [i for i in range(game_map.height)]
        while True:
            spawn_position = (random.choice(x), random.choice(y))
            if game_map.is_empty(spawn_position):
                entity = self.get_entity(spawn_position)
                if isinstance(entity,(Herbivore, Predator)):
                    if game_map.count_entity(entity) < 10:
                        game_map.add_entity(entity)
                        break
                    else:
                        break
                else:
                    game_map.add_entity(entity)
                    break
            else:
                break

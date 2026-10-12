from simulation_classes.actions.spawn_action import SpawnAction
from simulation_classes.elements.entities.dynamic_obj.herbivore import Herbivore


class SpawnHerbivore(SpawnAction):
    def __init__(self, speed, hp):
        self.speed = speed
        self.hp = hp

    def create_entity(self, position):
        return Herbivore(position, self.speed, self.hp)

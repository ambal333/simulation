from simulation_classes.actions.spawn_action import SpawnAction
from simulation_classes.elements.entities.dynamic_obj.predator import Predator


class SpawnPredator(SpawnAction):
    def __init__(self, speed, hp, attack_power):
        self.hp = hp
        self.speed = speed
        self.attack_power = attack_power

    def create_entity(self, position):
        return Predator(position, self.speed, self.hp, self.attack_power)

from abc import ABC, abstractmethod
import random
from simulation_classes.game_map import Map
from simulation_classes.entity import Rock,Grass,Tree
from simulation_classes.creature import Predator, Herbivore

class Action(ABC):
    @abstractmethod
    def execute(self, game_map: 'Map') -> None:
        pass

class SpawnAction(Action):
    @abstractmethod
    def create_entity(self, position):
        pass

    def execute(self, game_map: 'Map') -> None:
        x = [i for i in range(game_map.width)]
        y = [i for i in range(game_map.height)]
        while True:
            spawn_position = (random.choice(x), random.choice(y))
            if game_map.is_empty(spawn_position):
                entity = self.create_entity(spawn_position)
                game_map.add_entity(entity)
                break
            else:
                continue

class SpawnRock(SpawnAction):
    def create_entity(self, position):
        return Rock(position)

class SpawnTree(SpawnAction):
    def create_entity(self, position):
        return Tree(position)

class SpawnGrass(SpawnAction):
    def create_entity(self, position):
        return Grass(position)

class SpawnHerbivore(SpawnAction):
    def __init__(self, speed, hp):
        self.speed = speed
        self.hp = hp
    def create_entity(self, position):
        return Herbivore(position, self.speed, self.hp)

class SpawnPredator(SpawnAction):
    def __init__(self, speed, hp, attack_power):
        self.hp = hp
        self.speed = speed
        self.attack_power = attack_power
    def create_entity(self, position):
        return Predator(position, self.speed, self.hp, self.attack_power)





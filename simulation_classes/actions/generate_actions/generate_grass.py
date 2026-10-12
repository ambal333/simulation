from simulation_classes.actions.spawn_action import SpawnAction
from simulation_classes.elements.entities.static_obj.grass_obj import Grass


class SpawnGrass(SpawnAction):
    def create_entity(self, position):
        return Grass(position)

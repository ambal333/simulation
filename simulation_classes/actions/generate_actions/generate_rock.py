from simulation_classes.actions.spawn_action import SpawnAction
from simulation_classes.elements.entities.static_obj.rock_obj import Rock


class SpawnRock(SpawnAction):
    def create_entity(self, position):
        return Rock(position)

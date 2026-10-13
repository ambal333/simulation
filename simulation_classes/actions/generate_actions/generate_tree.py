from simulation_classes.actions.spawn_action import SpawnAction
from simulation_classes.elements.entities.static_obj.tree_obj import Tree


class SpawnTree(SpawnAction):
    def get_entity(self, position):
        return Tree(position)

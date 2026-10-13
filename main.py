from simulation_classes.actions.generate_actions.generate_rock import SpawnRock
from simulation_classes.actions.generate_actions.generate_grass import SpawnGrass
from simulation_classes.actions.generate_actions.generate_tree import SpawnTree
from simulation_classes.actions.generate_actions.generate_herbivore import (
    SpawnHerbivore,
)
from simulation_classes.actions.generate_actions.generate_predator import SpawnPredator
from simulation_classes.elements.simulation import Simulation
from simulation_classes.elements.map_and_render.game_map import Map
from simulation_classes.elements.map_and_render.renderer import Renderer


def main():
    map_1 = Map(10, 10)
    renderer = Renderer(map_1)
    init_action = [SpawnRock(), SpawnRock(), SpawnRock(), SpawnRock(),
                   SpawnRock(),
                   SpawnRock(),
                   SpawnRock(),
                   SpawnRock(),
                   SpawnRock(),
                   SpawnRock(),
                   SpawnRock(),
                   SpawnTree(), SpawnTree(), SpawnTree(), SpawnTree(), SpawnTree(), SpawnTree(), SpawnTree(),
                   SpawnPredator(3, 100, 20),
                   SpawnHerbivore(2, 100),
                   SpawnTree(),
                   SpawnTree(),
                   SpawnGrass(),
                   SpawnGrass(),
                   SpawnPredator(2, 100, 20),
                   SpawnHerbivore(1, 100),
                   SpawnHerbivore(2, 100),
                   ]
    turn_action = [SpawnGrass(), SpawnHerbivore(1, 100)]
    first_simulation = Simulation(map_1, init_action, turn_action, renderer)
    first_simulation.start_simulation()


if __name__ == "__main__":
    main()

from simulation_classes.action import SpawnRock, SpawnGrass, SpawnTree, SpawnHerbivore, SpawnPredator
from simulation_classes.simulation import Simulation
from simulation_classes.game_map import Map
from simulation_classes.renderer import Renderer



def main():
    map_1 = Map(10, 9)
    renderer = Renderer(map_1)
    init_action = [SpawnRock(), SpawnRock(), SpawnRock(), SpawnRock(), SpawnRock(),
                   SpawnPredator(10,100,20), SpawnHerbivore(5,100), SpawnTree()]
    turn_action = [SpawnGrass()]
    first_simulation = Simulation(map_1, init_action, turn_action, renderer)
    first_simulation.start_simulation()
    first_simulation.next_turn()

if __name__ == '__main__':
    main()



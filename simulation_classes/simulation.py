from simulation_classes.creature import Creature,Herbivore,Predator
from simulation_classes.renderer import Renderer
from simulation_classes.game_map import Map
class Simulation:
    def __init__(self, game_map: 'Map', init_actions: list, turn_action: list, renderer: 'Renderer'):
        self.map = game_map
        self.init_actions = init_actions
        self.turn_actions = turn_action
        self.renderer = renderer
        self.moves = 0

    def next_turn(self):
        self.moves += 1
        print(f'Ход номер {self.moves}')
        self.move_all_entities()
        for i in self.turn_actions:
            i.execute(self.map)
        self.renderer.visual_map()

    def start_simulation(self):
        for i in self.init_actions:
            i.execute(self.map)
        self.renderer.visual_map()
        while True:
            self.next_turn()
            input('Нажмите Enter для продолжения')
    def move_all_entities(self):
        entities = list(self.map.entities.values())
        for i in entities:
            if isinstance(i, Herbivore):
                i.make_move(self.map)
    def pause_simulation(self):
        pass


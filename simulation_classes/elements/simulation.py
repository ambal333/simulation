from simulation_classes.elements.creatures.herbivore import Herbivore
from simulation_classes.elements.creatures.predator import Predator
from simulation_classes.elements.renderer import Renderer
from simulation_classes.elements.game_map import Map


class Simulation:
    def __init__(
        self,
        game_map: "Map",
        init_actions: list,
        turn_action: list,
        renderer: "Renderer",
    ):
        self.map = game_map
        self.init_actions = init_actions
        self.turn_actions = turn_action
        self.renderer = renderer
        self.moves = 0
        self.is_running = True

    def next_turn(self):
        self.moves += 1
        print(f"Ход номер {self.moves}")
        self.move_all_entities()
        for i in self.turn_actions:
            i.execute(self.map)
        self.renderer.visual_map()

    def start_simulation(self):
        for i in self.init_actions:
            i.execute(self.map)
        self.renderer.visual_map()
        while self.is_running:
            self.next_turn()
            self.check_pause()

    def check_pause(self):
        user = input("Введите Enter чтобы продолжить. p - пауза, q - выход ").lower()
        if user == "q":
            self.is_running = False
        elif user == "p":
            print("ПАУЗА")
            input("нажмите Enter для продолжения")

    def move_all_entities(self):
        entities = list(self.map.entities.values())
        for i in entities:
            if isinstance(i, Herbivore):
                i.make_move(self.map)
        for i in entities:
            if isinstance(i, Predator):
                i.make_move(self.map)

    def pause_simulation(self):
        pass

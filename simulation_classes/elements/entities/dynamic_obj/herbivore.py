from simulation_classes.elements.bfs import bfs_find_path
from simulation_classes.elements.entities.creature import Creature
from typing import Tuple
from simulation_classes.elements.entities.static_obj.grass_obj import Grass


class Herbivore(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position, speed, hp)

    def make_move(self, game_map: "Map"):
        target_position = super()._find_entity(game_map, Grass)
        if target_position is None:
            print("Трава не найдена")
            return
        if super()._is_adjacent(target_position):
            grass = game_map.get_entity(target_position)
            if grass and self.hp < 100:
                self.hp += grass.nutritional_value
                if self.hp > 100:
                    self.hp = 100
                game_map.remove_entity(target_position)
                print(f"Съели траву! HP: {self.hp}")
                return
        if self.hp <= 0:
            print("Травоядное мертво")
            return
        path = bfs_find_path(game_map, self.position, target_position)
        if not path or len(path) <= 1:
            return
        steps_made = 0
        for i in range(1, len(path)):
            if steps_made >= self.speed:
                break
            next_step = path[i]
            if game_map.move_entity(self, next_step):
                steps_made += 1
            else:
                break
        if super()._is_adjacent(target_position):
            grass = game_map.get_entity(target_position)
            if grass and self.hp < 100:
                self.hp += grass.nutritional_value
                if self.hp > 100:
                    self.hp = 100
                game_map.remove_entity(target_position)
                print(f"Дошли и съели траву! HP: {self.hp}")

    def get_symbol(self):
        return "🦕"

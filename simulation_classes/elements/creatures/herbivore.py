from simulation_classes.elements.bfs import bfs_find_path
from simulation_classes.elements.creatures.creature import Creature
from typing import Tuple
from simulation_classes.elements.entity import Grass


class Herbivore(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position, speed, hp)

    def make_move(self, game_map: "Map"):
        # 1. Ищем ближайшую траву
        target_position = super()._find_entity(game_map, Grass)
        if target_position is None:
            print("Трава не найдена")
            return
        # 2. Если трава рядом — едим
        if super()._is_adjacent(target_position):
            grass = game_map.get_entity(target_position)
            if grass and self.hp < 100:
                self.hp += grass.nutritional_value
                if self.hp > 100:
                    self.hp = 100
                game_map.remove_entity(target_position)
                print(f"Съели траву! HP: {self.hp}")
                return  # ← ВАЖНО: после еды выходим, не двигаемся
        # 3. Проверяем, живы ли мы
        if self.hp <= 0:
            print("Травоядное мертво")
            return
        # 4. Строим путь к траве
        path = bfs_find_path(game_map, self.position, target_position)
        if not path or len(path) <= 1:
            return
        # 5. Делаем до self.speed шагов
        steps_made = 0
        for i in range(1, len(path)):
            if steps_made >= self.speed:
                break
            next_step = path[i]
            if game_map.move_entity(self, next_step):
                steps_made += 1
            else:
                break  # Не удалось сделать шаг
        # 6. После движения проверяем, не оказались ли рядом с травой
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

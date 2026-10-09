from simulation_classes.elements.bfs import bfs_find_path
from simulation_classes.elements.creatures.creature import Creature
from typing import Tuple
from simulation_classes.elements.creatures.herbivore import Herbivore


class Predator(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int, attack_power):
        super().__init__(position, speed, hp)
        self.attack_power = attack_power

    def make_move(self, game_map: "Map") -> None:
        # 1. Проверяем, рядом ли жертва
        target_position = self._find_entity(game_map, Herbivore)
        if target_position is None:
            return
        # 2. Если жертва в соседней клетке — атакуем
        if self._is_adjacent(target_position):
            self._attack(game_map, target_position)
            return
        # 3. Строим путь к жертве
        path = bfs_find_path(game_map, self.position, target_position)
        if not path or len(path) <= 1:
            return
        # 4. Делаем до self.speed шагов
        steps_made = 0
        for i in range(1, len(path)):
            if steps_made >= self.speed:
                break
            next_step = path[i]
            if game_map.move_entity(self, next_step):
                steps_made += 1
                # Проверяем, не дошли ли до жертвы
                if self.position == target_position:
                    self._attack(game_map, target_position)
                    break
            else:
                break

    def _attack(self, game_map, target_pos):
        prey = game_map.get_entity(target_pos)
        if prey:
            prey.hp -= self.attack_power
            print(
                f"Хищник атаковал травоядное в {target_pos}! У жертвы осталось {prey.hp} HP"
            )
            if prey.hp <= 0:
                print("Травоядное погибло!")
                game_map.remove_entity(target_pos)

    def get_symbol(self):
        return "🦖"

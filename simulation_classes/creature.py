from typing import Tuple
from simulation_classes.entity import Entity, Grass
from abc import abstractmethod
from simulation_classes.bfs import bfs_find_path
from simulation_classes.game_map import Map

class Creature(Entity):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position)
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self, game_map: 'Map'):
        pass

    def _find_entity(self, game_map: 'Map', grade):
        closest_grass_pos = None
        min_distance = float('inf')
        # Перебираем все объекты на карте
        for pos, entity in game_map.entities.items():
            if isinstance(entity, grade):
                distance = abs(self.position[0] - pos[0]) + abs(self.position[1] - pos[1])
                if distance < min_distance:
                    min_distance = distance
                    closest_grass_pos = pos
        return closest_grass_pos

    def _is_adjacent(self, target_pos):
        dx = abs(self.position[0] - target_pos[0])
        dy = abs(self.position[1] - target_pos[1])
        return dx <= 1 and dy <= 1 and (dx + dy) > 0

class Herbivore(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int):
        super().__init__(position, speed, hp)

    def make_move(self, game_map: 'Map'):
        # 1. Ищем ближайшую траву
        target_position = super()._find_entity(game_map, Grass)
        print(f'Жертва{target_position}')
        print(f'Найдена трава в {target_position}')
        print(f'Здоровье {self.hp}')
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
        print(f"Путь: {path}")
        if not path or len(path) <= 1:
            return
        # 5. Делаем до self.speed шагов
        steps_made = 0
        for i in range(1, len(path)):
            if steps_made >= self.speed:
                break
            next_step = path[i]
            print(f"Иду в {next_step}")
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
    # def make_move(self, game_map: 'Map'):
    #     target_position = super()._find_entity(game_map, Grass)
    #     print(f'жертва{target_position}')
    #     print(f"Найдена трава в {target_position}")
    #     print(f'Здоровье {self.hp}')
    #     if target_position:
    #         if super()._is_adjacent(target_position):
    #             grass = game_map.get_entity(target_position)
    #             if self.hp < 100:
    #                 self.hp += grass.nutritional_value
    #                 if self.hp > 100:
    #                     self.hp = 100
    #             game_map.remove_entity(target_position)
    #     if self.hp > 0:
    #         path = bfs_find_path(game_map, self.position, target_position)
    #         print(f"Путь: {path}")
    #         if path and len(path) > 1:
    #             next_step = path[1]
    #             print(f"Иду в {next_step}")
    #             game_map.move_entity(self, next_step)

    def get_symbol(self):
        return '🦕'

class Predator(Creature):
    def __init__(self, position: Tuple[int, int], speed: int, hp: int, attack_power):
        super().__init__(position, speed, hp)
        self.attack_power = attack_power

    def make_move(self, game_map: 'Map') -> None:
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
            print(f"Хищник атаковал травоядное в {target_pos}! У жертвы осталось {prey.hp} HP")
            if prey.hp <= 0:
                print("Травоядное погибло!")
                game_map.remove_entity(target_pos)

    def get_symbol(self):
        return '🦖'
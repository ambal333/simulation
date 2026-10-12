from abc import ABC, abstractmethod
from simulation_classes.elements.map_and_render.game_map import Map


class Action(ABC):
    @abstractmethod
    def execute(self, game_map: "Map") -> None:
        pass

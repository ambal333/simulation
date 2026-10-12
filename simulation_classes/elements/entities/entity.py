from abc import ABC, abstractmethod
from typing import Tuple


class Entity(ABC):
    def __init__(self, position: Tuple[int, int]):
        self.position = position

    @abstractmethod
    def get_symbol(self):
        pass

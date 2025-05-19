from abc import ABC, abstractmethod
from typing import List
from domain.entities.coffee import Coffee


class CoffeePresenterInterface(ABC):
    @abstractmethod
    def present_coffees(self, coffees: List[Coffee]) -> str:
        """Present coffees in a markdown format"""
        pass

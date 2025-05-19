from abc import ABC, abstractmethod
from typing import List

from src.domain.entities.coffee import Coffee


class CoffeeRepository(ABC):
    @abstractmethod
    async def fetch_by_category(self, category_url: str) -> List[Coffee]:
        """Fetch all coffees from a category URL"""
        pass

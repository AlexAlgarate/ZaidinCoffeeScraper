from abc import ABC, abstractmethod
from typing import List, Tuple

class CategoryRepository(ABC):
    @abstractmethod
    async def fetch_categories(self) -> List[Tuple[str, str]]:
        """Fetch available coffee categories"""
        pass
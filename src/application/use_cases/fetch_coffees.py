from typing import List

from src.domain.entities.coffee import Coffee
from src.domain.repositories.coffee_repository import CoffeeRepository


class FetchCoffees:
    def __init__(self, repository: CoffeeRepository):
        self.repository = repository

    async def execute(self, url: str) -> List[Coffee]:
        return await self.repository.fetch_by_category(url)

from typing import List
from domain.repositories.coffee_repository import CoffeeRepository
from domain.entities.coffee import Coffee
from typing import List

class FetchCoffees:
    def __init__(self, repository: CoffeeRepository):
        self.repository = repository
        
    async def execute(self, url: str) -> List[Coffee]:
        return await self.repository.fetch_by_category(url)
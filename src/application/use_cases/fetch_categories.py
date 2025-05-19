from typing import List, Tuple

from src.domain.repositories.category_repository import CategoryRepository


class FetchCategories:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def execute(self) -> List[Tuple[str, str]]:
        return await self.repository.fetch_categories()

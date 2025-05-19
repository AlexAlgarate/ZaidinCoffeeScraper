import asyncio
from typing import Any, Callable, List

from src.domain.entities.coffee import Coffee
from src.domain.exceptions.coffee_exceptions import CoffeeScrapingError
from src.domain.repositories.coffee_repository import CoffeeRepository
from src.infrastructure.mappers.coffee_mapper import CoffeeMapper
from src.infrastructure.services.coffee_scraper import CoffeeScraper


class CoffeeRepositoryImpl(CoffeeRepository):
    def __init__(
        self,
        coffee_scraper: CoffeeScraper,
        coffee_mapper: CoffeeMapper,
        async_runner: Callable[..., Any] = asyncio.run,
    ):
        self._scraper = coffee_scraper
        self._mapper = coffee_mapper
        self._async_runner = async_runner

    async def fetch_by_category(self, category_url: str) -> List[Coffee]:
        try:
            coffees = []
            products = await self._scraper.scrape_category(category_url)

            for product in products:
                if product.href:
                    details = await self._scraper.scrape_details(product.href)
                    coffee = self._mapper.to_entity(product, details)
                    if coffee:
                        coffees.append(coffee)

            return coffees
        except Exception as e:
            raise CoffeeScrapingError(
                f"Error fetching category {category_url}: {str(e)}"
            )

    def fetch_coffees(self, url: str) -> List[Coffee]:
        return self._async_runner(self.fetch_by_category(url))

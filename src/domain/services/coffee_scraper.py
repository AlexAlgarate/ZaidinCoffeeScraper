from abc import ABC, abstractmethod
from typing import List
from application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails


class CoffeeScraper(ABC):
    """Abstract interface for coffee scraping operations"""

    @abstractmethod
    async def scrape_category(self, url: str) -> List[ProductBasicInfo]:
        """Scrapes a category page and returns basic product information"""
        pass

    @abstractmethod
    async def scrape_details(self, url: str) -> ProductDetails:
        """Scrapes detailed information for a specific product"""
        pass

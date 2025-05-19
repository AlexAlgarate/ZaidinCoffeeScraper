from abc import abstractmethod
from typing import List
from domain.configuration.scraping_config import ScrapingConfig


class ScrapingConfig(ScrapingConfig):
    def __init__(self, selectors: List[str]):
        self._selectors = selectors

    @abstractmethod
    def get_product_selectors(self) -> List[str]:
        """Get list of product selectors"""
        pass

    @abstractmethod
    def get_base_url(self) -> str:
        """Get base URL for scraping"""
        pass

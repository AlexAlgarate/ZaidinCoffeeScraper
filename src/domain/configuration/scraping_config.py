from abc import ABC, abstractmethod
from typing import List


class ScrapingConfig(ABC):
    @abstractmethod
    def get_product_selectors(self) -> List[str]:
        """Get the list of product selectors"""
        pass

    @abstractmethod
    def get_base_url(self) -> str:
        """Get base URL for scraping"""
        pass

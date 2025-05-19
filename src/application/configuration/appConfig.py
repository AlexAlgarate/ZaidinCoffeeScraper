from dataclasses import dataclass, field
from typing import List

from src.domain.configuration.scraping_config import ScrapingConfig


@dataclass(frozen=True)
class AppConfig(ScrapingConfig):
    base_url: str = "https://soycafetera.es"
    _product_selectors: List[str] = field(
        default_factory=lambda: [
            "div.grid__products div.grid-product",
            ".grid-product",
            "ul.products li.product",
            ".product-item",
        ]
    )

    def get_product_selectors(self) -> List[str]:
        return self._product_selectors

    def get_base_url(self) -> str:
        return self.base_url

    @classmethod
    def create_default(cls) -> "AppConfig":
        return cls()

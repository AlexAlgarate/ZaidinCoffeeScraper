from application.configuration.scraping_config import ScrapingConfig
from dataclasses import field
from typing import List

class ScrapingConfig(ScrapingConfig):
    base_url: str
    selectors: List[str] = field(default_factory=list)

    def get_product_selectors(self) -> List[str]:
        return self.selectors

    def get_base_url(self) -> str:
        return self.base_url

    @classmethod
    def create_default(cls) -> 'ScrapingConfig':
        return cls(
            base_url="https://soycafetera.es",
            selectors=[
                "div.grid__products div.grid-product",
                ".grid-product",
                "ul.products li.product",
                '.product-item'
            ]
        )
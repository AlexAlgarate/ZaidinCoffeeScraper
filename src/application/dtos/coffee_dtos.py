from dataclasses import dataclass
from typing import List


@dataclass
class ProductBasicInfo:
    name: str
    price_text: str
    href: str | None = None


@dataclass
class ProductDetails:
    displayed_price: str
    process: str
    origins: List[str]
    formats: List[str]
    packages: List[str]

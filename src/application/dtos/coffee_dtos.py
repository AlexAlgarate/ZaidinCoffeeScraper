from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ProductBasicInfo:
    name: str
    price_text: str
    href: Optional[str] = None

@dataclass
class ProductDetails:
    sku: str
    displayed_price: str
    process: str
    origins: List[str]
    formats: List[str]
    packages: List[str]
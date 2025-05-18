from dataclasses import dataclass

@dataclass(frozen=True)
class Coffee:
    name: str
    sku: str
    price_per_kg: float
    process: str
    origins: list[str]
    formats: list[str]
    packages: list[str]
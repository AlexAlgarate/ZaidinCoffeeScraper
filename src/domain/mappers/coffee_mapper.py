from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.coffee import Coffee
from application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails


class CoffeeMapper(ABC):
    """Abstract interface for coffee mapping operations"""

    @abstractmethod
    def to_entity(
        self, basic_info: ProductBasicInfo, details: ProductDetails
    ) -> Optional[Coffee]:
        """Maps DTO objects to domain entity"""
        pass

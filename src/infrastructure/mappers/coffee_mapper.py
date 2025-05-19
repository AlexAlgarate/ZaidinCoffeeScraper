from typing import Optional

from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails
from src.domain.entities.coffee import Coffee
from src.domain.entities.price import Price
from src.domain.mappers.coffee_mapper import CoffeeMapper


class CoffeeMapperImpl(CoffeeMapper):
    def to_entity(
        self, basic_info: ProductBasicInfo, details: ProductDetails
    ) -> Optional[Coffee]:
        try:
            format_text = details.formats[0] if details.formats else "250g"
            price = Price.from_text(basic_info.price_text, format_text)

            if not price:
                return None

            return Coffee(
                name=basic_info.name,
                sku=details.sku,
                price_per_kg=price.amount,
                process=details.process,
                origins=details.origins,
                formats=details.formats,
                packages=details.packages,
            )
        except Exception as e:
            print(f"Error mapping coffee {basic_info.name}: {e}")
            return None

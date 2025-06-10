import re
from typing import Any, List

from src.application.dtos.coffee_dtos import ProductDetails
from src.application.interfaces.logger import ILogger
from src.domain.services.product_extractors import ProductDetailsExtractor


class WebProductDetailsExtractor(ProductDetailsExtractor):
    def __init__(self, logger: ILogger):
        self._logger = logger

    async def extract(self, page: Any) -> ProductDetails:
        displayed_price = await self.extract_displayed_price(page)
        origins = await self.extract_origins(page)
        formats = await self.extract_formats(page)
        packages = await self.extract_packages(page)

        return ProductDetails(
            displayed_price=displayed_price,
            process="Unknown",
            origins=origins,
            formats=formats,
            packages=packages,
        )

    async def extract_displayed_price(self, page: Any) -> str:
        try:
            price_el = await page.query_selector(".details-product-price__value")
            return await price_el.inner_text() if price_el else ""
        except Exception:
            return ""

    async def extract_origins(self, page: Any) -> List[str]:
        try:
            desc_el = await page.query_selector(
                ".woocommerce-product-details__short-description"
            )
            if not desc_el:
                return ["Unknown"]

            text = await desc_el.inner_text()
            countries = ["Brasil", "Colombia", "Ethiopia", "Kenya", "Guatemala"]
            origins = [country for country in countries if country in text]

            return origins or ["Unknown"]
        except Exception:
            return ["Unknown"]

    async def extract_formats(self, page: Any) -> List[str]:
        try:
            formats_el = await page.query_selector_all(".variation-selector option")
            formats = [
                el.inner_text().strip()
                for el in formats_el
                if any(
                    size in (await el.inner_text()).lower()
                    for size in ["250g", "500g", "1kg"]
                )
            ]

            if formats:
                return formats

            format_labels = await page.query_selector_all(
                'label[for^="form-control__radio"]'
            )
            for label in format_labels:
                text = await label.inner_text()
                if "Paquete" in text:
                    quantity_match = re.search(r"Paquete\s+(\d+)\s*g", text)
                    if quantity_match:
                        formats.append(f"{quantity_match.group(1)}g")
                elif any(size in text.lower() for size in ["250g", "500g", "1kg"]):
                    formats.append(text.strip())

            return formats or ["250g"]
        except Exception as e:
            self._logger.error(f"Error extracting formats: {e}")
            return ["250g"]

    async def extract_packages(self, page: Any) -> List[str]:
        try:
            packages_el = await page.query_selector_all(".package-type option")
            if not packages_el:
                return ["Grano"]

            packages = [await el.inner_text().strip() for el in packages_el]
            return packages or ["Grano"]
        except Exception:
            return ["Grano"]

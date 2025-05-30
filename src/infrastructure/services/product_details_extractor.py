import re
from typing import Any, List

from src.application.dtos.coffee_dtos import ProductDetails
from src.application.interfaces.logger import ILogger
from src.domain.services.product_extractors import ProductDetailsExtractor


class WebProductDetailsExtractor(ProductDetailsExtractor):
    def __init__(self, logger: ILogger):
        self._logger = logger

    async def extract(self, page: Any) -> ProductDetails:
        sku = await self.extract_sku(page)
        displayed_price = await self.extract_displayed_price(page)
        process = await self.extract_process(page)
        origins = await self.extract_origins(page)
        formats = await self.extract_formats(page)
        packages = await self.extract_packages(page)

        return ProductDetails(
            sku=sku,
            displayed_price=displayed_price,
            process=process,
            origins=origins,
            formats=formats,
            packages=packages,
        )

    async def extract_sku(self, page: Any) -> str:
        try:
            sku_el = await page.query_selector('meta[itemprop="sku"]')
            return await sku_el.get_attribute("content") if sku_el else "Unknown"
        except Exception:
            return "Unknown"

    async def extract_displayed_price(self, page: Any) -> str:
        try:
            price_el = await page.query_selector(".details-product-price__value")
            return await price_el.inner_text() if price_el else ""
        except Exception:
            return ""

    async def extract_process(self, page: Any) -> str:
        try:
            desc_el = await page.query_selector(
                ".woocommerce-product-details__short-description"
            )
            if desc_el:
                text = await desc_el.inner_text()
                return self._detect_process(text)
            return "Unknown"
        except Exception:
            return "Unknown"

    async def extract_origins(self, page: Any) -> List[str]:
        try:
            desc_el = await page.query_selector(
                ".woocommerce-product-details__short-description"
            )
            if desc_el:
                text = await desc_el.inner_text()
                origins = []
                countries = ["Brasil", "Colombia", "Ethiopia", "Kenya", "Guatemala"]
                for country in countries:
                    if country in text:
                        origins.append(country)
                return origins if origins else ["Unknown"]
            return ["Unknown"]
        except Exception:
            return ["Unknown"]

    async def extract_formats(self, page: Any) -> List[str]:
        try:
            formats = []
            formats_el = await page.query_selector_all(".variation-selector option")
            if formats_el:
                for el in formats_el:
                    text = await el.inner_text()
                    if any(size in text.lower() for size in ["250g", "500g", "1kg"]):
                        formats.append(text.strip())
                if formats:
                    return formats
            format_labels = await page.query_selector_all(
                'label[for^="form-control__radio"]'
            )
            if format_labels:
                for label in format_labels:
                    text = await label.inner_text()
                    if "Paquete" in text:
                        quantity_match = re.search(r"Paquete\s+(\d+)\s*g", text)
                        if quantity_match:
                            formats.append(f"{quantity_match.group(1)}g")
                        continue
                    if any(size in text.lower() for size in ["250g", "500g", "1kg"]):
                        formats.append(text.strip())

            return formats if formats else ["250g"]
        except Exception as e:
            self._logger.error(f"Error extracting formats: {e}")
            return ["250g"]

    async def extract_packages(self, page: Any) -> List[str]:
        try:
            packages_el = await page.query_selector_all(".package-type option")
            if packages_el:
                packages = []
                for el in packages_el:
                    text = await el.inner_text()
                    packages.append(text.strip())
                return packages if packages else ["Grano"]
            return ["Grano"]
        except Exception:
            return ["Grano"]

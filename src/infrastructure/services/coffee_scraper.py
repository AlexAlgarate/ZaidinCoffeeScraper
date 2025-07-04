from typing import List
from urllib.parse import urljoin

from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails
from src.application.interfaces.logger import ILogger
from src.application.services.coffee_scraper import CoffeeScraper
from src.application.services.web_client import WebClient
from src.infrastructure.services.scraping_service import ScrapingService


class CoffeeScraper(CoffeeScraper):
    def __init__(
        self,
        web_client: WebClient,
        scraping_service: ScrapingService,
        logger: ILogger,
        base_url: str,
    ):
        self._web_client = web_client
        self._scraping_service = scraping_service
        self._logger = logger
        self._base_url = base_url

    async def scrape_category(self, url: str) -> List[ProductBasicInfo]:
        async with self._web_client as browser:
            page = await browser.new_page()
            await browser.goto(page, url)
            products = await self._scraping_service.get_products(page)
            self._logger.info(
                f"Found {len(products)} products in category {url}... scraping details..."
            )

            await browser.close_page(page)
            return products

    async def scrape_details(self, url: str) -> ProductDetails:
        full_url = urljoin(self._base_url, url)
        async with self._web_client as browser:
            return await self._scraping_service.extract_detail_info(browser, full_url)

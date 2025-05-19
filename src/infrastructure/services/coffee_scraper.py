from typing import List

from src.application.dtos.coffee_dtos import ProductBasicInfo, ProductDetails
from src.domain.services.coffee_scraper import CoffeeScraper
from src.domain.services.web_client import WebClient
from src.infrastructure.services.scraping_service import ScrapingService


class CoffeeScraper(CoffeeScraper):
    def __init__(self, web_client: WebClient, scraping_service: ScrapingService):
        self._web_client = web_client
        self._scraping_service = scraping_service

    async def scrape_category(self, url: str) -> List[ProductBasicInfo]:
        async with self._web_client as browser:
            page = await browser.new_page()
            await browser.goto(page, url)
            products = await self._scraping_service.get_products(page)
            await browser.close_page(page)
            return products

    async def scrape_details(self, url: str) -> ProductDetails:
        async with self._web_client as browser:
            return await self._scraping_service.extract_detail_info(browser, url)

from typing import List, Tuple

from src.application.interfaces.logger import ILogger
from src.domain.repositories.category_repository import CategoryRepository
from src.domain.services.web_client import WebClient


class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, client: WebClient, base_url: str, logger: ILogger):
        self._client = client
        self._base_url = base_url
        self._logger = logger

    async def fetch_categories(self) -> List[Tuple[str, str]]:
        browser = await self._client.get_browser()
        try:
            page = await browser.new_page()
            self._logger.info("→ Loading main page...")
            await page.goto(f"{self._base_url}/tienda", wait_until="networkidle")

            try:
                await page.click("button:has-text('Aceptar')", timeout=3000)
                self._logger.info("✓ Cookies accepted")
            except Exception:
                self._logger.error("No cookie banner found")

            category_links = await page.query_selector_all("a.grid-category__title")
            self._logger.info(
                f"Found {len(category_links)} category links,... scraping..."
            )

            categories = []
            tarjet_categories = ["Gama de cafés"]

            for link in category_links:
                name = (await link.inner_text()).strip()
                url = await link.get_attribute("href")

                if name in tarjet_categories and url:
                    categories.append((name, url))

            return categories

        finally:
            await browser.close()

from typing import List, Tuple

from src.domain.repositories.category_repository import CategoryRepository
from src.domain.services.web_client import WebClient


class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, client: WebClient, base_url: str):
        self._client = client
        self._base_url = base_url

    async def fetch_categories(self) -> List[Tuple[str, str]]:
        browser = await self._client.get_browser()
        try:
            page = await browser.new_page()
            print("→ Loading main page...")
            await page.goto(f"{self._base_url}/tienda", wait_until="networkidle")

            try:
                await page.click("button:has-text('Aceptar')", timeout=3000)
                print("✓ Cookies accepted")
            except Exception:
                print("No cookie banner found")

            category_links = await page.query_selector_all("a.grid-category__title")
            print(f"Found {len(category_links)} category links,... scraping...")

            categories = []
            for link in category_links:
                name = await link.inner_text()
                url = await link.get_attribute("href")
                if name and url:
                    categories.append((name.strip(), url))

            return categories
        finally:
            await browser.close()

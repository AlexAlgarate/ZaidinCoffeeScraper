from abc import ABC, abstractmethod
from typing import Any


class PageNavigator(ABC):
    @abstractmethod
    async def navigate_to_product(self, browser: Any, url: str) -> Any:
        pass


class WebPageNavigator(PageNavigator):
    async def navigate_to_product(self, browser: Any, url: str) -> Any:
        page = await browser.new_page()
        try:
            await page.goto(url, wait_until="networkidle")
            return page
        except Exception:
            await page.close()
            raise

from typing import Any

from src.domain.services.page_navigator import PageNavigator


class WebPageNavigator(PageNavigator):
    async def navigate_to_product(self, browser: Any, url: str) -> Any:
        page = await browser.new_page()
        try:
            await page.goto(url, wait_until="networkidle")
            return page
        except Exception:
            await page.close()
            raise

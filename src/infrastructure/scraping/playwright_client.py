from playwright.async_api import async_playwright
from domain.services.web_client import WebClient,Browser


class PlaywrightClient(WebClient):
    async def __aenter__(self):
        self.pw = await async_playwright().start()
        self.browser = await self.pw.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled']
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.browser.close()
        await self.pw.stop()

    async def new_page(self):
        return await self.browser.new_page()

    async def goto(self, page, url: str):
        await page.goto(url, wait_until='networkidle')

    async def close_page(self, page):
        await page.close()
    
    async def get_browser(self) -> Browser:
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(
            headless=True,
            args=['--no-sandbox']
        )
        return browser
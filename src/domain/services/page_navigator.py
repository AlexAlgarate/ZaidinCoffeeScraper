from abc import ABC, abstractmethod
from typing import Any, List


class PageNavigator(ABC):
    @abstractmethod
    async def navigate_to_page(self, browser: Any, url: str) -> Any:
        pass

    @abstractmethod
    async def get_product_elements(self, page: Any) -> List[Any]:
        pass

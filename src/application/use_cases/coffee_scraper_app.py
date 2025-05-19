from domain.repositories.coffee_repository import CoffeeRepository
from domain.repositories.category_repository import CategoryRepository
from application.interfaces.coffe_pressenter import CoffeePresenterInterface


class CoffeeScraperApp:
    def __init__(
        self,
        coffee_repository: CoffeeRepository,
        category_repository: CategoryRepository,
        presenter: CoffeePresenterInterface,
    ):
        self._coffee_repository = coffee_repository
        self._category_repository = category_repository
        self._presenter = presenter

    async def run(self) -> str:
        categories = await self._category_repository.fetch_categories()
        if not categories:
            return self._presenter.present_coffees([])

        all_coffees = []
        for name, url in categories:
            coffees = await self._coffee_repository.fetch_by_category(url)
            all_coffees.extend(coffees)

        return self._presenter.present_coffees(all_coffees)

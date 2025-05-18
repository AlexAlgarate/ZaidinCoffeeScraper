import asyncio
from application.use_cases.coffee_scraper_app import CoffeeScraperApp
from di.diContainer import Container


async def run_app() -> None:
    container = Container()
    
    app = CoffeeScraperApp(
        coffee_repository=container.coffee_repository(),
        category_repository=container.category_repository(),
        presenter=container.presenter()
    )

    try:
        print("Starting scraper...")
        result = await app.run()
        print(result)
    except Exception as e:
        print(f"Error running application: {str(e)}")
        return 1
    return 0

def main() -> int:
    return asyncio.run(run_app())

if __name__ == "__main__":
    exit(main())
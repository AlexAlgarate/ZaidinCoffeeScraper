from dependency_injector import containers, providers

from src.application.configuration.appConfig import AppConfig
from src.presentation.presenters.configurations.markdown_configuration_factory import (
    MarkdownTableConfigFactory,
)


class Container(containers.DeclarativeContainer):
    # Configuration
    config: providers.Singleton = providers.Singleton(AppConfig.create_default)

    # Web Client
    web_client: providers.Singleton = providers.Singleton(
        "src.infrastructure.scraping.playwright_client.PlaywrightClient"
    )

    # Core Services
    element_finder: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.element_finder.WebElementFinder", config=config
    )

    process_detector: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.process_detector.CoffeeProcessDetector"
    )

    page_navigator: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.page_navigator.WebPageNavigator"
    )

    # Extractors
    product_info_extractor: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.product_info_extractor.WebProductInfoExtractor"
    )

    product_details_extractor: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.product_details_extractor.WebProductDetailsExtractor"
    )

    # Collectors
    product_collector: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.scraping_service.ProductCollectorImpl",
        product_info_extractor=product_info_extractor,
        element_finder=element_finder,
    )

    detail_collector: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.scraping_service.ProductDetailCollectorImpl",
        product_details_extractor=product_details_extractor,
        page_navigator=page_navigator,
        process_detector=process_detector,
    )

    # Services
    scraping_service: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.scraping_service.ScrapingService",
        product_collector=product_collector,
        detail_collector=detail_collector,
    )

    # Mappers
    coffee_mapper: providers.Singleton = providers.Singleton(
        "src.infrastructure.mappers.coffee_mapper.CoffeeMapperImpl"
    )

    # Presenters
    markdown_config: providers.Singleton = providers.Singleton(
        MarkdownTableConfigFactory.create_coffee_table_config
    )

    presenter: providers.Singleton = providers.Singleton(
        "src.presentation.presenters.markdown_presenter.MarkdownPresenter",
        config=markdown_config,
    )

    # Scrapers
    coffee_scraper: providers.Singleton = providers.Singleton(
        "src.infrastructure.services.coffee_scraper.CoffeeScraper",
        web_client=web_client,
        scraping_service=scraping_service,
    )

    # Repositories
    coffee_repository: providers.Singleton = providers.Singleton(
        "src.infrastructure.repositories.coffee_repository_impl.CoffeeRepositoryImpl",
        coffee_scraper=coffee_scraper,
        coffee_mapper=coffee_mapper,
    )

    category_repository: providers.Singleton = providers.Singleton(
        "src.infrastructure.repositories.category_repository_impl.CategoryRepositoryImpl",
        client=web_client,
        base_url=config.provided.base_url,
    )

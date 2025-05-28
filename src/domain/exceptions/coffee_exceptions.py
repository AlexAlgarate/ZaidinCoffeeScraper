class CoffeeException(Exception):
    """Base exception for coffee domain"""

    pass


class CoffeeScrapingError(CoffeeException):
    """Raised when there's an error scraping coffee data"""

    pass


class InvalidPriceError(CoffeeException):
    """Raised when price cannot be parsed or is invalid"""

    pass


class InvalidWeightError(CoffeeException):
    """Raised when weight cannot be determined"""

    pass


class ProductNotFoundError(CoffeeException):
    """Raised when a product cannot be found"""

    pass


class DetailExtractionError(CoffeeException):
    """Raised when product details cannot be extracted"""

    pass


class PriceParsingError(Exception):
    def __init__(self, price_text: str, format_text: str, original: Exception):
        msg = f"Error parsing price '{price_text}' with format '{format_text}'"
        super().__init__(msg)
        self.original = original

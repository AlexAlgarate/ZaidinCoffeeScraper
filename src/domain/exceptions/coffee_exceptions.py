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
from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def info(self, msg: str, **kwargs): ...

    @abstractmethod
    def error(self, msg: str, **kwargs): ...

import logging

from src.application.interfaces.logger import ILogger


class LoggerImpl(ILogger):
    def __init__(self, name: str = "app"):
        self._logger = logging.getLogger(name)

    def info(self, msg: str, **kwargs):
        self._logger.info(msg, extra={"custom": kwargs})

    def error(self, msg: str, **kwargs):
        self._logger.error(msg, extra={"custom": kwargs})

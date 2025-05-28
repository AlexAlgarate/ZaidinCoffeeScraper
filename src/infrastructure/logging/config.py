import logging


def configure_logging(level=logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        format="%(levelname)s -- %(asctime)s -- %(name)s : %(message)s",
        datefmt="%y-%m-%d %H:%M:%S",
    )

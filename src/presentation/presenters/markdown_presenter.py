from typing import List
from domain.entities.coffee import Coffee
from application.interfaces.coffe_pressenter import CoffeePresenterInterface
from .configurations.configurations import TableConfig, ColumnConfig
from typing import List, Protocol
from domain.entities.coffee import Coffee
from application.interfaces.coffe_pressenter import CoffeePresenterInterface
from .configurations.configurations import TableConfig

class TableFormatter(Protocol):
    def format_header(self, config: TableConfig) -> List[str]: ...
    def format_row(self, config: TableConfig, data: any) -> str: ...

class MarkdownTableFormatter:
    def format_header(self, config: TableConfig) -> List[str]:
        headers = [f"{col.header}" for col in config.columns]
        alignments = [f":{config.separator * (col.width-2)}:" for col in config.columns]
        return [
            f"| {' | '.join(headers)} |",
            f"| {' | '.join(alignments)} |"
        ]

    def format_row(self, config: TableConfig, data: any) -> str:
        cells = []
        for col in config.columns:
            value = getattr(data, col.field)
            if callable(col.formatter):
                formatted = col.formatter(value)
            else:
                formatted = col.formatter.format(value)
            cells.append(formatted)
        return f"| {' | '.join(cells)} |"

class MarkdownPresenter(CoffeePresenterInterface):
    def __init__(self, 
                 config: TableConfig,
                 formatter: TableFormatter = None):
        self._config = config
        self._formatter = formatter or MarkdownTableFormatter()

    def present_coffees(self, coffees: List[Coffee]) -> str:
        sorted_coffees = sorted(coffees, key=lambda c: c.price_per_kg)
        return self._format_table(sorted_coffees)

    def _format_table(self, coffees: List[Coffee]) -> str:
        header = self._formatter.format_header(self._config)
        rows = [self._formatter.format_row(self._config, coffee) for coffee in coffees]
        return "\n".join([*header, *rows])
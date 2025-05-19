from dataclasses import dataclass
from typing import List


@dataclass
class ColumnConfig:
    header: str
    width: int
    field: str
    formatter: str = "{}"


@dataclass
class TableConfig:
    columns: List[ColumnConfig]
    separator: str = "-"

from .configurations import TableConfig, ColumnConfig


class MarkdownTableConfigFactory:
    @staticmethod
    def create_coffee_table_config() -> TableConfig:
        return TableConfig(
            columns=[
                ColumnConfig("Name", 30, "name", "**{}**"),
                ColumnConfig("Price", 12, "price_per_kg", "**{:.2f}€/kg**"),
                ColumnConfig("Process", 15, "process", "*{}*"),
            ],
            separator="-",
        )

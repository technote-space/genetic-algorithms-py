from task import AbstractAtariGaSettings


class GaSettings(AbstractAtariGaSettings):
    """
    Description:
    ------------
    GAの設定
    """

    @property
    def test_number(self) -> int:
        return 3

    @property
    def population_size(self) -> int:
        return 50

    @property
    def island_number(self) -> int:
        return 5

    @property
    def cultural_island_rate(self) -> float:
        return 0

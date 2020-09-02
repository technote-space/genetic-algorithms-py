from .. import AbstractGaSettings


class AbstractGymGaSettings(AbstractGaSettings):
    """
    Description:
    ------------
    Gym用のGAの設定
    """

    @property
    def test_number(self) -> int:
        return 10

    @property
    def population_size(self) -> int:
        return 100

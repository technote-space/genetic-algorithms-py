from .. import AbstractGaSettings


class AbstractGymGaSettings(AbstractGaSettings):
    """
    Description:
    ------------
    GAの設定
    """

    @property
    def test_number(self):
        return 10

    @property
    def population_size(self):
        return 100

    @property
    def node_count(self):
        return 50

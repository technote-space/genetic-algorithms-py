from target import AbstractGaSettings


class GaSettings(AbstractGaSettings):
    """
    Description:
    ------------
    GAの設定
    """

    @property
    def test_number(self):
        return 5

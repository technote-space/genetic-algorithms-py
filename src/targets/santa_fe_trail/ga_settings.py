from target import AbstractGaSettings


class GaSettings(AbstractGaSettings):
    """
    Description:
    ------------
    GAの設定
    """

    @property
    def node_count(self):
        return 50

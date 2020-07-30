from ..gym import AbstractGymGaSettings


class AbstractAtariGaSettings(AbstractGymGaSettings):
    """
    Description:
    ------------
    Atari用のGAの設定
    """

    @property
    def node_count(self) -> int:
        return 100

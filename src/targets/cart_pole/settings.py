from target import AbstractGymSettings


class Settings(AbstractGymSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self) -> str:
        return 'Cart Pole'

    @property
    def perception_number(self) -> int:
        return 4

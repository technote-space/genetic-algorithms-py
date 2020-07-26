from target import AbstractGymSettings


class Settings(AbstractGymSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self):
        return 'Cart Pole'

    @property
    def perception_number(self):
        return 4

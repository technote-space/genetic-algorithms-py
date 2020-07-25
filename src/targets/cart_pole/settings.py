from target import AbstractSettings


class Settings(AbstractSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self):
        return 'Cart Pole'

    @property
    def action_limit(self):
        return 200

    @property
    def perception_number(self):
        return 4

    @property
    def action_number(self):
        return 2

    @property
    def fps(self):
        return 30

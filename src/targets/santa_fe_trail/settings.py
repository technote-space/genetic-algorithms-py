from target import AbstractSettings
from .implements.helper import Helper


class Settings(AbstractSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self):
        return Helper.get_name()

    @property
    def action_limit(self):
        return Helper.get_energy()

    @property
    def perception_number(self):
        return 1

    @property
    def action_number(self):
        return 3

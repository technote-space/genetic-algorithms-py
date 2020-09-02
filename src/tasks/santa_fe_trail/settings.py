from task import AbstractSettings
from .implements.helper import Helper


class Settings(AbstractSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self) -> str:
        return Helper.get_name()

    @property
    def action_limit(self) -> int:
        return Helper.get_energy()

    @property
    def step_limit(self) -> int:
        return Helper.get_step_limit()

    @property
    def perception_number(self) -> int:
        return 1

    @property
    def action_number(self) -> int:
        return 3

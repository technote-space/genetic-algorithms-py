from task import AbstractGymSettings


class Settings(AbstractGymSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self) -> str:
        return 'Mountain Car'

    @property
    def step_limit(self) -> int:
        return self.action_limit * 10

    @property
    def perception_number(self) -> int:
        return 10

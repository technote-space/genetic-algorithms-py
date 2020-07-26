from target import AbstractGymSettings


class Settings(AbstractGymSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self):
        return 'Mountain Car'

    @property
    def step_limit(self):
        return self.action_limit * 10

    @property
    def perception_number(self):
        return 10

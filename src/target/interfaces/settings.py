from abc import ABCMeta, abstractmethod


class ISettings(metaclass=ABCMeta):
    """
    Description:
    ------------
    設定のinterface
    """

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def gym_id(self):
        pass

    @property
    @abstractmethod
    def action_limit(self):
        pass

    @property
    @abstractmethod
    def step_limit(self):
        pass

    @property
    @abstractmethod
    def perception_number(self):
        pass

    @property
    @abstractmethod
    def action_number(self):
        pass

    @property
    @abstractmethod
    def fps(self):
        pass

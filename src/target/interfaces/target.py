from abc import ABCMeta, abstractmethod


class ITarget(metaclass=ABCMeta):
    """
    Description:
    ------------
    学習対象のinterface
    """

    @property
    @abstractmethod
    def step(self):
        pass

    @property
    @abstractmethod
    def action_step(self):
        pass

    @property
    @abstractmethod
    def settings(self):
        pass

    @property
    @abstractmethod
    def ga_settings(self):
        pass

    @property
    @abstractmethod
    def has_reached(self):
        pass

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def action(self, index):
        pass

    @abstractmethod
    def perceive(self, index):
        pass

    @abstractmethod
    def get_action_expression(self, index):
        pass

    @abstractmethod
    def get_perceive_expression(self, index):
        pass

    @abstractmethod
    def get_fitness(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def render(self):
        pass

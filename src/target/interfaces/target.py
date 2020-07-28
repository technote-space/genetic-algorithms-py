from abc import ABCMeta, abstractmethod


class ITarget(metaclass=ABCMeta):
    """
    Description:
    ------------
    学習対象のinterface
    """

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def is_player(self):
        pass

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
    def action(self, index):
        pass

    @abstractmethod
    def perceive(self, index):
        pass

    @abstractmethod
    def get_fitness(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def on_player(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def get_action_expression(self, index):
        pass

    @abstractmethod
    def get_perceive_expression(self, index, observation_name):
        pass

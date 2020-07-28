from target import AbstractGymTarget
from .settings import Settings
from .ga_settings import GaSettings


class MountainCar(AbstractGymTarget):
    """
    Description:
    ------------
    Mountain Car
    """

    def __init__(self):
        super().__init__('MountainCar-v0', Settings, GaSettings)
        self.____perception_settings = [
            (0, -1.2, -0.9),
            (0, -0.9, -0.6),
            (0, -0.6, -0.3),
            (0, -0.3, 0),
            (0, 0, 0.3),
            (0, 0.3, 0.6),
            (1, -0.07, -0.035),
            (1, -0.035, 0),
            (1, 0, 0.035),
            (1, 0.035, 0.07),
        ]
        self.__perceptions = {}
        for index, setting in enumerate(self.____perception_settings):
            self.__perceptions[index] = self.__get_perceive_function(setting[0], setting[1], setting[2])
        self.__max_position = 0

    @staticmethod
    def __perceive(value, left, right):
        return left <= value < right

    def __get_perceive_function(self, target, left, right):
        return lambda: self.__perceive(self.observation[target], left, right)

    def _perform_perceive(self, index):
        return self.__perceptions[index]()

    def _perform_get_fitness(self):
        self.__max_position = max(self.__max_position, self.observation[0])
        if self._has_reached_step or self._has_reached_action_step or self.is_player:
            return self.__max_position / 0.5

        return 1

    def get_perceive_expression(self, index, observation_name):
        setting = self.____perception_settings[index]
        return f'{setting[1]} <= {observation_name}[{setting[0]}] < {setting[2]}'

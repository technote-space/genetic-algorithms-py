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
        self.__perceptions = {
            0: self.__perceive_position(-1.2, -0.9),
            1: self.__perceive_position(-0.9, -0.6),
            2: self.__perceive_position(-0.6, -0.3),
            3: self.__perceive_position(-0.3, 0),
            4: self.__perceive_position(0, 0.3),
            5: self.__perceive_position(0.3, 0.6),
            6: self.__perceive_velocity(-0.07, -0.035),
            7: self.__perceive_velocity(-0.035, 0),
            8: self.__perceive_velocity(0, 0.035),
            9: self.__perceive_velocity(0.035, 0.07),
        }
        self.__max_position = 0

    @staticmethod
    def __perceive(value, left, right):
        return left <= value < right

    def __perceive_position(self, left, right):
        return lambda: self.__perceive(self.observation[0], left, right)

    def __perceive_velocity(self, left, right):
        return lambda: self.__perceive(self.observation[1], left, right)

    def _perform_perceive(self, index):
        return self.__perceptions[index]()

    def _perform_get_fitness(self):
        self.__max_position = max(self.__max_position, self.observation[0])
        if self._has_reached_step or self._has_reached_action_step or self.is_player:
            return self.__max_position / 0.5

        return 1

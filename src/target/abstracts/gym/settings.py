from gym.spaces import Discrete
from abc import abstractmethod
from .. import AbstractSettings


class AbstractGymSettings(AbstractSettings):
    """
    Description:
    ------------
    Gym用の設定の基底クラス
    """

    def __init__(self, env):
        self.__env = env
        self.__action_number = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    def action_limit(self):
        return self.__env.spec.max_episode_steps

    @property
    @abstractmethod
    def perception_number(self):
        pass

    @property
    def action_number(self):
        if self.__action_number is None:
            if type(self.__env.action_space) is Discrete:
                self.__action_number = self.__env.action_space.n

            else:
                raise Exception('Not implemented')

        return self.__action_number

    @property
    def fps(self):
        return 30

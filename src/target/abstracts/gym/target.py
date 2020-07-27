import gym
from abc import abstractmethod
from .. import AbstractTarget


class AbstractGymTarget(AbstractTarget):
    """
    Description:
    ------------
    Gym用の学習対象の基底クラス
    """

    def __init__(self, gym_id, settings, ga_settings):
        super().__init__()

        self.__env = gym.make(gym_id)
        self.__settings = settings(gym_id, self.__env)
        self.__ga_settings = ga_settings()
        self.__observation = self.__env.reset()
        self.__reward = 0

    def __del__(self):
        if self.__env:
            self.__env.close()

    @property
    def settings(self):
        return self.__settings

    @property
    def ga_settings(self):
        return self.__ga_settings

    @property
    def observation(self):
        return self.__observation

    # noinspection PyMethodMayBeStatic
    def _get_action(self, index):
        return index

    def _perform_action(self, index):
        observation, reward, done, _ = self.__env.step(self._get_action(index))
        self.__observation = observation
        self.__reward += reward

        if done:
            self._on_finished()

    @abstractmethod
    def _perform_perceive(self, index):
        pass

    # noinspection PyMethodMayBeStatic
    def _correction_fitness(self):
        return 0

    def _perform_get_fitness(self):
        fitness = self.__reward / self.__env.spec.reward_threshold
        if fitness > 1:
            surplus = fitness - 1
            fitness = 1 + surplus * 0.01
        return fitness + self._correction_fitness()

    def _perform_render(self):
        self.__env.render()

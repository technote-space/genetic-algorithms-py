import gym
from target import AbstractTarget
from .settings import Settings
from .ga_settings import GaSettings


class CartPole(AbstractTarget):
    """
    Description:
    ------------
    Cart Pole
    """

    def __init__(self):
        super().__init__()

        self.__settings = Settings()
        self.__ga_settings = GaSettings()
        self.__env = gym.make('CartPole-v1')
        self.__observe = self.__env.reset()

    def __del__(self):
        if self.__env:
            self.__env.close()

    @property
    def settings(self):
        return self.__settings

    @property
    def ga_settings(self):
        return self.__ga_settings

    def clone(self):
        return CartPole()

    def _perform_action(self, index):
        observe, reward, done, _ = self.__env.step(index)  # 0 or 1
        self.__observe = observe

        if done:
            self._on_finished()

    def _perform_perceive(self, index):
        return self.__observe[index] < 0

    def _perform_get_fitness(self):
        return self.action_step / self.settings.action_limit + (1 - abs(self.__observe[0]) / 2.4) * 0.01

    def _perform_render(self):
        self.__env.render()

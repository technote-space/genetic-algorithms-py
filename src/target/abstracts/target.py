import os
from abc import abstractmethod
from ..interfaces import ITarget


class AbstractTarget(ITarget):
    """
    Description:
    ------------
    学習対象の基底クラス
    """

    def __init__(self):
        self.__step = 0
        self.__action_step = 0
        self.__has_finished = False
        self.__is_player = False

    @property
    def is_player(self):
        return self.__is_player

    @property
    def step(self):
        return self.__step

    @property
    def action_step(self):
        return self.__action_step

    @property
    @abstractmethod
    def settings(self):
        pass

    @property
    @abstractmethod
    def ga_settings(self):
        pass

    @property
    def step_limit(self):
        return self.settings.step_limit

    @property
    def _has_reached_action_step(self):
        return self.action_step >= self.settings.action_limit

    @property
    def _has_reached_step(self):
        return self.step >= self.settings.step_limit

    @property
    def has_reached(self):
        return self.__has_finished or self._has_reached_action_step or self._has_reached_step

    def _on_finished(self):
        self.__has_finished = True

    @abstractmethod
    def clone(self):
        pass

    def action(self, index):
        if self.has_reached:
            raise Exception('The step has reached to limit')

        self.__step += 1
        self.__action_step += 1
        self._perform_action(index)

    @abstractmethod
    def _perform_action(self, index):
        pass

    def perceive(self, index):
        if self.has_reached:
            raise Exception('The step has reached to limit')

        self.__step += 1
        return self._perform_perceive(index)

    @abstractmethod
    def _perform_perceive(self, index):
        pass

    def get_action_expression(self, index):
        return f'行動{index}'

    def get_perceive_expression(self, index):
        return f'知覚{index}'

    def get_fitness(self):
        fitness = self._perform_get_fitness()
        if fitness >= 1:
            return fitness + 1.0 / (self.action_step + self.step)

        return fitness

    def on_player(self):
        self.__is_player = True

    @abstractmethod
    def _perform_get_fitness(self):
        pass

    def draw(self):
        pass

    def _perform_render(self):
        self.draw()

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        self._perform_render()

        print(f'{self.get_fitness():.3f}', self.step, self.action_step)

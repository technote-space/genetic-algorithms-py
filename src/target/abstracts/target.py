import os
from abc import abstractmethod
from typing import Optional
from ..interfaces import ITarget, ISettings, IGaSettings


class AbstractTarget(ITarget):
    """
    Description:
    ------------
    学習対象の基底クラス
    """

    __name: Optional[str]
    __step: int
    __action_step: int
    __has_finished: bool
    __is_player: bool

    def __init__(self) -> None:
        self.__name = None
        self.__step = 0
        self.__action_step = 0
        self.__has_finished = False
        self.__is_player = False

    @property
    def name(self) -> Optional[str]:
        return self.__name

    def close(self) -> None:
        pass

    @property
    def is_player(self) -> bool:
        return self.__is_player

    @property
    def step(self) -> int:
        return self.__step

    @property
    def action_step(self) -> int:
        return self.__action_step

    @property
    @abstractmethod
    def settings(self) -> ISettings:
        pass

    @property
    @abstractmethod
    def ga_settings(self) -> IGaSettings:
        pass

    @property
    def _has_reached_action_step(self) -> bool:
        return self.action_step >= self.settings.action_limit

    @property
    def _has_reached_step(self) -> bool:
        return self.step >= self.settings.step_limit

    @property
    def has_reached(self) -> bool:
        return self.__has_finished or self._has_reached_action_step or self._has_reached_step

    def _on_finished(self) -> None:
        self.__has_finished = True

    def action(self, index: int, is_start: bool = False) -> None:
        if self.has_reached:
            raise Exception('The step has reached to limit')

        self.__step += 1
        self.__action_step += 1
        self._perform_action(index, is_start)

    @abstractmethod
    def _perform_action(self, index: int, is_start: bool) -> None:
        pass

    def perceive(self, index: int) -> bool:
        if self.has_reached:
            raise Exception('The step has reached to limit')

        self.__step += 1
        return self._perform_perceive(index)

    @abstractmethod
    def _perform_perceive(self, index: int) -> bool:
        pass

    def get_fitness(self) -> float:
        fitness = self._perform_get_fitness()
        if fitness >= 1:
            return fitness + 1.0 / (self.action_step + self.step)

        return fitness

    def set_name(self, name: str) -> None:
        self.__name = name

    def on_player(self) -> None:
        self.__is_player = True

    @abstractmethod
    def _perform_get_fitness(self) -> float:
        pass

    def draw(self) -> None:
        pass

    def _perform_render(self) -> None:
        self.draw()

    def render(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        self._perform_render()

        print(f'{self.get_fitness():.3f}', self.step, self.action_step)

    def get_action_expression(self, index: int, is_start: bool = False) -> str:
        raise Exception('Not implemented.')

    def get_perceive_expression(self, index: int, observation_name: str) -> str:
        raise Exception('Not implemented.')

    def get_finished_expression(self, done_name: str, observation_name: str) -> str:
        return f'{done_name}'

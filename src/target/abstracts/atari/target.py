from abc import abstractmethod
from typing import Any
from ..gym import AbstractGymTarget


class AbstractAtariTarget(AbstractGymTarget):
    """
    Description:
    ------------
    Atari用の学習対象の基底クラス
    """

    def _get_action(self, index: int, is_start: bool) -> Any:  # type: ignore
        if index < 1 or is_start:
            return index

        return index + 1

    @abstractmethod
    def _perform_perceive(self, index: int) -> bool:
        pass

    def get_action_expression(self, index: int, is_start: bool = False) -> str:
        if index < 1 or is_start:
            return f'{index}'

        return f'{index + 1}'

    @abstractmethod
    def get_perceive_expression(self, index: int, observation_name: str) -> str:
        pass

    def _correction_fitness(self) -> float:
        return self.action_step / self.settings.action_limit * 0.01

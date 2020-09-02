from abc import abstractmethod
from typing import Optional, List
from ..interfaces import ISettings


class AbstractSettings(ISettings):
    """
    Description:
    ------------
    設定の基底クラス
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def gym_id(self) -> Optional[str]:
        return None

    @property
    @abstractmethod
    def action_limit(self) -> int:
        pass

    @property
    def step_limit(self) -> int:
        return self.action_limit * 5

    @property
    @abstractmethod
    def perception_number(self) -> int:
        pass

    @property
    @abstractmethod
    def action_number(self) -> int:
        pass

    @property
    def fps(self) -> float:
        return 8

    @property
    def action_frame(self) -> int:
        return 1

    @property
    def start_action_index(self) -> Optional[List[int]]:
        return None

    @property
    def start_action_index_expression(self) -> Optional[List[str]]:
        if self.start_action_index is not None:
            return [f'self.__context.action({index}, True)' for index in self.start_action_index]
        return []

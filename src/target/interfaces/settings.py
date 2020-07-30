from abc import ABCMeta, abstractmethod
from typing import Optional, List


class ISettings(metaclass=ABCMeta):
    """
    Description:
    ------------
    設定のinterface
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def gym_id(self) -> Optional[str]:
        pass

    @property
    @abstractmethod
    def action_limit(self) -> int:
        pass

    @property
    @abstractmethod
    def step_limit(self) -> int:
        pass

    @property
    @abstractmethod
    def perception_number(self) -> int:
        pass

    @property
    @abstractmethod
    def action_number(self) -> int:
        pass

    @property
    @abstractmethod
    def fps(self) -> float:
        pass

    @property
    @abstractmethod
    def action_frame(self) -> int:
        pass

    @property
    @abstractmethod
    def start_action_index(self) -> Optional[List[int]]:
        pass

    @property
    @abstractmethod
    def start_action_index_expression(self) -> Optional[List[str]]:
        pass

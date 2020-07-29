from abc import ABCMeta, abstractmethod
from typing import Optional
from .settings import ISettings
from .ga_settings import IGaSettings


class ITarget(metaclass=ABCMeta):
    """
    Description:
    ------------
    学習対象のinterface
    """

    @property
    @abstractmethod
    def name(self) -> Optional[str]:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @property
    @abstractmethod
    def is_player(self) -> bool:
        pass

    @property
    @abstractmethod
    def step(self) -> int:
        pass

    @property
    @abstractmethod
    def action_step(self) -> int:
        pass

    @property
    @abstractmethod
    def settings(self) -> ISettings:
        pass

    @property
    @abstractmethod
    def ga_settings(self) -> IGaSettings:
        pass

    @property
    @abstractmethod
    def has_reached(self) -> bool:
        pass

    @abstractmethod
    def action(self, index: int) -> None:
        pass

    @abstractmethod
    def perceive(self, index: int) -> bool:
        pass

    @abstractmethod
    def get_fitness(self) -> float:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def on_player(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def get_action_expression(self, index: int) -> str:
        pass

    @abstractmethod
    def get_perceive_expression(self, index: int, observation_name: str) -> str:
        pass

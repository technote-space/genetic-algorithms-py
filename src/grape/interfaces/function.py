from abc import ABCMeta, abstractmethod
from typing import Iterable


class IFunction(metaclass=ABCMeta):
    """
    Description:
    ------------
    関数のinterface
    """

    @abstractmethod
    def execute(self, c1: int, c2: int, context: 'IContext') -> None:
        pass

    @abstractmethod
    def get_possible_connections(self, c1: int, c2: int, context: 'IContext') -> Iterable[int]:
        pass

    @abstractmethod
    def programming(self, c1: int, c2: int, context: 'IContext') -> object:
        pass


from .context import IContext  # noqa: E402

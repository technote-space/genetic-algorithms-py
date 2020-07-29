from abc import ABCMeta, abstractmethod
from typing import Iterable
from .block import IFuncBlock


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
    def programming(self, c1: int, c2: int, context: 'IContext') -> IFuncBlock:
        pass


from .context import IContext  # noqa: E402

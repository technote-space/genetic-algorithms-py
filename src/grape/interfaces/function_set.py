from abc import ABCMeta, abstractmethod
from typing import List
from .function import IFunction


class IFunctionSet(metaclass=ABCMeta):
    """
    Description:
    ------------
    関数セットのinterface
    """

    @property
    @abstractmethod
    def functions(self) -> List[IFunction]:
        pass

    @property
    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def get_function(self, index: int) -> IFunction:
        pass

    @abstractmethod
    def add(self, func: IFunction) -> None:
        pass

    @abstractmethod
    def get_random_index(self) -> int:
        pass

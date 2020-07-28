from abc import ABCMeta, abstractmethod
from typing import List
from .algorithm import IAlgorithm


class IMigration(metaclass=ABCMeta):
    """
    Description:
    ------------
    移住のinterface
    """

    __rate: float
    __interval: int

    def __init__(self, rate: float, interval: int) -> None:
        self.__rate = rate
        self.__interval = interval

    @property
    def rate(self) -> float:
        return self.__rate

    @property
    def interval(self) -> int:
        return self.__interval

    @abstractmethod
    def init(self) -> None:
        pass

    @abstractmethod
    def get_count(self, algorithm: IAlgorithm) -> int:
        pass

    @abstractmethod
    def get_destinations(self, algorithm: IAlgorithm) -> List[int]:
        pass

    @abstractmethod
    def migrate(self, algorithm: IAlgorithm) -> None:
        pass

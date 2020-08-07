from abc import ABCMeta, abstractmethod
from typing import List
from .chromosome import IChromosome


class ICrossover(metaclass=ABCMeta):
    """
    Description:
    ------------
    交叉のinterface
    """

    __probability: float
    __parents_number: int
    __children_number: int

    def __init__(self, probability: float, parents_number: int, children_number: int) -> None:
        self.__probability = probability
        self.__parents_number = parents_number
        self.__children_number = children_number

    @property
    def probability(self) -> float:
        return self.__probability

    @property
    def parents_number(self) -> int:
        return self.__parents_number

    @property
    def children_number(self) -> int:
        return self.__children_number

    @abstractmethod
    def cross(self, parents: List[IChromosome]) -> List[IChromosome]:
        pass

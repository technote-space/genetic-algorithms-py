from abc import ABCMeta, abstractmethod
from typing import List
from .chromosome import IChromosome


class IPopulation(metaclass=ABCMeta):
    """
    Description:
    ------------
    人口のinterface
    """

    __size: int
    __adam: IChromosome

    def __init__(self, size: int, adam: IChromosome) -> None:
        self.__size = size
        self.__adam = adam

    @property
    def size(self) -> int:
        return self.__size

    @property
    def adam(self) -> IChromosome:
        return self.__adam

    @property
    @abstractmethod
    def chromosomes(self) -> List[IChromosome]:
        pass

    @abstractmethod
    def init(self) -> None:
        pass

    @abstractmethod
    def update(self, chromosomes: List[IChromosome]) -> None:
        pass

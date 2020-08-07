from abc import ABCMeta, abstractmethod
from .chromosome import IChromosome


class IMutation(metaclass=ABCMeta):
    """
    Description:
    ------------
    突然変異のinterface
    """

    __probability: float

    def __init__(self, probability: float) -> None:
        self.__probability = probability

    @property
    def probability(self) -> float:
        return self.__probability

    @abstractmethod
    def mutate(self, chromosome: IChromosome) -> None:
        pass

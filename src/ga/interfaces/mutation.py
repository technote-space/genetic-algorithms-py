from abc import ABCMeta, abstractmethod
from .chromosome import IChromosome


class IMutation(metaclass=ABCMeta):
    """
    Description:
    ------------
    突然変異のinterface
    """

    @abstractmethod
    def mutate(self, chromosome: IChromosome, probability: float) -> None:
        pass

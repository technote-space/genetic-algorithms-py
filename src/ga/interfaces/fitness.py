from abc import ABCMeta, abstractmethod
from .chromosome import IChromosome


class IFitness(metaclass=ABCMeta):
    """
    Description:
    ------------
    適応度のinterface
    """

    @abstractmethod
    def evaluate(self, chromosome: IChromosome) -> None:
        pass

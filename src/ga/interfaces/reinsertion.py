from abc import ABCMeta, abstractmethod
from typing import List
from .chromosome import IChromosome


class IReinsertion(metaclass=ABCMeta):
    """
    Description:
    ------------
    挿入のinterface
    """

    @abstractmethod
    def select(self, population: List[IChromosome], offspring: List[IChromosome], parents: List[IChromosome]) -> List[IChromosome]:
        pass

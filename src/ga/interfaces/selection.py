from abc import ABCMeta, abstractmethod
from typing import List, Tuple
from .chromosome import IChromosome


class ISelection(metaclass=ABCMeta):
    """
    Description:
    ------------
    選択のinterface
    """

    @abstractmethod
    def select(self, chromosomes: List[IChromosome]) -> Tuple[List[IChromosome], List[IChromosome]]:
        pass

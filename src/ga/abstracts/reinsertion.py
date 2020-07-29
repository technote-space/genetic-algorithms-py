from abc import abstractmethod
from typing import List
from ..interfaces import IReinsertion, IChromosome


class AbstractReinsertion(IReinsertion):
    """
    Description:
    ------------
    挿入の基底クラス
    """

    @abstractmethod
    def select(self, population: List[IChromosome], offspring: List[IChromosome], parents: List[IChromosome], size: int) -> List[IChromosome]:
        pass

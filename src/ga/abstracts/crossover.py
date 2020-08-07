from abc import abstractmethod
from typing import List, Iterable
from ..interfaces import ICrossover, IChromosome


class AbstractCrossover(ICrossover):
    """
    Description:
    ------------
    交叉の基底クラス
    """

    def cross(self, parents: List[IChromosome]) -> List[IChromosome]:
        if len(parents) != self.parents_number:
            raise Exception('Length is not same.')

        offspring = list(self._perform_cross(parents))
        if len(offspring) != self.children_number:
            raise Exception('Length is not same')

        return offspring

    @abstractmethod
    def _perform_cross(self, parents: List[IChromosome]) -> Iterable[IChromosome]:
        pass

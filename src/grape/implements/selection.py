import copy
from typing import List, Tuple
from ga import AbstractSelection, IChromosome


class Selection(AbstractSelection):
    """
    Description:
    ------------
    選択クラス
    """

    def select(self, chromosomes: List[IChromosome]) -> Tuple[List[IChromosome], List[IChromosome]]:
        population = copy.copy(chromosomes)
        parent1 = self._take_by_order(population)
        parent2 = self._take_by_order(population)
        return [parent1, parent2], population

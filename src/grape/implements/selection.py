import copy
from ga import AbstractSelection


class Selection(AbstractSelection):
    """
    Description:
    ------------
    選択クラス
    """

    def select(self, chromosomes):
        population = copy.copy(chromosomes)
        parent1 = self._take_by_order(population)
        parent2 = self._take_by_order(population)
        return [parent1, parent2], population

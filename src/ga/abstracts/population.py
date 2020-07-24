import copy
from ..interfaces import IPopulation


class AbstractPopulation(IPopulation):
    """
    Description:
    ------------
    人口の基底クラス
    """

    def __init__(self, size, adam):
        super().__init__(size, adam)

        self._chromosomes = []

    @property
    def chromosomes(self):
        return self._chromosomes

    def init(self):
        self._chromosomes = []
        for _ in range(self.size):
            self._chromosomes.append(self.adam.create_new())
        self._perform_init()

    def _perform_init(self):
        pass

    def update(self, chromosomes):
        if self.size != len(chromosomes):
            raise Exception('Population size does not match the setting.')

        self._chromosomes = copy.copy(chromosomes)

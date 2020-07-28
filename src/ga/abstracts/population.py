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

        self.__chromosomes = []

    @property
    def chromosomes(self):
        return self.__chromosomes

    def init(self):
        self.__chromosomes = []
        for _ in range(self.size):
            self.__chromosomes.append(self.adam.create_new())
        self._perform_init()

    def _perform_init(self):
        pass

    def update(self, chromosomes):
        if self.size != len(chromosomes):
            raise Exception('Population size does not match the setting.')

        self.__chromosomes = copy.copy(chromosomes)

import copy
from typing import List
from ..interfaces import IPopulation, IChromosome


class AbstractPopulation(IPopulation):
    """
    Description:
    ------------
    人口の基底クラス
    """

    __chromosomes: List[IChromosome]

    def __init__(self, size: int, adam: IChromosome) -> None:
        super().__init__(size, adam)

        self.__chromosomes = []

    @property
    def chromosomes(self) -> List[IChromosome]:
        return self.__chromosomes

    def init(self) -> None:
        self.__chromosomes = []
        for _ in range(self.size):
            self.__chromosomes.append(self.adam.create_new())
        self._perform_init()

    def _perform_init(self) -> None:
        pass

    def update(self, chromosomes: List[IChromosome]) -> None:
        if self.size != len(chromosomes):
            raise Exception('Population size does not match the setting.')

        self.__chromosomes = copy.copy(chromosomes)

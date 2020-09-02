from typing import List, Iterable
from ga import AbstractCrossover, IChromosome
from ...genotype import Genotype
from ....interfaces import IFunctionSet


class CulturalCrossover(AbstractCrossover):
    """
    Description:
    ------------
    異文化型島モデルの交叉クラス
    """

    __pool: List[IChromosome]

    def __init__(self, node_count: int, functions: IFunctionSet) -> None:
        super().__init__(0, 2, 2)

        self.__pool = []
        for _ in range(self.children_number):
            self.__pool.append(Genotype(node_count, functions))

    def _perform_cross(self, parents: List[IChromosome]) -> Iterable[IChromosome]:
        for index in range(len(parents)):
            self.__pool[index].copy_from(parents[index])

        return self.__pool

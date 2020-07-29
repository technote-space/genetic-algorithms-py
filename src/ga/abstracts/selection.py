import math
import random
from functools import reduce
from abc import abstractmethod
from typing import List, Tuple, Callable
from ..interfaces import ISelection, IChromosome


class AbstractSelection(ISelection):
    """
    Description:
    ------------
    選択の基底クラス
    """

    @abstractmethod
    def select(self, chromosomes: List[IChromosome]) -> Tuple[List[IChromosome], List[IChromosome]]:
        pass

    @staticmethod
    def _take_random(chromosomes: List[IChromosome]) -> IChromosome:
        return chromosomes.pop(math.floor(random.random() * len(chromosomes)))

    @staticmethod
    def _take_by_fitness(chromosomes: List[IChromosome]) -> IChromosome:
        lambda_func: Callable[[float, IChromosome], float] = lambda acc, c: acc + max(0.0, c.fitness)
        sum_fitness: float = reduce(lambda_func, chromosomes, 0.0)
        cumulative: float = 0
        rand = random.random() * sum_fitness

        for index in range(len(chromosomes)):
            chromosome = chromosomes[index]
            cumulative += max(0.0, chromosome.fitness)
            if cumulative >= rand:
                return chromosomes.pop(index)

        raise Exception('Unexpected error')

    @staticmethod
    def _take_by_order(chromosomes: List[IChromosome]) -> IChromosome:
        sum_value = len(chromosomes) * (len(chromosomes) + 1) / 2
        cumulative = 0
        rand = random.random() * sum_value

        for index in range(len(chromosomes)):
            cumulative += len(chromosomes) - index
            if cumulative >= rand:
                return chromosomes.pop(index)

        raise Exception('Unexpected error')

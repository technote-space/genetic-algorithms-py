import copy
import random
from functools import reduce
from typing import List, Callable
from ga import AbstractReinsertion, IChromosome


class MggReinsertion(AbstractReinsertion):
    """
    Description:
    ------------
    Mggの挿入クラス
    """

    def select(self, population: List[IChromosome], offspring: List[IChromosome], parents: List[IChromosome]) -> List[IChromosome]:
        sorted_offspring = sorted(offspring + parents, key=lambda x: x.fitness, reverse=True)

        selected = copy.copy(population)
        selected.append(sorted_offspring.pop(0))
        selected.append(self._take(sorted_offspring))

        return selected

    @staticmethod
    def _take(chromosomes: List[IChromosome]) -> IChromosome:
        lambda_func: Callable[[float, IChromosome], float] = lambda acc, c: acc + max(0.0, c.fitness)
        sum_fitness: float = reduce(lambda_func, chromosomes, 0.0)
        cumulative: float = 0
        rand = random.random() * sum_fitness

        for chromosome in chromosomes:
            cumulative += max(0.0, chromosome.fitness)
            if cumulative >= rand:
                return chromosome

        raise Exception('Unexpected error')

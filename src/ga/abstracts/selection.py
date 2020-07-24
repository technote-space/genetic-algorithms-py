import math
import random
from functools import reduce
from abc import abstractmethod
from ..interfaces import ISelection


class AbstractSelection(ISelection):
    """
    Description:
    ------------
    選択の基底クラス
    """

    @abstractmethod
    def select(self, chromosomes):
        pass

    @staticmethod
    def _take_random(chromosomes):
        return chromosomes.pop(math.floor(random.random() * len(chromosomes)))

    @staticmethod
    def _take_by_fitness(chromosomes):
        sum_fitness = reduce(lambda acc, c: acc + max(0, c.fitness), chromosomes, 0)
        cumulative = 0
        rand = random.random() * sum_fitness

        for index in range(len(chromosomes)):
            chromosome = chromosomes[index]
            cumulative += max(0, chromosome.fitness)
            if cumulative >= rand:
                return chromosomes.pop(index)

        raise Exception('Unexpected error')

    @staticmethod
    def _take_by_order(chromosomes):
        sum_value = len(chromosomes) * (len(chromosomes) + 1) / 2
        cumulative = 0
        rand = random.random() * sum_value

        for index in range(len(chromosomes)):
            cumulative += len(chromosomes) - index
            if cumulative >= rand:
                return chromosomes.pop(index)

        raise Exception('Unexpected error')

import copy
import random
from functools import reduce
from ga import AbstractReinsertion


class MggReinsertion(AbstractReinsertion):
    """
    Description:
    ------------
    Mggの挿入クラス
    """

    def select(self, population, offspring, parents, size):
        sorted_offspring = sorted(offspring + parents, key=lambda x: x.fitness, reverse=True)

        selected = copy.copy(population)
        selected.append(sorted_offspring.pop(0))
        selected.append(self._take(sorted_offspring))

        return selected

    @staticmethod
    def _take(chromosomes):
        sum_fitness = reduce(lambda acc, c: acc + max(0, c.fitness), chromosomes, 0)
        cumulative = 0
        rand = random.random() * sum_fitness

        for chromosome in chromosomes:
            cumulative += max(0, chromosome.fitness)
            if cumulative >= rand:
                return chromosome

        raise Exception('Unexpected error')

import copy
import math
import random
from ..interfaces import IMigration


class AbstractMigration(IMigration):
    """
    Description:
    ------------
    移住の基底クラス
    """

    def __init__(self, rate, interval):
        super().__init__(rate, interval)

        self.__prev = 0
        self.__time = 0

    def init(self):
        self.__prev = 0
        self.__time = 0

    def get_count(self, algorithm):
        return algorithm.offspring_number

    def get_destinations(self, algorithm):
        island_number = len(algorithm.islands)
        time = self.__time % (island_number - 1)
        return list(map(lambda num: (num + 1 + time) % island_number, range(island_number)))

    @staticmethod
    def __take_random_chromosomes(chromosomes, count):
        results = []
        for _ in range(count):
            results.append(chromosomes.pop(math.floor(random.random() * len(chromosomes))))

        return results

    def __get_take_count(self, chromosomes):
        return math.ceil(len(chromosomes) * self.rate)

    def __split_chromosomes(self, chromosomes, count):
        population = copy.copy(chromosomes)
        emigrants = self.__take_random_chromosomes(population, count)
        return population, emigrants

    def _perform_migrate(self, algorithm):
        destination = self.get_destinations(algorithm)
        islands = list(
            map(
                lambda x: self.__split_chromosomes(
                    x.population.chromosomes,
                    self.__get_take_count(x.population.chromosomes)
                ), algorithm.islands
            )
        )
        for index in range(len(islands)):
            islands[destination[index]][0].extend(islands[index][1])

        for index, island in enumerate(algorithm.islands):
            island.population.update(islands[index][0])

    def migrate(self, algorithm):
        if len(algorithm.islands) <= 1:
            return

        count = self.get_count(algorithm)
        if count >= self.__prev + self.interval:
            self.__prev = count
            self._perform_migrate(algorithm)
            self.__time += 1

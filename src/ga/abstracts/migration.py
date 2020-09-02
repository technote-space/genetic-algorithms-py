import copy
import math
import random
from typing import List, Tuple, Callable
from ..interfaces import IMigration, IAlgorithm, IChromosome, IIsland


class AbstractMigration(IMigration):
    """
    Description:
    ------------
    移住の基底クラス
    """

    __prev: int
    __time: int

    def __init__(self, rate: float, interval: int) -> None:
        super().__init__(rate, interval)
        self.init()

    def init(self) -> None:
        self.__prev = 0
        self.__time = 0

    def get_count(self, algorithm: IAlgorithm) -> int:
        return algorithm.offspring_number

    def get_destinations(self, algorithm: IAlgorithm) -> List[int]:
        island_number = len(algorithm.islands)
        time = self.__time % (island_number - 1)
        lambda_func: Callable[[int], int] = lambda num: (num + 1 + time) % island_number
        return list(map(lambda_func, range(island_number)))

    @staticmethod
    def __take_random_chromosomes(chromosomes: List[IChromosome], count: int) -> List[IChromosome]:
        results = []
        for _ in range(count):
            results.append(chromosomes.pop(math.floor(random.random() * len(chromosomes))))

        return results

    def __get_take_count(self, chromosomes: List[IChromosome]) -> int:
        return math.ceil(len(chromosomes) * self.rate)

    def __split_chromosomes(self, chromosomes: List[IChromosome], count: int) -> Tuple[List[IChromosome], List[IChromosome]]:
        population = copy.copy(chromosomes)
        emigrants = self.__take_random_chromosomes(population, count)
        return population, emigrants

    def _perform_migrate(self, algorithm: IAlgorithm) -> None:
        destination = self.get_destinations(algorithm)
        lambda_func: Callable[[IIsland], Tuple[List[IChromosome], List[IChromosome]]] = lambda x: self.__split_chromosomes(
            x.population.chromosomes,
            self.__get_take_count(x.population.chromosomes)
        )
        islands = list(map(lambda_func, algorithm.islands))
        for index in range(len(islands)):
            islands[destination[index]][0].extend(islands[index][1])

        for index, island in enumerate(algorithm.islands):
            island.population.update(islands[index][0])

    def migrate(self, algorithm: IAlgorithm) -> None:
        if len(algorithm.islands) <= 1:
            return

        count = self.get_count(algorithm)
        if count >= self.__prev + self.interval:
            self.__prev = count
            self._perform_migrate(algorithm)
            self.__time += 1

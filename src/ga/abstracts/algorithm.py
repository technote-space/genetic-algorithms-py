from abc import abstractmethod
from functools import reduce
from concurrent.futures import ThreadPoolExecutor
from ..interfaces import IAlgorithm


class AbstractAlgorithm(IAlgorithm):
    """
    Description:
    ------------
    アルゴリズムの基底クラス
    """

    def __init__(self, best_changed, islands, termination, migration=None):
        super().__init__(islands, termination, migration)

        self.__best_changed = best_changed
        self.__chromosomes = []
        self.__fitness = 0
        self.__best = None

    @property
    def initialized(self):
        return all(map(lambda island: island.initialized, self.islands))

    @property
    def generation_number(self):
        return reduce(lambda acc, island: acc + island.generation_number, self.islands, 0)

    @property
    def offspring_number(self):
        return reduce(lambda acc, island: acc + island.offspring_number, self.islands, 0)

    @property
    def chromosomes(self):
        return self.__chromosomes

    @property
    def best(self):
        if self.__best:
            return self.__best

        return self.__chromosomes[0] if len(self.__chromosomes) > 0 else None

    @property
    def progress(self):
        return self.termination.progress

    @property
    def fitness(self):
        return self.__chromosomes[0].fitness if len(self.__chromosomes) > 0 else None

    @property
    def has_reached(self):
        return self.termination.has_reached(self)

    def _update_chromosomes(self):
        self.__chromosomes = sorted(
            reduce(lambda acc, island: acc + island.population.chromosomes, self.islands, []),
            key=lambda chromosome: chromosome.fitness,
            reverse=True
        )

        if len(self.__chromosomes) > 0:
            self.__best = self.__chromosomes[0].clone()
            best_fitness = self.__chromosomes[0].fitness
            if best_fitness >= 0 and best_fitness != self.__fitness:
                self.__fitness = best_fitness
                self.__best_changed(self)

    def reset(self):
        for island in self.islands:
            island.reset()
        if self.migration:
            self.migration.init()
        self.termination.init()
        self._update_chromosomes()
        self._perform_reset()
        self.__fitness = 0
        self.__best = None

    def _perform_reset(self):
        pass

    @staticmethod
    def __island_step(island):
        island.step()

    def step(self):
        if self.has_reached:
            return

        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(self.__island_step, self.islands)

        if self.migration:
            self.migration.migrate(self)
        self._update_chromosomes()
        self._perform_step()

    def _perform_step(self):
        pass

    @abstractmethod
    def draw(self):
        pass

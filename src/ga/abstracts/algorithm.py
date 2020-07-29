from abc import abstractmethod
from functools import reduce
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable, List, Optional
from ..interfaces import IAlgorithm, IChromosome, IIsland, ITermination, IMigration


class AbstractAlgorithm(IAlgorithm):
    """
    Description:
    ------------
    アルゴリズムの基底クラス
    """

    __best_changed: Callable[[IAlgorithm], None]
    __chromosomes: List[IChromosome]
    __fitness: float
    __best: Optional[IChromosome]

    def __init__(self, best_changed: Callable[[IAlgorithm], None], islands: Iterable[IIsland], termination: ITermination, migration: Optional[IMigration] = None) -> None:
        super().__init__(islands, termination, migration)

        self.__best_changed = best_changed  # type: ignore
        self.__chromosomes = []
        self.__fitness = 0
        self.__best = None

    @property
    def initialized(self) -> bool:
        lambda_func: Callable[[IIsland], bool] = lambda island: island.initialized
        return all(map(lambda_func, self.islands))

    @property
    def generation_number(self) -> int:
        lambda_func: Callable[[int, IIsland], int] = lambda acc, island: acc + island.generation_number
        return reduce(lambda_func, self.islands, 0)

    @property
    def offspring_number(self) -> int:
        lambda_func: Callable[[int, IIsland], int] = lambda acc, island: acc + island.offspring_number
        return reduce(lambda_func, self.islands, 0)

    @property
    def chromosomes(self) -> List[IChromosome]:
        return self.__chromosomes

    @property
    def best(self) -> Optional[IChromosome]:
        if self.__best:
            return self.__best

        return self.__chromosomes[0] if len(self.__chromosomes) > 0 else None

    @property
    def progress(self) -> float:
        return self.termination.progress

    @property
    def fitness(self) -> Optional[float]:
        return self.__chromosomes[0].fitness if len(self.__chromosomes) > 0 else None

    @property
    def has_reached(self) -> bool:
        return self.termination.has_reached(self)

    def _update_chromosomes(self) -> None:
        lambda_func: Callable[[List[IChromosome], IIsland], List[IChromosome]] = lambda acc, island: acc + island.population.chromosomes
        initial: List[IChromosome] = []
        self.__chromosomes = sorted(
            reduce(lambda_func, self.islands, initial),  # type: ignore
            key=lambda chromosome: chromosome.fitness,
            reverse=True
        )

        if len(self.__chromosomes) > 0:
            self.__best = self.__chromosomes[0].clone()
            best_fitness = self.__chromosomes[0].fitness
            if best_fitness >= 0 and best_fitness != self.__fitness:
                self.__fitness = best_fitness
                self.__best_changed(self)  # type: ignore

    def reset(self) -> None:
        for island in self.islands:
            island.reset()
        if self.migration:
            self.migration.init()
        self.termination.init()
        self._update_chromosomes()
        self._perform_reset()
        self.__fitness = 0
        self.__best = None

    def _perform_reset(self) -> None:
        pass

    @staticmethod
    def __island_step(island: IIsland) -> None:
        island.step()

    def step(self) -> None:
        if self.has_reached:
            return

        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(self.__island_step, self.islands)

        if self.migration:
            self.migration.migrate(self)
        self._update_chromosomes()
        self._perform_step()

    def _perform_step(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

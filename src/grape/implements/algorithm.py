import math
from typing import List, Tuple, Callable, Optional
from targets import get_target
from target import ITarget
from ga import AbstractAlgorithm, IChromosome, IAlgorithm, IIsland
from .termination import Termination
from .migration import Migration
from .function_set import FunctionSet
from .generations import MggIsland, CulturalIsland
from .test import TestData, TestDataset
from .fitness_helper import FitnessHelper
from ..interfaces import IGenotype


class Algorithm(AbstractAlgorithm):
    """
    Description:
    ------------
    アルゴリズム
    """

    __target: str
    __best_changed: Tuple[Callable[[IAlgorithm, ITarget, IChromosome], None], ...]
    __cloned_target: Optional[ITarget]

    def __init__(self, target: str, *best_changed: Callable[[IAlgorithm, ITarget, IChromosome], None]) -> None:
        self.__target = target
        self.__best_changed = best_changed

        target_instance = get_target(target)
        settings = target_instance.ga_settings
        super().__init__(
            self.__best_changed_function,
            self.__get_islands(target, target_instance),
            Termination(settings.terminate_offspring_number),
            Migration(settings.migration_rate, settings.migration_interval)
        )

        self.__cloned_target = None

    def __best_changed_function(self, algorithm: IAlgorithm) -> None:
        self.__cloned_target = get_target(self.__target)
        if not isinstance(self.best, IGenotype):
            raise Exception('Unexpected Error')
        phenotype = self.best.phenotype
        phenotype.while_end(phenotype.get_context(self.__cloned_target))

        self.draw()
        if self.best:
            for func in self.__best_changed:
                if callable(func):
                    func(algorithm, self.__cloned_target, self.best)

    @staticmethod
    def __get_islands(target: str, target_instance: ITarget) -> List[IIsland]:
        settings = target_instance.ga_settings
        total_island_number = max(1, settings.island_number)
        cultural_island_number = math.floor(total_island_number * settings.cultural_island_rate)
        mgg_island_number = max(1, total_island_number - cultural_island_number)
        cultural_island_number = total_island_number - mgg_island_number

        dataset = TestDataset(settings.test_number, TestData(target))
        population_size = math.floor(settings.population_size / total_island_number)
        functions = FunctionSet(target_instance.settings.action_number, target_instance.settings.perception_number)
        helper = FitnessHelper(target)
        islands: List[IIsland] = []
        for _ in range(mgg_island_number):
            islands.append(MggIsland(
                helper,
                population_size,
                settings.crossover_probability,
                settings.mutation_probability,
                dataset,
                functions,
                settings.node_count,
                settings.mix_probability,
                settings.crossover_time,
                settings.test_number > 1
            ))
        if cultural_island_number > 0:
            for _ in range(cultural_island_number):
                islands.append(CulturalIsland(
                    helper,
                    population_size,
                    settings.crossover_probability,
                    settings.mutation_probability,
                    dataset,
                    functions,
                    settings.node_count,
                    settings.test_number > 1
                ))
        return islands

    def draw(self) -> None:
        if not self.__cloned_target:
            return

        self.__cloned_target.draw()

        print(f'{self.progress:.3f}', f'{self.fitness:.3f}')
        print(f'{self.__cloned_target.get_fitness():.3f}', self.__cloned_target.step, self.__cloned_target.action_step)
        print()

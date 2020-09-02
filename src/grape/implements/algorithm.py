import math
from typing import List, Tuple, Callable, Optional, cast
from tasks import get_task
from task import ITask, AbstractAtariTask
from ga import AbstractAlgorithm, IChromosome, IAlgorithm, IIsland
from .termination import Termination
from .migration import Migration
from .function_set import FunctionSet
from .phenotype import Phenotype
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

    __task_name: str
    __best_changed: Tuple[Callable[[IAlgorithm, ITask, IChromosome], None], ...]
    __cloned_task: Optional[ITask]

    def __init__(self, task_name: str, *best_changed: Callable[[IAlgorithm, ITask, IChromosome], None]) -> None:
        self.__task_name = task_name
        self.__best_changed = best_changed

        task = get_task(task_name)
        settings = task.ga_settings
        super().__init__(
            1 if isinstance(task, AbstractAtariTask) else 3,  # type: ignore
            self.__best_changed_function,
            self.__get_islands(task_name, task),
            Termination(settings.terminate_offspring_number),
            Migration(settings.migration_rate, settings.migration_interval)
        )

        self.__cloned_task = None

    def __best_changed_function(self, algorithm: IAlgorithm) -> None:
        if not self.best or not isinstance(self.best, IGenotype):
            raise Exception('Unexpected Error')

        genotype: IGenotype = cast(IGenotype, self.best)
        self.__cloned_task = get_task(self.__task_name)
        Phenotype.while_end(genotype, Phenotype.get_context(genotype, self.__cloned_task))
        for func in self.__best_changed:
            if callable(func):
                func(algorithm, self.__cloned_task, self.best)

    @staticmethod
    def __get_islands(task_name: str, task: ITask) -> List[IIsland]:
        settings = task.ga_settings
        total_island_number = max(1, settings.island_number)
        cultural_island_number = math.floor(total_island_number * settings.cultural_island_rate)
        mgg_island_number = max(1, total_island_number - cultural_island_number)
        cultural_island_number = total_island_number - mgg_island_number

        dataset = TestDataset(settings.test_number, TestData(task_name))
        population_size = math.floor(settings.population_size / total_island_number)
        functions = FunctionSet(task.settings.action_number, task.settings.perception_number)
        helper = FitnessHelper(task_name)
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
                    settings.mutation_probability,
                    dataset,
                    functions,
                    settings.node_count,
                    False
                ))
        return islands

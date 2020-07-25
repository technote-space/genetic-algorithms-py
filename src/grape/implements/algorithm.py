import math
from ga import AbstractAlgorithm
from .termination import Termination
from .migration import Migration
from .function_set import FunctionSet
from .generations import MggIsland, CulturalIsland
from .test import TestData, TestDataset


class Algorithm(AbstractAlgorithm):
    """
    Description:
    ------------
    アルゴリズム
    """

    def __init__(self, target):
        self.__target = target
        settings = target.ga_settings
        super().__init__(
            self.__best_changed,
            self.__get_islands(target),
            Termination(settings.terminate_offspring_number),
            Migration(settings.migration_rate, settings.migration_interval)
        )

    @staticmethod
    def __best_changed(algorithm):
        algorithm.draw()

    @staticmethod
    def __get_islands(target):
        settings = target.ga_settings
        dataset = TestDataset(settings.test_number, TestData(target))
        functions = FunctionSet(target)
        total_island_number = max(1, settings.island_number)
        cultural_island_number = math.floor(total_island_number * settings.cultural_island_rate)
        mgg_island_number = max(1, total_island_number - cultural_island_number)
        cultural_island_number = total_island_number - mgg_island_number
        population_size = math.floor(settings.population_size / total_island_number)

        islands = []
        for _ in range(mgg_island_number):
            islands.append(MggIsland(
                population_size,
                settings.crossover_probability,
                settings.mutation_probability,
                dataset,
                functions,
                settings.node_count,
                settings.mix_probability,
                settings.crossover_time
            ))
        if cultural_island_number > 0:
            for _ in range(cultural_island_number):
                islands.append(CulturalIsland(
                    population_size,
                    settings.crossover_probability,
                    settings.mutation_probability,
                    dataset,
                    functions,
                    settings.node_count
                ))
        return islands

    def draw(self):
        target = self.__target.clone()
        phenotype = self.best.phenotype
        phenotype.while_end(phenotype.get_context(target, FunctionSet(target)))
        target.draw()

        print(self.progress, f'{self.fitness:.3f}')
        print(f'{target.get_fitness():.3f}', target.step, target.action_step)
        print()

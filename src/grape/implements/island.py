from typing import List
from ga import AbstractIsland, ICrossover, IReinsertion, IChromosome
from .genotype import Genotype
from .population import Population
from .fitness import Fitness
from .selection import Selection
from .mutation import Mutation
from .fitness_helper import FitnessHelper
from ..interfaces import IFunctionSet, ITestDataset


class GrapeIsland(AbstractIsland):
    """
    Description:
    ------------
    島の基底クラス
    """

    __helper: FitnessHelper

    def __init__(
        self,
        helper: FitnessHelper,
        population_size: int,
        crossover: ICrossover,
        crossover_probability: float,
        mutation_probability: float,
        reinsertion: IReinsertion,
        dataset: ITestDataset,
        functions: IFunctionSet,
        node_count: int,
        evaluate_parents_fitness: bool
    ):
        super().__init__(
            Population(population_size, Genotype(node_count, functions)),
            Fitness(dataset),
            Selection(),
            crossover,
            crossover_probability,
            Mutation(),
            mutation_probability,
            reinsertion,
            evaluate_parents_fitness
        )

        self.__helper = helper

    def _evaluate(self, chromosomes: List[IChromosome]) -> None:
        self.__helper.run(chromosomes)

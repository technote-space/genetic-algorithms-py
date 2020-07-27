from ga import AbstractIsland
from .genotype import Genotype
from .population import Population
from .fitness import Fitness
from .selection import Selection
from .mutation import Mutation


class GrapeIsland(AbstractIsland):
    """
    Description:
    ------------
    島の基底クラス
    """

    def __init__(
            self,
            helper,
            population_size,
            crossover,
            crossover_probability,
            mutation_probability,
            reinsertion,
            dataset,
            functions,
            node_count,
            evaluate_parents_fitness
    ):
        super().__init__(
            Population(population_size, Genotype(node_count, functions)),
            Fitness(dataset, functions),
            Selection(),
            crossover,
            crossover_probability,
            Mutation(),
            mutation_probability,
            reinsertion,
            evaluate_parents_fitness
        )

        self.__helper = helper

    def _evaluate(self, chromosomes):
        self.__helper.run(chromosomes)

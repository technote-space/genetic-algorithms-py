from ...island import GrapeIsland
from .crossover import MggCrossover
from .reinsertion import MggReinsertion
from ...fitness_helper import FitnessHelper
from ....interfaces import ITestDataset, IFunctionSet


class MggIsland(GrapeIsland):
    """
    Description:
    ------------
    島クラス
    """

    def __init__(
        self,
        helper: FitnessHelper,
        population_size: int,
        crossover_probability: float,
        mutation_probability: float,
        dataset: ITestDataset,
        functions: IFunctionSet,
        node_count: int,
        mix_probability: float,
        crossover_time: int,
        evaluate_parents_fitness: bool
    ):
        super().__init__(
            helper,
            population_size,
            MggCrossover(crossover_probability, mix_probability, crossover_time),
            mutation_probability,
            MggReinsertion(),
            dataset,
            functions,
            node_count,
            evaluate_parents_fitness
        )

from ...island import GrapeIsland
from .crossover import CulturalCrossover
from .reinsertion import CulturalReinsertion
from ...fitness_helper import FitnessHelper
from ....interfaces import ITestDataset, IFunctionSet


class CulturalIsland(GrapeIsland):
    """
    Description:
    ------------
    島クラス
    """

    def __init__(
        self,
        helper: FitnessHelper,
        population_size: int,
        mutation_probability: float,
        dataset: ITestDataset,
        functions: IFunctionSet,
        node_count: int,
        evaluate_parents_fitness: bool
    ):
        super().__init__(
            helper,
            population_size,
            CulturalCrossover(node_count, functions),
            mutation_probability,
            CulturalReinsertion(),
            dataset,
            functions,
            node_count,
            evaluate_parents_fitness
        )

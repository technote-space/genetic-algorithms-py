from ...island import GrapeIsland
from .crossover import CulturalCrossover
from .reinsertion import CulturalReinsertion


class CulturalIsland(GrapeIsland):
    """
    Description:
    ------------
    島クラス
    """

    def __init__(
            self,
            helper,
            population_size,
            crossover_probability,
            mutation_probability,
            dataset,
            functions,
            node_count,
            evaluate_parents_fitness
    ):
        super().__init__(
            helper,
            population_size,
            CulturalCrossover(),
            crossover_probability,
            mutation_probability,
            CulturalReinsertion(),
            dataset,
            functions,
            node_count,
            evaluate_parents_fitness
        )

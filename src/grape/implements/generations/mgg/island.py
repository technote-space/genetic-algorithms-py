from ...island import GrapeIsland
from .crossover import MggCrossover
from .reinsertion import MggReinsertion


class MggIsland(GrapeIsland):
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
            mix_probability,
            crossover_time
    ):
        super().__init__(
            helper,
            population_size,
            MggCrossover(mix_probability, crossover_time),
            crossover_probability,
            mutation_probability,
            MggReinsertion(),
            dataset,
            functions,
            node_count
        )

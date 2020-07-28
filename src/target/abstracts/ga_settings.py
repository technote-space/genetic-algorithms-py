from ..interfaces import IGaSettings


class AbstractGaSettings(IGaSettings):
    """
    Description:
    ------------
    GAの設定の基底クラス
    """

    @property
    def terminate_offspring_number(self) -> int:
        return 250000

    @property
    def population_size(self) -> int:
        return 200

    @property
    def island_number(self) -> int:
        return 10

    @property
    def cultural_island_rate(self) -> float:
        return 0.1

    @property
    def migration_interval(self) -> int:
        return 2500

    @property
    def migration_rate(self) -> float:
        return 0.01

    @property
    def crossover_time(self) -> int:
        return 10

    @property
    def crossover_probability(self) -> float:
        return 0.02

    @property
    def mutation_probability(self) -> float:
        return 0.1

    @property
    def mix_probability(self) -> float:
        return 0.1

    @property
    def node_count(self) -> int:
        return 50

    @property
    def test_number(self) -> int:
        return 1

from ..interfaces import IGaSettings


class AbstractGaSettings(IGaSettings):
    """
    Description:
    ------------
    GAの設定の基底クラス
    """

    @property
    def terminate_offspring_number(self):
        return 250000

    @property
    def population_size(self):
        return 200

    @property
    def island_number(self):
        return 10

    @property
    def cultural_island_rate(self):
        return 0.1

    @property
    def migration_interval(self):
        return 2500

    @property
    def migration_rate(self):
        return 0.01

    @property
    def crossover_time(self):
        return 10

    @property
    def crossover_probability(self):
        return 0.02

    @property
    def mutation_probability(self):
        return 0.1

    @property
    def mix_probability(self):
        return 0.1

    @property
    def node_count(self):
        return 100

from abc import ABCMeta, abstractmethod


class IGaSettings(metaclass=ABCMeta):
    """
    Description:
    ------------
    GAの設定のinterface
    """

    @property
    @abstractmethod
    def terminate_offspring_number(self):
        pass

    @property
    @abstractmethod
    def population_size(self):
        pass

    @property
    @abstractmethod
    def island_number(self):
        pass

    @property
    @abstractmethod
    def cultural_island_rate(self):
        pass

    @property
    @abstractmethod
    def migration_interval(self):
        pass

    @property
    @abstractmethod
    def migration_rate(self):
        pass

    @property
    @abstractmethod
    def crossover_time(self):
        pass

    @property
    @abstractmethod
    def crossover_probability(self):
        pass

    @property
    @abstractmethod
    def mutation_probability(self):
        pass

    @property
    @abstractmethod
    def mix_probability(self):
        pass

    @property
    @abstractmethod
    def node_count(self):
        pass

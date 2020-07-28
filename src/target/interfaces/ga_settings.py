from abc import ABCMeta, abstractmethod


class IGaSettings(metaclass=ABCMeta):
    """
    Description:
    ------------
    GAの設定のinterface
    """

    @property
    @abstractmethod
    def terminate_offspring_number(self) -> int:
        pass

    @property
    @abstractmethod
    def population_size(self) -> int:
        pass

    @property
    @abstractmethod
    def island_number(self) -> int:
        pass

    @property
    @abstractmethod
    def cultural_island_rate(self) -> float:
        pass

    @property
    @abstractmethod
    def migration_interval(self) -> int:
        pass

    @property
    @abstractmethod
    def migration_rate(self) -> float:
        pass

    @property
    @abstractmethod
    def crossover_time(self) -> int:
        pass

    @property
    @abstractmethod
    def crossover_probability(self) -> float:
        pass

    @property
    @abstractmethod
    def mutation_probability(self) -> float:
        pass

    @property
    @abstractmethod
    def mix_probability(self) -> float:
        pass

    @property
    @abstractmethod
    def node_count(self) -> int:
        pass

    @property
    @abstractmethod
    def test_number(self) -> int:
        pass

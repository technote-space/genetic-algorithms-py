from abc import ABCMeta, abstractmethod
from typing import List, Iterable


class IChromosome(metaclass=ABCMeta):
    """
    Description:
    ------------
    染色体のinterface
    """

    @property
    @abstractmethod
    def length(self) -> int:
        pass

    @property
    @abstractmethod
    def acids(self) -> List[int]:
        pass

    @property
    @abstractmethod
    def fitness(self) -> float:
        pass

    @abstractmethod
    def create_from_acids(self, acids: Iterable[int]) -> None:
        pass

    @abstractmethod
    def get_acid(self, index: int) -> int:
        pass

    @abstractmethod
    def set_acid(self, index: int, acid: int) -> None:
        pass

    @abstractmethod
    def generate_acid(self, index: int) -> int:
        pass

    @abstractmethod
    def generate_acids(self) -> None:
        pass

    @abstractmethod
    def create_new(self) -> 'IChromosome':
        pass

    @abstractmethod
    def clone(self) -> 'IChromosome':
        pass

    @abstractmethod
    def copy_from(self, chromosome: 'IChromosome') -> None:
        pass

    @abstractmethod
    def mutation(self, index: int) -> None:
        pass

    @abstractmethod
    def set_fitness(self, fitness: float, step: float, action_step: float) -> None:
        pass

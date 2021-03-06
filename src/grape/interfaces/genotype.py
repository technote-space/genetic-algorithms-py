from abc import abstractmethod
from typing import List
from ga import IChromosome


class IGenotype(IChromosome):
    """
    Description:
    ------------
    遺伝子型のinterface
    """

    @property
    @abstractmethod
    def fitness(self) -> float:
        pass

    @property
    @abstractmethod
    def step(self) -> float:
        pass

    @property
    @abstractmethod
    def action_step(self) -> float:
        pass

    @property
    @abstractmethod
    def functions(self) -> 'IFunctionSet':
        pass

    @abstractmethod
    def create_from_nodes(self, nodes: List[int]) -> None:
        pass

    @abstractmethod
    def get_node_genes(self, index: int) -> List[int]:
        pass

    @abstractmethod
    def get_nodes(self) -> List[int]:
        pass

    @property
    @abstractmethod
    def node_count(self) -> int:
        pass

    @abstractmethod
    def generate_acid(self, index: int) -> int:
        pass

    @abstractmethod
    def create_new(self) -> 'IGenotype':
        pass


from .function_set import IFunctionSet  # noqa: E402

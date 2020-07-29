import math
import random
from typing import Optional, List
from ..interfaces import IGenotype, IFunctionSet, IPhenotype
from .phenotype import Phenotype


class Genotype(IGenotype):
    """
    Description:
    ------------
    遺伝子型
    """

    __node_count: int
    __node_length: int
    __functions: IFunctionSet
    __phenotype: Optional[IPhenotype]

    def __init__(self, node_count: int, functions: IFunctionSet) -> None:
        super().__init__((node_count + 1) * 3)
        self.__node_count = node_count
        self.__node_length = 3
        self.__functions = functions
        self.__phenotype = None
        self.generate_acids()

    @property
    def phenotype(self) -> IPhenotype:
        if self.__phenotype is None:
            self.__phenotype = Phenotype(self)
        return self.__phenotype

    @property
    def fitness(self) -> float:
        return self.phenotype.fitness

    @property
    def step(self) -> float:
        return self.phenotype.step

    @property
    def functions(self) -> IFunctionSet:
        return self.__functions

    def create_from_nodes(self, nodes: List[int]) -> None:
        self.create_from_acids(nodes)
        self.__node_count = math.ceil(len(nodes) / self.__node_length) - 1

    def get_node_genes(self, index: int) -> List[int]:
        genes = []
        for key in range(self.__node_length):
            genes.append(self.get_acid(key + index * self.__node_length))

        return genes

    def get_nodes(self) -> List[int]:
        nodes = []
        for index in range(self.__node_count + 1):
            nodes.extend(self.get_node_genes(index))
        return nodes

    @property
    def node_count(self) -> int:
        return self.__node_count

    def generate_acid(self, index: int) -> int:
        if index % 3 == 0:
            return self._get_node_type(index)
        else:
            return self._get_connection()

    def _get_node_type(self, index: int) -> int:
        if index == 0:
            return 0

        return self.__functions.get_random_index()

    def _get_connection(self) -> int:
        return math.floor(random.random() * self.node_count) + 1

    def create_new(self) -> IGenotype:
        return Genotype(self.node_count, self.__functions)

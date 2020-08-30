import math
import random
from typing import List
from ga import IChromosome, AbstractChromosome
from ..interfaces import IGenotype, IFunctionSet


class Genotype(AbstractChromosome, IGenotype):
    """
    Description:
    ------------
    遺伝子型
    """

    __node_count: int
    __node_length: int
    __functions: IFunctionSet
    __fitness: float
    __step: float
    __action_step: float

    def __init__(self, node_count: int, functions: IFunctionSet) -> None:
        super().__init__((node_count + 1) * 3)
        self.__node_count = node_count
        self.__node_length = 3
        self.__functions = functions
        self.__fitness = -1
        self.__step = 0
        self.__action_step = 0
        self.generate_acids()

    @property
    def fitness(self) -> float:
        return self.__fitness

    @property
    def step(self) -> float:
        return self.__step

    @property
    def action_step(self) -> float:
        return self.__action_step

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

    def _perform_copy_from(self, chromosome: IChromosome) -> None:
        if isinstance(chromosome, IGenotype):
            self.__fitness = chromosome.fitness
            self.__step = chromosome.step
            self.__action_step = chromosome.action_step

    def set_fitness(self, fitness: float, step: float, action_step: float) -> None:
        self.__fitness = fitness
        self.__step = step
        self.__action_step = action_step

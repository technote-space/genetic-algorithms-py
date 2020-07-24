import math
import random
from ga import AbstractChromosome
from .phenotype import Phenotype


class Genotype(AbstractChromosome):
    """
    Description:
    ------------
    遺伝子型
    """

    def __init__(self, node_count, functions):
        super().__init__((node_count + 1) * 3)
        self.__node_count = node_count
        self.__node_length = 3
        self.__functions = functions
        self.__phenotype = None
        self.generate_acids()

    @property
    def phenotype(self):
        if self.__phenotype is None:
            self.__phenotype = Phenotype(self)
        return self.__phenotype

    @property
    def fitness(self):
        return self.phenotype.fitness

    @property
    def step(self):
        return self.phenotype.step

    def create_from_nodes(self, nodes):
        self.create_from_acids(nodes)
        self.__node_count = len(nodes) / self.__node_length - 1

    def get_node_genes(self, index):
        genes = []
        for key in range(self.__node_length):
            genes.append(self.get_acid(key + index * self.__node_length))

        return genes

    def get_nodes(self):
        nodes = []
        for index in range(self.__node_count + 1):
            nodes.extend(self.get_node_genes(index))
        return nodes

    @property
    def node_count(self):
        return self.__node_count

    def generate_acid(self, index):
        if index % 3 == 0:
            return self._get_node_type(index)
        else:
            return self._get_connection()

    def _get_node_type(self, index):
        if index == 0:
            return 0

        return self.__functions.get_random_index()

    def _get_connection(self):
        return math.floor(random.random() * self.node_count) + 1

    def create_new(self):
        return Genotype(self.node_count, self.__functions)

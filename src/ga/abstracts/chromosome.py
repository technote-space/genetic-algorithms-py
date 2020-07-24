from abc import abstractmethod
import copy
from ..interfaces import IChromosome


class AbstractChromosome(IChromosome):
    """
    Description:
    ------------
    染色体の基底クラス
    """

    def __init__(self, length):
        self.__acids = [0] * length

    @property
    def length(self):
        return len(self.__acids)

    @property
    def acids(self):
        return self.__acids

    @property
    @abstractmethod
    def fitness(self):
        pass

    def create_from_acids(self, acids):
        self.__acids = copy.copy(acids)

    def get_acid(self, index):
        return self.__acids[index]

    def set_acid(self, index, acid):
        self.__acids[index] = acid

    @abstractmethod
    def generate_acid(self, index):
        pass

    def generate_acids(self):
        for index in range(self.length):
            self.set_acid(index, self.generate_acid(index))

    @abstractmethod
    def create_new(self):
        pass

    def clone(self):
        cloned = self.create_new()
        cloned.copy_from(self)
        return cloned

    def copy_from(self, chromosome):
        if self.length != chromosome.length:
            raise Exception('Length is not same.')

        for index in range(self.length):
            self.set_acid(index, chromosome.get_acid(index))
        self._perform_copy_from(chromosome)

    def _perform_copy_from(self, chromosome):
        pass

    def mutation(self, index):
        self.set_acid(index, self.generate_acid(index))

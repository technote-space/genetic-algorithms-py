from abc import ABCMeta, abstractmethod


class IChromosome(metaclass=ABCMeta):
    """
    Description:
    ------------
    染色体のinterface
    """

    @property
    @abstractmethod
    def length(self):
        pass

    @property
    @abstractmethod
    def acids(self):
        pass

    @property
    @abstractmethod
    def fitness(self):
        pass

    @abstractmethod
    def create_from_acids(self, acids):
        pass

    @abstractmethod
    def get_acid(self, index):
        pass

    @abstractmethod
    def set_acid(self, index, acid):
        pass

    @abstractmethod
    def generate_acid(self, index):
        pass

    @abstractmethod
    def generate_acids(self):
        pass

    @abstractmethod
    def create_new(self):
        pass

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def copy_from(self, chromosome):
        pass

    @abstractmethod
    def mutation(self, index):
        pass

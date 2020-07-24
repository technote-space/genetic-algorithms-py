from abc import ABCMeta, abstractmethod


class IAlgorithm(metaclass=ABCMeta):
    """
    Description:
    ------------
    アルゴリズムのinterface
    """

    def __init__(self, islands, termination, migration=None):
        self.__islands = tuple(islands)
        self.__termination = termination
        self.__migration = migration

    @property
    def islands(self):
        return self.__islands

    @property
    def termination(self):
        return self.__termination

    @property
    def migration(self):
        return self.__migration

    @property
    @abstractmethod
    def initialized(self):
        pass

    @property
    @abstractmethod
    def generation_number(self):
        pass

    @property
    @abstractmethod
    def offspring_number(self):
        pass

    @property
    @abstractmethod
    def chromosomes(self):
        pass

    @property
    @abstractmethod
    def best(self):
        pass

    @property
    @abstractmethod
    def progress(self):
        pass

    @property
    @abstractmethod
    def fitness(self):
        pass

    @property
    @abstractmethod
    def has_reached(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def draw(self):
        pass

from abc import ABCMeta, abstractmethod


class IPopulation(metaclass=ABCMeta):
    """
    Description:
    ------------
    人口のinterface
    """

    def __init__(self, size, adam):
        self.__size = size
        self.__adam = adam

    @property
    def size(self):
        return self.__size

    @property
    def adam(self):
        return self.__adam

    @property
    @abstractmethod
    def chromosomes(self):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def update(self, chromosomes):
        pass

from abc import ABCMeta, abstractmethod


class IReinsertion(metaclass=ABCMeta):
    """
    Description:
    ------------
    挿入のinterface
    """

    @abstractmethod
    def select(self, population, offspring, parents, size):
        pass

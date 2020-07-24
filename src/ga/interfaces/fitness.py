from abc import ABCMeta, abstractmethod


class IFitness(metaclass=ABCMeta):
    """
    Description:
    ------------
    適応度のinterface
    """

    @abstractmethod
    def evaluate(self, chromosome):
        pass

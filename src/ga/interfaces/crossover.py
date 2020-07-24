from abc import ABCMeta, abstractmethod


class ICrossover(metaclass=ABCMeta):
    """
    Description:
    ------------
    交叉のinterface
    """

    def __init__(self, parents_number, children_number):
        self.__parents_number = parents_number
        self.__children_number = children_number

    @property
    def parents_number(self):
        return self.__parents_number

    @property
    def children_number(self):
        return self.__children_number

    @abstractmethod
    def cross(self, parents, probability):
        pass

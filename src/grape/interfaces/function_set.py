from abc import ABCMeta, abstractmethod


class IFunctionSet(metaclass=ABCMeta):
    """
    Description:
    ------------
    関数セットのinterface
    """

    @property
    @abstractmethod
    def functions(self):
        pass

    @property
    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def get_function(self, index):
        pass

    @abstractmethod
    def add(self, func):
        pass

    @abstractmethod
    def get_random_index(self):
        pass

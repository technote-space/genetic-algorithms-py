from abc import ABCMeta, abstractmethod


class ITermination(metaclass=ABCMeta):
    """
    Description:
    ------------
    終了条件のinterface
    """

    @property
    @abstractmethod
    def progress(self):
        pass

    @abstractmethod
    def has_reached(self, algorithm):
        pass

    @abstractmethod
    def init(self):
        pass

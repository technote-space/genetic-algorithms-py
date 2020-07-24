from abc import ABCMeta, abstractmethod


class IContext(metaclass=ABCMeta):
    """
    Description:
    ------------
    コンテキストのinterface
    """

    @property
    @abstractmethod
    def target(self):
        pass

    @property
    @abstractmethod
    def current(self):
        pass

    @property
    @abstractmethod
    def node_count(self):
        pass

    @property
    @abstractmethod
    def functions(self):
        pass

    @property
    @abstractmethod
    def phenotype(self):
        pass

    @abstractmethod
    def set_current(self, current):
        pass

from abc import ABCMeta, abstractmethod


class IFunction(metaclass=ABCMeta):
    """
    Description:
    ------------
    関数のinterface
    """

    @abstractmethod
    def execute(self, c1, c2, context):
        pass

    @abstractmethod
    def get_possible_connections(self, c1, c2, context):
        pass

    @abstractmethod
    def programming(self, c1, c2, context):
        pass

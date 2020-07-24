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
    def function_expression(self, c1, c2, context):
        pass

    @abstractmethod
    def connection_expression(self, c1, c2, context):
        pass

    @abstractmethod
    def possible_connections(self, c1, c2, context):
        pass

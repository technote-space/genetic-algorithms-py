from abc import abstractmethod
from ..interfaces import IFunction


class AbstractFunction(IFunction):
    """
    Description:
    ------------
    関数の基底クラス
    """

    @abstractmethod
    def _run(self, c1, c2, context):
        pass

    def execute(self, c1, c2, context):
        self._run(c1, c2, context)

    def get_possible_connections(self, c1, c2, context):
        pass

    @abstractmethod
    def programming(self, c1, c2, context):
        pass

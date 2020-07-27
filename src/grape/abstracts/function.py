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

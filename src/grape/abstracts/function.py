from abc import abstractmethod
from typing import Iterable
from ..interfaces import IFunction, IContext, IFuncBlock


class AbstractFunction(IFunction):
    """
    Description:
    ------------
    関数の基底クラス
    """

    @abstractmethod
    def _run(self, c1: int, c2: int, context: IContext) -> None:
        pass

    def execute(self, c1: int, c2: int, context: IContext) -> None:
        self._run(c1, c2, context)

    def get_possible_connections(self, c1: int, c2: int, context: IContext) -> Iterable[int]:
        pass

    @abstractmethod
    def programming(self, c1: int, c2: int, context: IContext) -> IFuncBlock:
        pass

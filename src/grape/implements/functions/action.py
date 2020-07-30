from typing import Iterable
from ..block import FuncBlock
from ...abstracts import AbstractFunction
from ...interfaces import IContext, IFuncBlock


class Action(AbstractFunction):
    """
    Description:
    ------------
    行動
    """

    __index: int

    def __init__(self, index: int) -> None:
        self.__index = index

    def _run(self, c1: int, c2: int, context: IContext) -> None:
        context.target.action(self.__index)
        if not context.is_skipping_frame:
            context.current = c1  # type: ignore  #(@see https://github.com/python/mypy/issues/1362)

    def get_possible_connections(self, c1: int, c2: int, context: IContext) -> Iterable[int]:
        return c1,

    def programming(self, c1: int, c2: int, context: IContext) -> IFuncBlock:
        return FuncBlock(
            context.current,
            [f'self.__context.action({self.__index})'] * context.target.settings.action_frame,
            c1
        )

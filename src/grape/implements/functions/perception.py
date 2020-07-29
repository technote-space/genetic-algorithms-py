from typing import Iterable
from ..block import FuncBlock, NextBlock
from ...abstracts import AbstractFunction
from ...interfaces import IContext, IFuncBlock


class Perception(AbstractFunction):
    """
    Description:
    ------------
    知覚
    """

    __index: int

    def __init__(self, index: int) -> None:
        self.__index = index

    def _run(self, c1: int, c2: int, context: IContext) -> None:
        context.set_current(c1 if context.target.perceive(self.__index) else c2)

    def get_possible_connections(self, c1: int, c2: int, context: IContext) -> Iterable[int]:
        return c1, c2

    def programming(self, c1: int, c2: int, context: IContext) -> IFuncBlock:
        return FuncBlock(
            context.current,
            [],
            NextBlock(f'self.__context.perception({self.__index})', [], c1, [], c2)
        )

from .action import Action
from ..block import FuncBlock
from ...interfaces import IContext, IFuncBlock


class Start(Action):
    """
    Description:
    ------------
    スタート
    """

    def __init__(self) -> None:
        super().__init__(0)

    def _run(self, c1: int, c2: int, context: IContext) -> None:
        context.current = c1  # type: ignore  #(@see https://github.com/python/mypy/issues/1362)

    def programming(self, c1: int, c2: int, context: IContext) -> IFuncBlock:
        return FuncBlock(context.current, [], c1)

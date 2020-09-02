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
        start_action_index = context.task.settings.start_action_index
        if start_action_index is not None:
            for index in start_action_index:
                context.task.action(index, True)
        context.current = c1  # type: ignore  #(@see https://github.com/python/mypy/issues/1362)

    def programming(self, c1: int, c2: int, context: IContext) -> IFuncBlock:
        start_action_index = context.task.settings.start_action_index_expression
        if start_action_index is not None:
            return FuncBlock(
                context.current,
                start_action_index,
                c1
            )
        return FuncBlock(context.current, [], c1)

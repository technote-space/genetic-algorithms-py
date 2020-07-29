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
        if context.target.settings.start_action_index is not None:
            context.target.action(context.target.settings.start_action_index, True)
        context.current = c1  # type: ignore  #(@see https://github.com/python/mypy/issues/1362)

    def programming(self, c1: int, c2: int, context: IContext) -> IFuncBlock:
        if context.target.settings.start_action_index is not None:
            return FuncBlock(
                context.current,
                [f'self.__context.action({context.target.settings.start_action_index}, True)'],
                c1
            )
        return FuncBlock(context.current, [], c1)

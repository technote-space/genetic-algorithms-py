from .action import Action
from ...interfaces import IContext


class Start(Action):
    """
    Description:
    ------------
    スタート
    """

    def __init__(self) -> None:
        super().__init__(0)

    def _run(self, c1: int, c2: int, context: IContext) -> None:
        context.set_current(c1)

    def programming(self, c1: int, c2: int, context: IContext) -> object:
        return {
            "id": context.current,
            "actions": [],
            "next": c1
        }

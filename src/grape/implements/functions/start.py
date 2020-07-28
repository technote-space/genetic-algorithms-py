from .action import Action


class Start(Action):
    """
    Description:
    ------------
    スタート
    """

    def __init__(self):
        super().__init__(0)

    def _run(self, c1, c2, context):
        context.set_current(c1)

    def programming(self, c1, c2, context):
        return {
            "id": context.current,
            "actions": [],
            "next": c1
        }

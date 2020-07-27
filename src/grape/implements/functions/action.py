from ...abstracts import AbstractFunction


class Action(AbstractFunction):
    """
    Description:
    ------------
    行動
    """

    def __init__(self, index):
        self.__index = index

    def _run(self, c1, c2, context):
        context.target.action(self.__index)
        context.set_current(c1)

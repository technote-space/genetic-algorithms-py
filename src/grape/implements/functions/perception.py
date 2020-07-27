from ...abstracts import AbstractFunction


class Perception(AbstractFunction):
    """
    Description:
    ------------
    知覚
    """

    def __init__(self, index):
        self.__index = index

    def _run(self, c1, c2, context):
        context.set_current(c1 if context.target.perceive(self.__index) else c2)

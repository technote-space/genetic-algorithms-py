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

    def function_expression(self, c1, c2, context):
        return context.target.get_perceive_expression(self.__index)

    def connection_expression(self, c1, c2, context):
        return f'goto {c1} : {c2}'

    def possible_connections(self, c1, c2, context):
        return c1, c2

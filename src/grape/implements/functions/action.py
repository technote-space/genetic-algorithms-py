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

    def function_expression(self, c1, c2, context):
        return context.target.get_action_expression(self.__index)

    def connection_expression(self, c1, c2, context):
        return f'then goto {c1}'

    def possible_connections(self, c1, c2, context):
        return c1,

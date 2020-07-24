from ..interfaces import IContext


class Context(IContext):
    """
    Description:
    ------------
    コンテキスト
    """

    def __init__(self, target, start, node_count, functions, phenotype):
        self.__target = target
        self.__current = start
        self.__node_count = node_count
        self.__functions = functions
        self.__phenotype = phenotype

    @property
    def target(self):
        return self.__target

    @property
    def current(self):
        return self.__current

    @property
    def node_count(self):
        return self.__node_count

    @property
    def functions(self):
        return self.__functions

    @property
    def phenotype(self):
        return self.__phenotype

    def set_current(self, current):
        self.__current = current

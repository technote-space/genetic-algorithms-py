from task import ITask
from ..interfaces import IContext, IFunctionSet


class Context(IContext):
    """
    Description:
    ------------
    コンテキスト
    """

    __task: ITask
    __current: int
    __node_count: int
    __functions: IFunctionSet
    __action_frame: int

    def __init__(self, task: ITask, start: int, node_count: int, functions: IFunctionSet) -> None:
        self.__task = task
        self.__current = start
        self.__node_count = node_count
        self.__functions = functions
        self.__action_frame = task.settings.action_frame
        self.__skip = 0

    @property
    def task(self) -> ITask:
        return self.__task

    @property
    def current(self) -> int:
        return self.__current

    @current.setter
    def current(self, current: int) -> None:
        self.__current = current

    @property
    def node_count(self) -> int:
        return self.__node_count

    @property
    def functions(self) -> IFunctionSet:
        return self.__functions

    @property
    def is_skipping_frame(self) -> bool:
        if self.__action_frame <= 1:
            return False

        self.__skip += 1
        if self.__skip >= self.__action_frame:
            self.__skip = 0
            return False
        return True

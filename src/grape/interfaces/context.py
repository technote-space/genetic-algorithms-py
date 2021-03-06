from abc import ABCMeta, abstractmethod
from task import ITask


class IContext(metaclass=ABCMeta):
    """
    Description:
    ------------
    コンテキストのinterface
    """

    @property
    @abstractmethod
    def task(self) -> ITask:
        pass

    @property  # type: ignore  #(@see https://github.com/python/mypy/issues/1362)
    @abstractmethod
    def current(self) -> int:
        pass

    @current.setter  # type: ignore  #(@see https://github.com/python/mypy/issues/1362)
    @abstractmethod
    def current(self, current: int) -> None:
        pass

    @property
    @abstractmethod
    def node_count(self) -> int:
        pass

    @property
    @abstractmethod
    def functions(self) -> 'IFunctionSet':
        pass

    @property
    @abstractmethod
    def is_skipping_frame(self) -> bool:
        pass


from .function_set import IFunctionSet  # noqa: E402

from abc import ABCMeta, abstractmethod
from task import ITask


class ITestData(metaclass=ABCMeta):
    """
    Description:
    ------------
    テストデータのinterface
    """

    @property
    @abstractmethod
    def task_name(self) -> str:
        pass

    @abstractmethod
    def create_new(self) -> ITask:
        pass

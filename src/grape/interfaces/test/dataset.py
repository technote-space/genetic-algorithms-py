from abc import ABCMeta, abstractmethod
from typing import Iterable
from task import ITask
from .data import ITestData


class ITestDataset(metaclass=ABCMeta):
    """
    Description:
    ------------
    テストデータセットのinterface
    """

    @property
    @abstractmethod
    def length(self) -> int:
        pass

    @property
    @abstractmethod
    def data(self) -> ITestData:
        pass

    @abstractmethod
    def create_dataset(self) -> Iterable[ITask]:
        pass

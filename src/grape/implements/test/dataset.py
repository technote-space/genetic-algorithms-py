from typing import Iterable
from task import ITask
from ...interfaces import ITestDataset, ITestData


class TestDataset(ITestDataset):
    """
    Description:
    ------------
    テストデータセット
    """

    __length: int
    __data: ITestData

    def __init__(self, length: int, data: ITestData) -> None:
        self.__length = max(1, length)
        self.__data = data

    @property
    def length(self) -> int:
        return self.__length

    @property
    def data(self) -> ITestData:
        return self.__data

    def __lambda(self, _: int) -> ITask:
        return self.data.create_new()

    def create_dataset(self) -> Iterable[ITask]:
        return map(self.__lambda, range(self.length))

from tasks import get_task
from task import ITask
from ...interfaces import ITestData


class TestData(ITestData):
    """
    Description:
    ------------
    テストデータ
    """

    __task: str

    def __init__(self, task: str) -> None:
        self.__task = task

    @property
    def task(self) -> str:
        return self.__task

    def create_new(self) -> ITask:
        return get_task(self.task)

from tasks import get_task
from task import ITask
from ...interfaces import ITestData


class TestData(ITestData):
    """
    Description:
    ------------
    テストデータ
    """

    __task_name: str

    def __init__(self, task_name: str) -> None:
        self.__task_name = task_name

    @property
    def task_name(self) -> str:
        return self.__task_name

    def create_new(self) -> ITask:
        return get_task(self.task_name)

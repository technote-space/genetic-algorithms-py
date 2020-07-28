from targets import get_target
from target import ITarget
from ...interfaces import ITestData


class TestData(ITestData):
    """
    Description:
    ------------
    テストデータ
    """

    __target: str

    def __init__(self, target: str) -> None:
        self.__target = target

    @property
    def target(self) -> str:
        return self.__target

    def create_new(self) -> ITarget:
        return get_target(self.target)

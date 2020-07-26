from targets import get_target
from ...interfaces import ITestData


class TestData(ITestData):
    """
    Description:
    ------------
    テストデータ
    """

    def __init__(self, target):
        self.__target = target

    @property
    def target(self):
        return self.__target

    def create_new(self):
        return get_target(self.target)

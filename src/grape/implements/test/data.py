from ...interfaces import ITestData


class TestData(ITestData):
    """
    Description:
    ------------
    テストデータ
    """

    def __init__(self, target):
        self.__adam = target

    @property
    def adam(self):
        return self.__adam

    def create_new(self):
        return self.adam.clone()

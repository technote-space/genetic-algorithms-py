from ...interfaces import ITestDataset


class TestDataset(ITestDataset):
    """
    Description:
    ------------
    テストデータセット
    """

    def __init__(self, length, data):
        self.__length = length
        self.__adam = data

    @property
    def length(self):
        return self.__length

    @property
    def adam(self):
        return self.__adam

    def create_dataset(self):
        return map(lambda _: self.adam.create_new(), range(self.length))

from ...interfaces import ITestDataset


class TestDataset(ITestDataset):
    """
    Description:
    ------------
    テストデータセット
    """

    def __init__(self, length, data):
        self.__length = max(1, length)
        self.__data = data

    @property
    def length(self):
        return self.__length

    @property
    def data(self):
        return self.__data

    def create_dataset(self):
        return map(lambda _: self.data.create_new(), range(self.length))

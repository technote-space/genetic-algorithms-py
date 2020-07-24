from abc import ABCMeta, abstractmethod


class ITestDataset(metaclass=ABCMeta):
    """
    Description:
    ------------
    テストデータセットのinterface
    """

    @property
    @abstractmethod
    def length(self):
        pass

    @property
    @abstractmethod
    def adam(self):
        pass

    @abstractmethod
    def create_dataset(self):
        pass

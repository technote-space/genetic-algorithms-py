from abc import ABCMeta, abstractmethod


class ITestData(metaclass=ABCMeta):
    """
    Description:
    ------------
    テストデータのinterface
    """

    @property
    @abstractmethod
    def adam(self):
        pass

    @abstractmethod
    def create_new(self):
        pass

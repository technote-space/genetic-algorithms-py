from abc import ABCMeta, abstractmethod


class ITestData(metaclass=ABCMeta):
    """
    Description:
    ------------
    テストデータのinterface
    """

    @property
    @abstractmethod
    def target(self):
        pass

    @abstractmethod
    def create_new(self):
        pass

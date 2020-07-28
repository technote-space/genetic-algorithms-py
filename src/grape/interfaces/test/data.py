from abc import ABCMeta, abstractmethod
from target import ITarget


class ITestData(metaclass=ABCMeta):
    """
    Description:
    ------------
    テストデータのinterface
    """

    @property
    @abstractmethod
    def target(self) -> str:
        pass

    @abstractmethod
    def create_new(self) -> ITarget:
        pass

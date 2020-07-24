from abc import ABCMeta, abstractmethod


class IMigration(metaclass=ABCMeta):
    """
    Description:
    ------------
    移住のinterface
    """

    def __init__(self, rate, interval):
        self.__rate = rate
        self.__interval = interval

    @property
    def rate(self):
        return self.__rate

    @property
    def interval(self):
        return self.__interval

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def get_count(self, algorithm):
        pass

    @abstractmethod
    def get_destinations(self, algorithm):
        pass

    @abstractmethod
    def migrate(self, algorithm):
        pass

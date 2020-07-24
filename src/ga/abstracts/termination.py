from abc import abstractmethod
from ..interfaces import ITermination


class AbstractTermination(ITermination):
    """
    Description:
    ------------
    終了条件の基底クラス
    """

    def __init__(self):
        self.__has_reached = False
        self.__progress = 0

    def init(self):
        self.__has_reached = False
        self.__progress = 0
        self._perform_init()

    def _perform_init(self):
        pass

    @property
    def progress(self):
        return self.__progress

    def has_reached(self, algorithm):
        if not self.__has_reached:
            self.__has_reached = self._perform_has_reached(algorithm)
            if self.__has_reached:
                self.__progress = 1
            else:
                self.__progress = self._perform_get_progress(algorithm)

        return self.__has_reached

    @abstractmethod
    def _perform_has_reached(self, algorithm):
        pass

    @abstractmethod
    def _perform_get_progress(self, algorithm):
        pass

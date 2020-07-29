from abc import abstractmethod
from ..interfaces import ITermination, IAlgorithm


class AbstractTermination(ITermination):
    """
    Description:
    ------------
    終了条件の基底クラス
    """

    __has_reached: bool
    __progress: float

    def __init__(self) -> None:
        self.__has_reached = False
        self.__progress = 0

    def init(self) -> None:
        self.__has_reached = False
        self.__progress = 0
        self._perform_init()

    def _perform_init(self) -> None:
        pass

    @property
    def progress(self) -> float:
        return self.__progress

    def has_reached(self, algorithm: IAlgorithm) -> bool:
        if not self.__has_reached:
            self.__has_reached = self._perform_has_reached(algorithm)
            if self.__has_reached:
                self.__progress = 1
            else:
                self.__progress = self._perform_get_progress(algorithm)

        return self.__has_reached

    @abstractmethod
    def _perform_has_reached(self, algorithm: IAlgorithm) -> bool:
        pass

    @abstractmethod
    def _perform_get_progress(self, algorithm: IAlgorithm) -> float:
        pass

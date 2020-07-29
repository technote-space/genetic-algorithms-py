from abc import ABCMeta, abstractmethod


class ITermination(metaclass=ABCMeta):
    """
    Description:
    ------------
    終了条件のinterface
    """

    @property
    @abstractmethod
    def progress(self) -> float:
        pass

    @abstractmethod
    def has_reached(self, algorithm: 'IAlgorithm') -> bool:
        pass

    @abstractmethod
    def init(self) -> None:
        pass


from .algorithm import IAlgorithm  # noqa: E402

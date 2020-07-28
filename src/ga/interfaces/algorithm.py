from abc import ABCMeta, abstractmethod
from typing import List, Tuple, Iterable, Optional


class IAlgorithm(metaclass=ABCMeta):
    """
    Description:
    ------------
    アルゴリズムのinterface
    """

    __islands: Tuple['IIsland']
    __termination: 'ITermination'
    __migration: 'IMigration'

    def __init__(self, islands: Iterable['IIsland'], termination: 'ITermination', migration: Optional['IMigration'] = None) -> None:
        self.__islands = tuple(islands)
        self.__termination = termination
        self.__migration = migration

    @property
    def islands(self) -> Tuple['IIsland']:
        return self.__islands

    @property
    def termination(self) -> 'ITermination':
        return self.__termination

    @property
    def migration(self) -> 'IMigration':
        return self.__migration

    @property
    @abstractmethod
    def initialized(self) -> bool:
        pass

    @property
    @abstractmethod
    def generation_number(self) -> int:
        pass

    @property
    @abstractmethod
    def offspring_number(self) -> int:
        pass

    @property
    @abstractmethod
    def chromosomes(self) -> List['IChromosome']:
        pass

    @property
    @abstractmethod
    def best(self) -> Optional['IChromosome']:
        pass

    @property
    @abstractmethod
    def progress(self) -> float:
        pass

    @property
    @abstractmethod
    def fitness(self) -> Optional[float]:
        pass

    @property
    @abstractmethod
    def has_reached(self) -> bool:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def step(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


from .island import IIsland  # noqa: E402
from .termination import ITermination  # noqa: E402
from .migration import IMigration  # noqa: E402
from .chromosome import IChromosome  # noqa: E402

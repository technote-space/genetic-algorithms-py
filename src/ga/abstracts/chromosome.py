import copy
from abc import abstractmethod
from typing import List, Iterable
from ..interfaces import IChromosome


class AbstractChromosome(IChromosome):
    """
    Description:
    ------------
    染色体の基底クラス
    """

    __acids: List[int]

    def __init__(self, length: int) -> None:
        self.__acids = [0] * length

    @property
    def length(self) -> int:
        return len(self.__acids)

    @property
    def acids(self) -> List[int]:
        return self.__acids

    @property
    @abstractmethod
    def fitness(self) -> float:
        pass

    def create_from_acids(self, acids: Iterable[int]) -> None:
        self.__acids = list(copy.copy(acids))

    def get_acid(self, index: int) -> int:
        return self.__acids[index]

    def set_acid(self, index: int, acid: int) -> None:
        self.__acids[index] = acid

    @abstractmethod
    def generate_acid(self, index: int) -> int:
        pass

    def generate_acids(self) -> None:
        for index in range(self.length):
            self.set_acid(index, self.generate_acid(index))

    @abstractmethod
    def create_new(self) -> IChromosome:
        pass

    def clone(self) -> IChromosome:
        cloned = self.create_new()
        cloned.copy_from(self)
        return cloned

    def copy_from(self, chromosome: IChromosome) -> None:
        if self.length != chromosome.length:
            raise Exception('Length is not same.')

        for index in range(self.length):
            self.set_acid(index, chromosome.get_acid(index))
        self._perform_copy_from(chromosome)

    def _perform_copy_from(self, chromosome: IChromosome) -> None:
        pass

    def mutation(self, index: int) -> None:
        self.set_acid(index, self.generate_acid(index))

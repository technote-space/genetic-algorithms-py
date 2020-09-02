import copy
from typing import MutableMapping
from .field_flags import FieldFlags
from .helper import Helper


class Field:
    """
    Description:
    ------------
    Field
    """

    __ate: int
    __field: MutableMapping[int, FieldFlags]
    __foods: int

    def __init__(self) -> None:
        self.__ate = 0
        self.__field = copy.copy(Helper.get_field())
        self.__foods = Helper.get_count()

    @property
    def width(self) -> int:
        return Helper.get_width()

    @property
    def height(self) -> int:
        return Helper.get_height()

    @property
    def rest(self) -> int:
        return self.__foods - self.__ate

    @property
    def is_finished(self) -> bool:
        return self.rest <= 0

    def __set_flag(self, x: int, y: int, flag: FieldFlags) -> None:
        self.__field[Helper.position_to_index(x, y, self.width)] = flag

    def get_flag(self, x: int, y: int) -> FieldFlags:
        index = Helper.position_to_index(x, y, self.width)
        if index in self.__field:
            return self.__field[index]

        return FieldFlags.NONE

    def __add_flag(self, x: int, y: int, flag: FieldFlags) -> None:
        # noinspection PyTypeChecker
        self.__set_flag(x, y, self.get_flag(x, y) | flag)

    def check(self, x: int, y: int, flag: FieldFlags) -> bool:
        return (self.get_flag(x, y) & flag) == flag

    def on_visited(self, x: int, y: int) -> None:
        if not self.check(x, y, FieldFlags.VISITED):
            self.__add_flag(x, y, FieldFlags.VISITED)

            if self.check(x, y, FieldFlags.FOOD):
                self.__ate += 1

    def get_fitness(self) -> float:
        return self.__ate / self.__foods

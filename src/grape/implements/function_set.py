import math
import random
from typing import List
from ..interfaces import IFunctionSet, IFunction
from .functions import Action, Perception, Start


class FunctionSet(IFunctionSet):
    """
    Description:
    ------------
    関数セット
    """

    __functions: List[IFunction]

    def __init__(self, action_number: int, perception_number: int) -> None:
        super().__init__()
        self.__functions = [Start()]
        self.__set_target_functions(action_number, perception_number)

    def __set_target_functions(self, action_number: int, perception_number: int) -> None:
        for index in range(action_number):
            self.add(Action(index))
        for index in range(perception_number):
            self.add(Perception(index))

    @property
    def functions(self) -> List[IFunction]:
        return self.__functions

    @property
    def length(self) -> int:
        return len(self.__functions)

    def get_function(self, index: int) -> IFunction:
        return self.__functions[index]

    def add(self, func: IFunction) -> None:
        self.__functions.append(func)

    def get_random_index(self) -> int:
        return math.floor(random.random() * (self.length - 1)) + 1

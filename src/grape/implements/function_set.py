import math
import random
from ..interfaces import IFunctionSet
from .functions import Action, Perception, Start


class FunctionSet(IFunctionSet):
    """
    Description:
    ------------
    関数セット
    """

    def __init__(self, target):
        super().__init__()
        self.__functions = [Start()]
        self.__set_target_functions(target)

    def __set_target_functions(self, target):
        for index in range(target.settings.action_number):
            self.add(Action(index))
        for index in range(target.settings.perception_number):
            self.add(Perception(index))

    @property
    def functions(self):
        return self.__functions

    @property
    def length(self):
        return len(self.__functions)

    def get_function(self, index):
        return self.__functions[index]

    def add(self, func):
        self.__functions.append(func)

    def get_random_index(self):
        return math.floor(random.random() * (self.length - 1)) + 1

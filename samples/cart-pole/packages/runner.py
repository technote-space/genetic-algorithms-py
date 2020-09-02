import time
import sys
from .finished import Finished


class Runner:
    def __init__(self, context, algorithm):
        sys.setrecursionlimit(2500)
        self.__context = context
        self.__algorithm = algorithm

    def start(self):
        while True:
            try:
                self.__episode()

            except Finished:
                pass

            time.sleep(2)

    def __episode(self):
        self.__context.reset()
        self.__algorithm.start()

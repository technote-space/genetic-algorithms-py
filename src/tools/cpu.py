import psutil
from grape import FitnessHelper


class Cpu:
    """
    Description:
    ------------
    CPU負荷対応ツール
    """

    def __init__(self, percent, count=3):
        self.__percent = min(90, max(5, percent))
        self.__index = 0
        self.__started = False
        self.__count = max(1, count)
        self.__history = [0] * self.__count

    def run(self):
        self.__history[self.__index] = psutil.cpu_percent(interval=None)
        self.__index = (self.__index + 1) % self.__count

        if not self.__started:
            self.__started = self.__index == 0
        if self.__started:
            percent = sum(self.__history) / self.__count
            FitnessHelper.sleep *= percent / self.__percent

            print(percent)

        print(self.__history)
        print(FitnessHelper.sleep)

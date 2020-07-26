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
        self.__cpu_history = [0] * self.__count
        self.__prev_sleep = FitnessHelper.sleep

    def run(self):
        self.__cpu_history[self.__index] = psutil.cpu_percent(interval=None)
        self.__index = (self.__index + 1) % self.__count

        count = self.__count
        if not self.__started:
            self.__started = self.__index == 0
            if not self.__started:
                count = self.__index

        percent = sum(self.__cpu_history) / count
        FitnessHelper.sleep = FitnessHelper.sleep * percent / self.__percent * 0.7 + self.__prev_sleep * 0.3
        self.__prev_sleep = FitnessHelper.sleep

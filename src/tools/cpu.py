import psutil
from grape import FitnessHelper


class Cpu:
    """
    Description:
    ------------
    CPU負荷対応ツール
    """

    def __init__(self, percent, rate=0.7):
        self.__percent = min(90, max(5, percent))
        self.__rate = rate
        self.__prev_percent = psutil.cpu_percent(interval=None)
        self.__prev_sleep = FitnessHelper.sleep

    def run(self):
        percent = psutil.cpu_percent(interval=None) * self.__rate + self.__prev_percent * (1 - self.__rate)
        FitnessHelper.sleep = FitnessHelper.sleep * percent / self.__percent * self.__rate + self.__prev_sleep * (1 - self.__rate)

        self.__prev_percent = percent
        self.__prev_sleep = FitnessHelper.sleep

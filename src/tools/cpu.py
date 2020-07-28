import psutil  # type: ignore
import multiprocessing
import threading
import time
from grape import FitnessHelper


class Cpu:
    """
    Description:
    ------------
    CPU負荷対応ツール
    """

    __percent: float
    __rate: float
    __interval: float
    __prev_percent: float
    __prev_sleep: float

    def __init__(self, percent: float, rate: float = 0.7, interval: float = 5) -> None:
        self.__percent = min(90.0, max(5.0, percent))
        self.__rate = rate
        self.__interval = max(1.0, interval)
        self.__prev_percent = percent
        self.__prev_sleep = 0.1
        self.__start()

    def __start(self) -> None:
        t = threading.Thread(target=self.__run, daemon=True)
        t.start()

    def __run(self) -> None:
        while True:
            percent: float = psutil.cpu_percent(interval=None)  # type: ignore
            percent = percent * self.__rate + self.__prev_percent * (1 - self.__rate)
            FitnessHelper.sleep = max(0.001, min(2.0, FitnessHelper.sleep * percent / self.__percent * self.__rate + self.__prev_sleep * (1 - self.__rate)))
            if FitnessHelper.sleep > 1:
                prev = FitnessHelper.pool_size
                FitnessHelper.pool_size = max(1, FitnessHelper.pool_size - 1)
                if FitnessHelper.pool_size < prev:
                    FitnessHelper.sleep /= 2
            elif FitnessHelper.sleep < 0.1:
                prev = FitnessHelper.pool_size
                FitnessHelper.pool_size = min(multiprocessing.cpu_count(), FitnessHelper.pool_size + 1)
                if FitnessHelper.pool_size > prev:
                    FitnessHelper.sleep *= 2

            self.__prev_percent = percent
            self.__prev_sleep = FitnessHelper.sleep

            time.sleep(self.__interval)

import time


class Runner:
    """
    Description:
    ------------
    実行ヘルパー
    """

    def __init__(self, algorithm, sleep=1):
        self.__algorithm = algorithm
        self.__sleep = sleep
        self.__main()

    def __main(self):
        while not self.__algorithm.has_reached:
            self.__algorithm.step()
            if self.__sleep > 0:
                time.sleep(self.__sleep)

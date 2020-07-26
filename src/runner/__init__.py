from tools import Cpu


class Runner:
    """
    Description:
    ------------
    実行ヘルパー
    """

    def __init__(self, algorithm, percent):
        self.__algorithm = algorithm
        self.__cpu = Cpu(percent)
        self.__main()

    def __main(self):
        while not self.__algorithm.has_reached:
            self.__algorithm.step()
            self.__cpu.run()

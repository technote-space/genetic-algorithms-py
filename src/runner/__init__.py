from tools import Cpu
from ga import IAlgorithm


class Runner:
    """
    Description:
    ------------
    実行ヘルパー
    """

    __algorithm: IAlgorithm

    def __init__(self, algorithm: IAlgorithm, percent: float) -> None:
        Cpu(percent)
        self.__algorithm = algorithm
        self.__main()

    def __main(self) -> None:
        while not self.__algorithm.has_reached:
            self.__algorithm.step()

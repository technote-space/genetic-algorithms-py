from ga import AbstractTermination, IAlgorithm


class Termination(AbstractTermination):
    """
    Description:
    ------------
    終了条件クラス
    """

    __offspring_number: int

    def __init__(self, offspring_number: int) -> None:
        super().__init__()
        self.__offspring_number = offspring_number

    def _perform_has_reached(self, algorithm: IAlgorithm) -> bool:
        return algorithm.offspring_number >= self.__offspring_number

    def _perform_get_progress(self, algorithm: IAlgorithm) -> float:
        return algorithm.offspring_number / self.__offspring_number

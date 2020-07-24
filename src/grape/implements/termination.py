from ga import AbstractTermination


class Termination(AbstractTermination):
    """
    Description:
    ------------
    終了条件クラス
    """

    def __init__(self, offspring_number):
        super().__init__()
        self.__offspring_number = offspring_number

    def _perform_get_progress(self, algorithm):
        return algorithm.offspring_number / self.__offspring_number

    def _perform_has_reached(self, algorithm):
        return algorithm.offspring_number >= self.__offspring_number

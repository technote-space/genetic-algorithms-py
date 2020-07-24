from abc import abstractmethod
from ..interfaces import IFitness


class AbstractFitness(IFitness):
    """
    Description:
    ------------
    適応度の基底クラス
    """

    @abstractmethod
    def evaluate(self, chromosome):
        pass

from abc import abstractmethod
from ..interfaces import IFitness, IChromosome


class AbstractFitness(IFitness):
    """
    Description:
    ------------
    適応度の基底クラス
    """

    @abstractmethod
    def evaluate(self, chromosome: IChromosome) -> None:
        pass

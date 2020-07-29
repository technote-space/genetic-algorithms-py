from typing import List
from ga import AbstractReinsertion, IChromosome


class CulturalReinsertion(AbstractReinsertion):
    """
    Description:
    ------------
    異文化型島モデルの挿入クラス
    """

    def select(self, population: List[IChromosome], offspring: List[IChromosome], parents: List[IChromosome], size: int) -> List[IChromosome]:
        return population + offspring

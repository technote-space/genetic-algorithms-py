from typing import List, Iterable, Callable
from ga import AbstractCrossover, IChromosome


class CulturalCrossover(AbstractCrossover):
    """
    Description:
    ------------
    異文化型島モデルの交叉クラス
    """

    def __init__(self) -> None:
        super().__init__(0, 2, 2)

    def _perform_cross(self, parents: List[IChromosome]) -> Iterable[IChromosome]:
        lambda_func: Callable[[IChromosome], IChromosome] = lambda parent: parent.clone()
        return map(lambda_func, parents)

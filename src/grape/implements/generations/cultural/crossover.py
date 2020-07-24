from ga import AbstractCrossover


class CulturalCrossover(AbstractCrossover):
    """
    Description:
    ------------
    異文化型島モデルの交叉クラス
    """

    def __init__(self):
        super().__init__(2, 2)

    def _perform_cross(self, parents, probability):
        return map(lambda parent: parent.clone(), parents)

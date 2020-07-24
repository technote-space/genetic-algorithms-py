from ga import AbstractReinsertion


class CulturalReinsertion(AbstractReinsertion):
    """
    Description:
    ------------
    異文化型島モデルの挿入クラス
    """

    def select(self, population, offspring, parents, size):
        return population + offspring

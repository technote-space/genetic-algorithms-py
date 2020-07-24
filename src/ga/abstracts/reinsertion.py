from abc import abstractmethod
from ..interfaces import IReinsertion


class AbstractReinsertion(IReinsertion):
    """
    Description:
    ------------
    挿入の基底クラス
    """

    @abstractmethod
    def select(self, population, offspring, parents, size):
        pass

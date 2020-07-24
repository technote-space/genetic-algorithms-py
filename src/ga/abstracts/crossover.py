from abc import abstractmethod
from ..interfaces import ICrossover


class AbstractCrossover(ICrossover):
    """
    Description:
    ------------
    交叉の基底クラス
    """

    def __init__(self, parents_number, children_number):
        super().__init__(parents_number, children_number)

    def cross(self, parents, probability):
        if len(parents) != self.parents_number:
            raise Exception('Length is not same.')

        offspring = list(self._perform_cross(parents, probability))
        if len(offspring) != self.children_number:
            raise Exception('Length is not same')

        return offspring

    @abstractmethod
    def _perform_cross(self, parents, probability):
        pass

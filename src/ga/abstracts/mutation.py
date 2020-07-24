import random
from ..interfaces import IMutation


class AbstractMutation(IMutation):
    """
    Description:
    ------------
    突然変異の基底クラス
    """

    def mutate(self, chromosome, probability):
        for index in range(chromosome.length):
            if random.random() < probability:
                chromosome.mutation(index)

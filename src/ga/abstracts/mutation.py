import random
from ..interfaces import IMutation, IChromosome


class AbstractMutation(IMutation):
    """
    Description:
    ------------
    突然変異の基底クラス
    """

    def mutate(self, chromosome: IChromosome, probability: float) -> None:
        for index in range(chromosome.length):
            if random.random() < probability:
                chromosome.mutation(index)

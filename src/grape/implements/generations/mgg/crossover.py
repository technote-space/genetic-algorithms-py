import random
from ga import AbstractCrossover


class MggCrossover(AbstractCrossover):
    """
    Description:
    ------------
    MGGの交叉クラス
    """

    def __init__(self, mix_probability, crossover_time):
        super().__init__(2, crossover_time * 2)

        # [0, 0.5)
        self.__mix_probability = min(max(mix_probability if mix_probability < 0.5 else 1 - mix_probability, 0), 0.5)
        self.__crossover_time = crossover_time

    def _perform_cross(self, parents, probability):
        parent1 = parents[0]
        parent2 = parents[1]

        offspring = []
        for _ in range(self.__crossover_time):
            child1 = parent1.clone()
            child2 = parent2.clone()

            if probability > 0 and random.random() < probability:
                for index in range(parent1.length):
                    if random.random() < self.__mix_probability:
                        child1.set_acid(index, parent2.get_acid(index))
                        child2.set_acid(index, parent1.get_acid(index))

            offspring.append(child1)
            offspring.append(child2)

        return offspring

from ga import AbstractFitness


class Fitness(AbstractFitness):
    """
    Description:
    ------------
    適応度クラス
    """

    def __init__(self, dataset):
        self.__dataset = dataset

    def evaluate(self, chromosome):
        chromosome.phenotype.calc_fitness(self.__dataset)

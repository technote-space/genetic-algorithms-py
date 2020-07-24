from ga import AbstractFitness


class Fitness(AbstractFitness):
    """
    Description:
    ------------
    適応度クラス
    """

    def __init__(self, dataset, functions):
        self.__dataset = dataset
        self.__functions = functions

    def evaluate(self, chromosome):
        chromosome.phenotype.calc_fitness(self.__dataset, self.__functions)

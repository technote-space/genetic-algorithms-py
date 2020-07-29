from ga import AbstractFitness, IChromosome
from ..interfaces import IGenotype, ITestDataset


class Fitness(AbstractFitness):
    """
    Description:
    ------------
    適応度クラス
    """

    __dataset: ITestDataset

    def __init__(self, dataset: ITestDataset) -> None:
        self.__dataset = dataset

    def evaluate(self, chromosome: IChromosome) -> None:
        if isinstance(chromosome, IGenotype):
            chromosome.phenotype.calc_fitness(self.__dataset)

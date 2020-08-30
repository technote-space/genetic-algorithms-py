from ga import AbstractFitness, IChromosome
from ..interfaces import IGenotype, ITestDataset
from .phenotype import Phenotype


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
            step, action_step, fitness = Phenotype.run_episodes(chromosome, self.__dataset)
            chromosome.set_fitness(fitness, step, action_step)

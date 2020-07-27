from multiprocessing import Pool
import time
from targets import get_target
from .genotype import Genotype
from .function_set import FunctionSet
from .test import TestData, TestDataset


def evaluate(args):
    target, chromosomes, sleep = args

    target_instance = get_target(target)
    dataset = TestDataset(target_instance.ga_settings.test_number, TestData(target))
    functions = FunctionSet(target_instance)
    genotype = Genotype(0, functions)

    genotype.create_from_nodes(chromosomes)
    genotype.phenotype.calc_fitness(dataset, functions)

    time.sleep(sleep)

    return genotype.fitness, genotype.step


class FitnessHelper:
    """
    Description:
    ------------
    適応度計算ツール
    """

    pool_size = 6
    sleep = 0.1

    def __init__(self, target):
        self.__target = target

    def run(self, chromosomes):
        with Pool(FitnessHelper.pool_size) as pool:
            results = pool.map(evaluate, map(lambda x: (self.__target, x.acids, FitnessHelper.sleep), chromosomes))

        for index, chromosome in enumerate(chromosomes):
            chromosome.phenotype.set_fitness(results[index][0], results[index][1])

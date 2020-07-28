import time
from typing import Tuple, List, Callable
from multiprocessing import Pool
from ga import IChromosome
from targets import get_target
from .genotype import Genotype
from .function_set import FunctionSet
from .test import TestData, TestDataset
from ..interfaces import IGenotype


def evaluate(args: Tuple[str, List[int], float]) -> Tuple[float, float]:
    target, chromosomes, sleep = args

    target_instance = get_target(target)
    dataset = TestDataset(target_instance.ga_settings.test_number, TestData(target))
    functions = FunctionSet(target_instance)
    genotype = Genotype(0, functions)

    genotype.create_from_nodes(chromosomes)
    genotype.phenotype.calc_fitness(dataset)

    time.sleep(sleep)

    return genotype.fitness, genotype.step


class FitnessHelper:
    """
    Description:
    ------------
    適応度計算ツール
    """

    pool_size: int = 4
    sleep: float = 0.1
    __target: str

    def __init__(self, target: str) -> None:
        self.__target = target

    def run(self, chromosomes: List[IChromosome]) -> None:
        filter_func: Callable[[IChromosome], Tuple[str, List[int], float]] = lambda x: (self.__target, x.acids, FitnessHelper.sleep)
        with Pool(FitnessHelper.pool_size) as pool:
            results = pool.map(evaluate, map(filter_func, chromosomes))

        for index, chromosome in enumerate(chromosomes):
            if isinstance(chromosome, IGenotype):
                chromosome.phenotype.set_fitness(results[index][0], results[index][1])

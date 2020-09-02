import time
from typing import Tuple, List, Callable
from multiprocessing import Pool
from ga import IChromosome
from tasks import get_task
from .genotype import Genotype
from .function_set import FunctionSet
from .test import TestData, TestDataset
from .phenotype import Phenotype
from ..interfaces import IGenotype


def evaluate(args: Tuple[str, List[int], float]) -> Tuple[float, float, float]:
    task_name, chromosomes, sleep = args

    task = get_task(task_name)
    dataset = TestDataset(task.ga_settings.test_number, TestData(task_name))
    functions = FunctionSet(task.settings.action_number, task.settings.perception_number)
    genotype = Genotype(0, functions)

    genotype.create_from_nodes(chromosomes)
    step, action_step, fitness = Phenotype.run_episodes(genotype, dataset)

    time.sleep(sleep)

    return fitness, step, action_step


class FitnessHelper:
    """
    Description:
    ------------
    適応度計算ツール
    """

    pool_size: int = 4
    sleep: float = 0.1
    __task_name: str

    def __init__(self, task_name: str) -> None:
        self.__task_name = task_name

    def run(self, chromosomes: List[IChromosome]) -> None:
        filter_func: Callable[[IChromosome], Tuple[str, List[int], float]] = lambda x: (self.__task_name, x.acids, FitnessHelper.sleep)
        with Pool(FitnessHelper.pool_size) as pool:
            results = pool.map(evaluate, map(filter_func, chromosomes))

        for index, chromosome in enumerate(chromosomes):
            if isinstance(chromosome, IGenotype):
                chromosome.set_fitness(results[index][0], results[index][1], results[index][2])

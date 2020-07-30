import json
import os
from typing import List
from ga import IAlgorithm, IChromosome
from target import ITarget


class IO:
    """
    Description:
    ------------
    入出力ツール
    """

    __name: str
    __result: str

    def __init__(self, name: str, result: str) -> None:
        self.__name = name
        self.__result = result
        if self.__result and os.path.exists(os.path.join(os.getcwd(), self.__result)):
            os.remove(os.path.join(os.getcwd(), self.__result))

    def save_chromosome(self, _algorithm: IAlgorithm, _target: ITarget, chromosome: IChromosome) -> None:
        if self.__name:
            with open(os.path.join(os.getcwd(), self.__name), mode='w') as f:
                f.write(json.dumps(chromosome.acids, ensure_ascii=False))

    def load_chromosome(self) -> List[int]:
        if self.__name:
            with open(os.path.join(os.getcwd(), self.__name), mode='r') as f:
                return json.load(f)  # type: ignore
        raise Exception('[name] is not specified')

    def save_result(self, algorithm: IAlgorithm, _target: ITarget, _chromosome: IChromosome) -> None:
        if self.__result:
            with open(os.path.join(os.getcwd(), self.__result), mode='a') as f:
                f.write(f'{algorithm.progress} {algorithm.fitness}\n')

    @staticmethod
    def draw(algorithm: IAlgorithm, target: ITarget, _chromosome: IChromosome) -> None:
        target.draw()

        print(f'{algorithm.progress:.3f}', f'{algorithm.fitness:.3f}')
        print(f'{target.get_fitness():.3f}', target.step, target.action_step)
        print()

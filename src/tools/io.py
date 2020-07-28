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

    def __init__(self, name: str) -> None:
        self.__name = name

    def save_chromosome(self, _algorithm: IAlgorithm, _target: ITarget, chromosome: IChromosome) -> None:
        if self.__name:
            with open(os.path.join(os.getcwd(), self.__name), mode='w') as f:
                f.write(json.dumps(chromosome.acids, ensure_ascii=False))

    def load_chromosome(self) -> List[int]:
        if self.__name:
            with open(os.path.join(os.getcwd(), self.__name), mode='r') as f:
                return json.load(f)  # type: ignore
        raise Exception('[name] is not specified')

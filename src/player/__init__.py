import time
from typing import List
from targets import get_target
from grape import Genotype, FunctionSet, IFunctionSet, IGenotype


class Player:
    """
    Description:
    ------------
    再生ヘルパー
    """

    __target: str
    __functions: IFunctionSet
    __genotype: IGenotype

    def __init__(self, target: str, chromosome: List[int]) -> None:
        self.__target = target

        functions = FunctionSet(get_target(target))
        self.__functions = functions
        self.__genotype = Genotype(0, functions)
        self.__genotype.create_from_nodes(chromosome)
        self.__reset()
        self.__main()

    def __reset(self) -> None:
        self.__context = self.__genotype.phenotype.get_context(get_target(self.__target, True))

    def __main(self) -> None:
        while True:
            while not self.__context.target.has_reached:
                self.__genotype.phenotype.until_action(self.__context)
                self.__context.target.render()
                time.sleep(1.0 / self.__context.target.settings.fps)

            time.sleep(2)
            self.__reset()

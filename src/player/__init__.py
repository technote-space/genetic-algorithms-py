import time
from typing import List, Optional
from targets import get_target
from grape import Genotype, FunctionSet, IGenotype, IContext, Phenotype


class Player:
    """
    Description:
    ------------
    再生ヘルパー
    """

    __target: str
    __chromosome: List[int]
    __genotype: IGenotype
    __context: Optional[IContext]

    def __init__(self, target: str, chromosome: List[int]) -> None:
        self.__target = target
        self.__chromosome = chromosome
        self.__context = None
        self.__reset()
        self.__main()

    def __reset(self) -> None:
        if self.__context:
            self.__context.target.close()
        target = get_target(self.__target, True)
        self.__genotype = Genotype(0, FunctionSet(target.settings.action_number, target.settings.perception_number))
        self.__genotype.create_from_nodes(self.__chromosome)
        self.__context = Phenotype.get_context(self.__genotype, target)

    def __main(self) -> None:
        if not self.__context:
            return
        while True:
            while not self.__context.target.has_reached:
                Phenotype.until_action(self.__genotype, self.__context)
                self.__context.target.render()
                time.sleep(1.0 / self.__context.target.settings.fps)

            time.sleep(2)
            self.__reset()

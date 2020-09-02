import time
from typing import List, Optional
from tasks import get_task
from grape import Genotype, FunctionSet, IGenotype, IContext, Phenotype


class Player:
    """
    Description:
    ------------
    再生ヘルパー
    """

    __task_name: str
    __chromosome: List[int]
    __genotype: IGenotype
    __context: Optional[IContext]

    def __init__(self, task_name: str, chromosome: List[int]) -> None:
        self.__task_name = task_name
        self.__chromosome = chromosome
        self.__context = None
        self.__reset()
        self.__main()

    def __reset(self) -> None:
        if self.__context:
            self.__context.task.close()
        task = get_task(self.__task_name, True)
        self.__genotype = Genotype(0, FunctionSet(task.settings.action_number, task.settings.perception_number))
        self.__genotype.create_from_nodes(self.__chromosome)
        self.__context = Phenotype.get_context(self.__genotype, task)

    def __main(self) -> None:
        if not self.__context:
            return
        while True:
            while not self.__context.task.has_reached:
                Phenotype.until_action(self.__genotype, self.__context)
                self.__context.task.render()
                time.sleep(1.0 / self.__context.task.settings.fps)

            time.sleep(2)
            self.__reset()

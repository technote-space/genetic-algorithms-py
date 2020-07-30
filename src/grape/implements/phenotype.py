from typing import Tuple, List
from target import ITarget
from .context import Context
from .functions import Perception
from ..interfaces import IPhenotype, IGenotype, ITestDataset, IContext, IFuncBlock


class Phenotype(IPhenotype):
    """
    Description:
    ------------
    表現型
    """

    __genotype: IGenotype
    __fitness: float
    __step: float
    __action_step: float

    def __init__(self, genotype: IGenotype) -> None:
        self.__genotype = genotype
        self.__fitness = -1
        self.__step = 0
        self.__action_step = 0

    @property
    def fitness(self) -> float:
        return self.__fitness

    @property
    def step(self) -> float:
        return self.__step

    @property
    def action_step(self) -> float:
        return self.__action_step

    @property
    def genotype(self) -> IGenotype:
        return self.__genotype

    def calc_fitness(self, dataset: ITestDataset) -> None:
        step, action_step, fitness = self._run_episodes(dataset)
        self.__fitness = fitness
        self.__step = step
        self.__action_step = action_step

    def set_fitness(self, fitness: float, step: float, action_step: float) -> None:
        self.__fitness = fitness
        self.__step = step
        self.__action_step = action_step

    def _run_episodes(self, dataset: ITestDataset) -> Tuple[float, float, float]:
        sum_steps: float = 0
        sum_action_steps: float = 0
        sum_score: float = 0

        # noinspection PyBroadException
        try:
            for target in dataset.create_dataset():
                result = self._episode(target)
                sum_steps += result[0]
                sum_action_steps += result[1]
                sum_score += result[2]
        except Exception:
            return 0, 0, 0

        return sum_steps / dataset.length, sum_action_steps / dataset.length, sum_score / dataset.length

    @staticmethod
    def _next(node: List[int], context: IContext) -> None:
        context.functions.get_function(node[0]).execute(node[1], node[2], context)

    def until_action(self, context: IContext) -> None:
        while not context.target.has_reached:
            node = self.__genotype.get_node_genes(context.current)
            func = context.functions.get_function(node[0])
            func.execute(node[1], node[2], context)
            if type(func) is not Perception:
                break

    def while_end(self, context: IContext) -> None:
        while not context.target.has_reached:
            node = self.__genotype.get_node_genes(context.current)
            self._next(node, context)

    def get_context(self, target: ITarget, current: int = 0) -> IContext:
        return Context(target, current, self.__genotype.node_count, self.genotype.functions, self)

    def _episode(self, target: ITarget) -> Tuple[float, float, float]:
        context = self.get_context(target)
        self.while_end(context)

        return context.target.step, context.target.action_step, context.target.get_fitness()

    def get_programming(self, target: ITarget) -> List[IFuncBlock]:
        blocks = {}
        stack = [0]
        while len(stack) > 0:
            current = stack.pop()
            if current in blocks:
                continue

            node = self.genotype.get_node_genes(current)
            func = self.genotype.functions.get_function(node[0])
            context = self.get_context(target, current)
            blocks[current] = func.programming(node[1], node[2], context)
            for c in func.get_possible_connections(node[1], node[2], context):
                stack.append(c)

        return list(blocks.values())

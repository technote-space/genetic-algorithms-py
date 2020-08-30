from typing import Tuple, List
from target import ITarget
from .context import Context
from .functions import Perception
from ..interfaces import IGenotype, ITestDataset, IContext, IFuncBlock


class Phenotype:
    """
    Description:
    ------------
    表現型
    """

    @staticmethod
    def run_episodes(genotype: IGenotype, dataset: ITestDataset) -> Tuple[float, float, float]:
        sum_steps: float = 0
        sum_action_steps: float = 0
        sum_score: float = 0

        # noinspection PyBroadException
        try:
            for target in dataset.create_dataset():
                result = Phenotype._episode(genotype, target)
                sum_steps += result[0]
                sum_action_steps += result[1]
                sum_score += result[2]
        except Exception:
            return 0, 0, 0

        return sum_steps / dataset.length, sum_action_steps / dataset.length, sum_score / dataset.length

    @staticmethod
    def _next(node: List[int], context: IContext) -> None:
        context.functions.get_function(node[0]).execute(node[1], node[2], context)

    @staticmethod
    def until_action(genotype: IGenotype, context: IContext) -> None:
        while not context.target.has_reached:
            node = genotype.get_node_genes(context.current)
            func = context.functions.get_function(node[0])
            func.execute(node[1], node[2], context)
            if type(func) is not Perception:
                break

    @staticmethod
    def while_end(genotype: IGenotype, context: IContext) -> None:
        while not context.target.has_reached:
            node = genotype.get_node_genes(context.current)
            Phenotype._next(node, context)

    @staticmethod
    def get_context(genotype: IGenotype, target: ITarget, current: int = 0) -> IContext:
        return Context(target, current, genotype.node_count, genotype.functions)

    @staticmethod
    def _episode(genotype: IGenotype, target: ITarget) -> Tuple[float, float, float]:
        context = Phenotype.get_context(genotype, target)
        Phenotype.while_end(genotype, context)

        return context.target.step, context.target.action_step, context.target.get_fitness()

    @staticmethod
    def get_programming(genotype: IGenotype, target: ITarget) -> List[IFuncBlock]:
        blocks = {}
        stack = [0]
        while len(stack) > 0:
            current = stack.pop()
            if current in blocks:
                continue

            node = genotype.get_node_genes(current)
            func = genotype.functions.get_function(node[0])
            context = Phenotype.get_context(genotype, target, current)
            blocks[current] = func.programming(node[1], node[2], context)
            for c in func.get_possible_connections(node[1], node[2], context):
                stack.append(c)

        return list(blocks.values())

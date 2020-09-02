from typing import Tuple, List
from task import ITask
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
            for task in dataset.create_dataset():
                result = Phenotype._episode(genotype, task)
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
        while not context.task.has_reached:
            node = genotype.get_node_genes(context.current)
            func = context.functions.get_function(node[0])
            func.execute(node[1], node[2], context)
            if type(func) is not Perception:
                break

    @staticmethod
    def while_end(genotype: IGenotype, context: IContext) -> None:
        while not context.task.has_reached:
            node = genotype.get_node_genes(context.current)
            Phenotype._next(node, context)

    @staticmethod
    def get_context(genotype: IGenotype, task: ITask, current: int = 0) -> IContext:
        return Context(task, current, genotype.node_count, genotype.functions)

    @staticmethod
    def _episode(genotype: IGenotype, task: ITask) -> Tuple[float, float, float]:
        context = Phenotype.get_context(genotype, task)
        Phenotype.while_end(genotype, context)

        return context.task.step, context.task.action_step, context.task.get_fitness()

    @staticmethod
    def get_programming(genotype: IGenotype, task: ITask) -> List[IFuncBlock]:
        blocks = {}
        stack = [0]
        while len(stack) > 0:
            current = stack.pop()
            if current in blocks:
                continue

            node = genotype.get_node_genes(current)
            func = genotype.functions.get_function(node[0])
            context = Phenotype.get_context(genotype, task, current)
            blocks[current] = func.programming(node[1], node[2], context)
            for c in func.get_possible_connections(node[1], node[2], context):
                stack.append(c)

        return list(blocks.values())

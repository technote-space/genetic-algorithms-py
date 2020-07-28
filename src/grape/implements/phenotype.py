from .context import Context
from .functions import Perception


class Phenotype:
    """
    Description:
    ------------
    表現型
    """

    def __init__(self, genotype):
        self.__genotype = genotype
        self.__fitness = -1
        self.__step = 0

    @property
    def fitness(self):
        return self.__fitness

    @property
    def step(self):
        return self.__step

    @property
    def genotype(self):
        return self.__genotype

    def calc_fitness(self, dataset):
        step, fitness = self._run_episodes(dataset)
        self.__fitness = fitness
        self.__step = step

    def set_fitness(self, fitness, step):
        self.__fitness = fitness
        self.__step = step

    def _run_episodes(self, dataset):
        sum_score = 0
        sum_steps = 0

        # noinspection PyBroadException
        try:
            for target in dataset.create_dataset():
                result = self._episode(target)
                sum_steps += result[0]
                sum_score += result[1]
        except Exception:
            return 0, 0

        return sum_steps / dataset.length, sum_score / dataset.length

    @staticmethod
    def _next(node, context):
        context.functions.get_function(node[0]).execute(node[1], node[2], context)

    def until_action(self, context):
        while not context.target.has_reached:
            node = self.__genotype.get_node_genes(context.current)
            func = context.functions.get_function(node[0])
            func.execute(node[1], node[2], context)
            if type(func) is not Perception:
                break

    def while_end(self, context):
        while not context.target.has_reached:
            node = self.__genotype.get_node_genes(context.current)
            self._next(node, context)

    def get_context(self, target, current=0):
        return Context(target, current, self.__genotype.node_count, self.genotype.functions, self)

    def _episode(self, target):
        context = self.get_context(target)
        self.while_end(context)

        return context.target.step, context.target.get_fitness()

    def get_programming(self, target):
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

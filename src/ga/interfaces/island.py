from abc import ABCMeta, abstractmethod


class IIsland(metaclass=ABCMeta):
    """
    Description:
    ------------
    島モデルにおける島のinterface
    """

    def __init__(
            self,
            population,
            fitness,
            selection,
            crossover,
            crossover_probability,
            mutation,
            mutation_probability,
            reinsertion
    ):
        self.__population = population
        self.__fitness = fitness
        self.__selection = selection
        self.__crossover = crossover
        self.__crossover_probability = crossover_probability
        self.__mutation = mutation
        self.__mutation_probability = mutation_probability
        self.__reinsertion = reinsertion

    @property
    def population(self):
        return self.__population

    @property
    def fitness(self):
        return self.__fitness

    @property
    def selection(self):
        return self.__selection

    @property
    def crossover(self):
        return self.__crossover

    @property
    def crossover_probability(self):
        return self.__crossover_probability

    @property
    def mutation(self):
        return self.__mutation

    @property
    def mutation_probability(self):
        return self.__mutation_probability

    @property
    def reinsertion(self):
        return self.__reinsertion

    @property
    @abstractmethod
    def initialized(self):
        pass

    @property
    @abstractmethod
    def generation_number(self):
        pass

    @property
    @abstractmethod
    def offspring_number(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def step(self):
        pass

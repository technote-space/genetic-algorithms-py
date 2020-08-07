from abc import ABCMeta, abstractmethod
from .population import IPopulation
from .fitness import IFitness
from .selection import ISelection
from .crossover import ICrossover
from .mutation import IMutation
from .reinsertion import IReinsertion


class IIsland(metaclass=ABCMeta):
    """
    Description:
    ------------
    島モデルにおける島のinterface
    """

    __population: IPopulation
    __fitness: IFitness
    __selection: ISelection
    __crossover: ICrossover
    __mutation: IMutation
    __reinsertion: IReinsertion
    __evaluate_parents_fitness: bool

    def __init__(
        self,
        population: IPopulation,
        fitness: IFitness,
        selection: ISelection,
        crossover: ICrossover,
        mutation: IMutation,
        reinsertion: IReinsertion,
        evaluate_parents_fitness: bool
    ):
        self.__population = population
        self.__fitness = fitness
        self.__selection = selection
        self.__crossover = crossover
        self.__mutation = mutation
        self.__reinsertion = reinsertion
        self.__evaluate_parents_fitness = evaluate_parents_fitness

    @property
    def population(self) -> IPopulation:
        return self.__population

    @property
    def fitness(self) -> IFitness:
        return self.__fitness

    @property
    def selection(self) -> ISelection:
        return self.__selection

    @property
    def crossover(self) -> ICrossover:
        return self.__crossover

    @property
    def mutation(self) -> IMutation:
        return self.__mutation

    @property
    def reinsertion(self) -> IReinsertion:
        return self.__reinsertion

    @property
    def evaluate_parents_fitness(self) -> bool:
        return self.__evaluate_parents_fitness

    @property
    @abstractmethod
    def initialized(self) -> bool:
        pass

    @property
    @abstractmethod
    def generation_number(self) -> int:
        pass

    @property
    @abstractmethod
    def offspring_number(self) -> int:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def step(self) -> None:
        pass

from abc import abstractmethod
from typing import List
from ..interfaces import IIsland, IPopulation, IFitness, ISelection, ICrossover, IMutation, IReinsertion, IChromosome


class AbstractIsland(IIsland):
    """
    Description:
    ------------
    島モデルにおける島の基底クラス
    """

    __generation_number: int
    __offspring_number: int
    __initialized: bool

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
        super().__init__(
            population,
            fitness,
            selection,
            crossover,
            mutation,
            reinsertion,
            evaluate_parents_fitness
        )

        self.__generation_number = 0
        self.__offspring_number = 0
        self.__initialized = False

    @property
    def initialized(self) -> bool:
        return self.__initialized

    @property
    def generation_number(self) -> int:
        return self.__generation_number

    @property
    def offspring_number(self) -> int:
        return self.__offspring_number

    def reset(self) -> None:
        self.__initialized = False
        self.population.init()

        for chromosome in self.population.chromosomes:
            self.fitness.evaluate(chromosome)
        self.__generation_number = 0
        self.__offspring_number = 0
        self._perform_reset()
        self.__initialized = True

    def _perform_reset(self) -> None:
        pass

    def _perform_mutate(self, chromosomes: List[IChromosome]) -> None:
        for chromosome in chromosomes:
            self.mutation.mutate(chromosome)

    @abstractmethod
    def _evaluate(self, chromosomes: List[IChromosome]) -> None:
        pass

    def step(self) -> None:
        if not self.__initialized:
            self.reset()

        parents, population = self.selection.select(self.population.chromosomes)
        offspring = self.crossover.cross(parents)

        self._perform_mutate(offspring)
        self._evaluate(offspring)
        if self.evaluate_parents_fitness:
            self._evaluate(parents)

        self.population.update(self.reinsertion.select(population, offspring, parents, self.population.size))
        self.__generation_number += 1
        self.__offspring_number += len(offspring)
        self._perform_step()

    def _perform_step(self) -> None:
        pass

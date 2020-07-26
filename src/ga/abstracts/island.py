from ..interfaces import IIsland


class AbstractIsland(IIsland):
    """
    Description:
    ------------
    島モデルにおける島の基底クラス
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
        super().__init__(
            population,
            fitness,
            selection,
            crossover,
            crossover_probability,
            mutation,
            mutation_probability,
            reinsertion
        )

        self.__generation_number = 0
        self.__offspring_number = 0
        self.__initialized = False

    @property
    def initialized(self):
        return self.__initialized

    @property
    def generation_number(self):
        return self.__generation_number

    @property
    def offspring_number(self):
        return self.__offspring_number

    def reset(self):
        self.__initialized = False
        self.population.init()

        for chromosome in self.population.chromosomes:
            self.fitness.evaluate(chromosome)
        self.__generation_number = 0
        self.__offspring_number = 0
        self._perform_reset()
        self.__initialized = True

    def _perform_reset(self):
        pass

    def __evaluate_offspring(self, chromosome):
        self.mutation.mutate(chromosome, self.mutation_probability)
        self.fitness.evaluate(chromosome)

    def __evaluate_parents(self, chromosome):
        self.fitness.evaluate(chromosome)

    def step(self):
        if not self.__initialized:
            self.reset()

        parents, population = self.selection.select(self.population.chromosomes)
        offspring = self.crossover.cross(parents, self.crossover_probability)

        for chromosome in offspring:
            self.__evaluate_offspring(chromosome)
        for chromosome in parents:
            self.__evaluate_parents(chromosome)

        self.population.update(self.reinsertion.select(population, offspring, parents, self.population.size))
        self.__generation_number += 1
        self.__offspring_number += len(offspring)
        self._perform_step()

    def _perform_step(self):
        pass

import time
from grape import Genotype, FunctionSet


class Player:
    """
    Description:
    ------------
    再生ヘルパー
    """

    def __init__(self, target, chromosome):
        functions = FunctionSet(target)
        self.__target = target
        self.__genotype = Genotype(0, functions)
        self.__genotype.create_from_nodes(chromosome)
        self.__reset()
        self.__main()

    def __reset(self):
        target = self.__target.clone()
        target.on_player()
        functions = FunctionSet(target)
        self.__context = self.__genotype.phenotype.get_context(target, functions)

    def __main(self):
        while True:
            while not self.__context.target.has_reached:
                self.__genotype.phenotype.until_action(self.__context)
                self.__context.target.render()
                time.sleep(1.0 / self.__context.target.settings.fps)

            for _ in range(3):
                time.sleep(1)

            self.__reset()

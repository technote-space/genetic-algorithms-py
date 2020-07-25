import json
import os


class IO:
    """
    Description:
    ------------
    入出力ツール
    """

    def __init__(self, name):
        self.__name = name

    def save_chromosome(self, _algorithm, _target, chromosome):
        if self.__name:
            with open(os.path.join(os.getcwd(), self.__name), mode='w') as f:
                f.write(json.dumps(chromosome.acids, ensure_ascii=False))

    def load_chromosome(self):
        if self.__name:
            with open(os.path.join(os.getcwd(), self.__name), mode='r') as f:
                return json.load(f)

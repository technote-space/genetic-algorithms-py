from abc import ABCMeta, abstractmethod


class IMutation(metaclass=ABCMeta):
    """
    Description:
    ------------
    突然変異のinterface
    """

    @abstractmethod
    def mutate(self, chromosome, probability):
        pass

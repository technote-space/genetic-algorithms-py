from abc import ABCMeta, abstractmethod


class ISelection(metaclass=ABCMeta):
    """
    Description:
    ------------
    選択のinterface
    """

    @abstractmethod
    def select(self, chromosomes):
        pass

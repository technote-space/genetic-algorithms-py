from abc import ABCMeta, abstractmethod
from typing import List
from target import ITarget
from .block import IFuncBlock


class IPhenotype(metaclass=ABCMeta):
    """
    Description:
    ------------
    表現型のinterface
    """

    @property
    @abstractmethod
    def fitness(self) -> float:
        pass

    @property
    @abstractmethod
    def step(self) -> float:
        pass

    @property
    @abstractmethod
    def action_step(self) -> float:
        pass

    @property
    @abstractmethod
    def genotype(self) -> 'IGenotype':
        pass

    @abstractmethod
    def calc_fitness(self, dataset: 'ITestDataset') -> None:
        pass

    @abstractmethod
    def set_fitness(self, fitness: float, step: float, action_step: float) -> None:
        pass

    @abstractmethod
    def until_action(self, context: 'IContext') -> None:
        pass

    @abstractmethod
    def while_end(self, context: 'IContext') -> None:
        pass

    @abstractmethod
    def get_context(self, target: ITarget, current: int = 0) -> 'IContext':
        pass

    @abstractmethod
    def get_programming(self, target: ITarget) -> List[IFuncBlock]:
        pass


from .genotype import IGenotype  # noqa: E402
from .context import IContext  # noqa: E402
from .test import ITestDataset  # noqa: E402

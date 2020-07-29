from abc import ABCMeta, abstractmethod
from target import ITarget


class IContext(metaclass=ABCMeta):
    """
    Description:
    ------------
    コンテキストのinterface
    """

    @property
    @abstractmethod
    def target(self) -> ITarget:
        pass

    @property
    @abstractmethod
    def current(self) -> int:
        pass

    @property
    @abstractmethod
    def node_count(self) -> int:
        pass

    @property
    @abstractmethod
    def functions(self) -> 'IFunctionSet':
        pass

    @property
    @abstractmethod
    def phenotype(self) -> 'IPhenotype':
        pass

    @abstractmethod
    def set_current(self, current: int) -> None:
        pass


from .function_set import IFunctionSet  # noqa: E402
from .phenotype import IPhenotype  # noqa: E402

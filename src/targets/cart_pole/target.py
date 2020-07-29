from target import AbstractGymTarget
from .settings import Settings
from .ga_settings import GaSettings


class CartPole(AbstractGymTarget):
    """
    Description:
    ------------
    Cart Pole
    """

    def __init__(self) -> None:
        super().__init__('CartPole-v1', Settings, GaSettings)  # type: ignore

    def _perform_perceive(self, index: int) -> bool:
        return self.observation[index] < 0  # type: ignore

    def _correction_fitness(self) -> float:
        return (1 - abs(self.observation[0]) / 2.4) * 0.01  # type: ignore

    def get_perceive_expression(self, index: int, observation_name: str) -> str:
        return f'{observation_name}[{index}] < 0'

from target import AbstractGymTarget
from .settings import Settings
from .ga_settings import GaSettings


class CartPole(AbstractGymTarget):
    """
    Description:
    ------------
    Cart Pole
    """

    def __init__(self):
        super().__init__('CartPole-v1', Settings, GaSettings)

    def _perform_perceive(self, index):
        return self.observation[index] < 0

    def _correction_fitness(self):
        return (1 - abs(self.observation[0]) / 2.4) * 0.01

    def get_perceive_expression(self, index, observation_name):
        return f'{observation_name}[{index}] < 0'

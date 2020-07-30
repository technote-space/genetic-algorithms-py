from target import AbstractAtariTarget
from .settings import Settings
from .ga_settings import GaSettings


class Breakout(AbstractAtariTarget):
    """
    Description:
    ------------
    Breakout
    """

    def __init__(self) -> None:
        super().__init__('Breakout-ramNoFrameskip-v4', Settings, GaSettings)  # type: ignore

    def _perform_check_done(self, done: bool) -> bool:
        return done or self.observation[57] < 5  # type: ignore

    def _perform_perceive(self, index: int) -> bool:
        return int(self.observation[72]) - int(self.observation[99]) < -8  # type: ignore

    def _calc_fitness(self) -> float:
        return self.reward / 428

    def get_perceive_expression(self, index: int, observation_name: str) -> str:
        return f'int({observation_name}[72]) - int({observation_name}[99]) < -8'

    def get_finished_expression(self, done_name: str, observation_name: str) -> str:
        return f'{done_name} or {observation_name}[57] < 5'

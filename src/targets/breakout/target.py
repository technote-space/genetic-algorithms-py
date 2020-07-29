from typing import List, Tuple
from target import AbstractAtariTarget
from .settings import Settings
from .ga_settings import GaSettings


class Breakout(AbstractAtariTarget):
    """
    Description:
    ------------
    Breakout
    """

    __perception_settings: List[Tuple[int, float, float]] = [(72, 0, 16), (72, 16, 32), (72, 32, 48), (72, 48, 64), (72, 64, 80), (72, 80, 96), (72, 96, 112), (72, 112, 128),
                                                             (72, 128, 144), (72, 144, 160), (72, 160, 176), (72, 176, 192), (72, 192, 208), (72, 208, 224), (72, 224, 240),
                                                             (72, 240, 256), (99, 0, 16), (99, 16, 32), (99, 32, 48), (99, 48, 64), (99, 64, 80), (99, 80, 96), (99, 96, 112),
                                                             (99, 112, 128), (99, 128, 144), (99, 144, 160), (99, 160, 176), (99, 176, 192), (99, 192, 208), (99, 208, 224),
                                                             (99, 224, 240), (99, 240, 256), (101, 0, 16), (101, 16, 32), (101, 32, 48), (101, 48, 64), (101, 64, 80),
                                                             (101, 80, 96), (101, 96, 112), (101, 112, 128), (101, 128, 144), (101, 144, 160), (101, 160, 176), (101, 176, 192),
                                                             (101, 192, 208), (101, 208, 224), (101, 224, 240), (101, 240, 256)]

    def __init__(self) -> None:
        super().__init__('Breakout-ramNoFrameskip-v4', Settings, GaSettings)  # type: ignore
        self.__perceptions = {}
        for index, setting in enumerate(Breakout.__perception_settings):
            self.__perceptions[index] = self._get_perceive_function(setting[0], setting[1], setting[2])
        self.__max_position = 0

    def _perform_check_done(self, done: bool) -> bool:
        return done or self.observation[57] < 5  # type: ignore

    def _perform_perceive(self, index: int) -> bool:
        return self.__perceptions[index]()

    def _calc_fitness(self) -> float:
        return self.reward / 428

    def get_perceive_expression(self, index: int, observation_name: str) -> str:
        setting = self.__perception_settings[index]
        return f'{setting[1]} <= {observation_name}[{setting[0]}] < {setting[2]}'

    def get_finished_expression(self, done_name: str, observation_name: str) -> str:
        return f'{done_name} or {observation_name}[57] < 5'

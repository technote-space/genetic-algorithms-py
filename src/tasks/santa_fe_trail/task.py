import sys
from typing import Mapping, Callable
from task import AbstractTask, ISettings, IGaSettings
from .implements import Agent, Field, FieldFlags
from .settings import Settings
from .ga_settings import GaSettings


class SantaFeTrail(AbstractTask):
    """
    Description:
    ------------
    Santa Fe Trail
    """

    __settings: Settings
    __ga_settings: GaSettings
    __field: Field
    __agent: Agent
    __actions: Mapping[int, Callable[[], None]]
    __perceptions: Mapping[int, Callable[[], bool]]

    def __init__(self) -> None:
        super().__init__()

        self.__settings = Settings()
        self.__ga_settings = GaSettings()
        self.__field = Field()
        self.__agent = Agent(self.__field)
        self.__actions = {
            0: self.__go_forward,
            1: self.__turn_left,
            2: self.__turn_right,
        }
        self.__perceptions = {
            0: self.__is_food,
        }

    @property
    def settings(self) -> ISettings:
        return self.__settings

    @property
    def ga_settings(self) -> IGaSettings:
        return self.__ga_settings

    def __go_forward(self) -> None:
        self.__agent.go_forward()
        if self.__field.is_finished:
            self._on_finished()

    def __turn_right(self) -> None:
        self.__agent.turn_right()

    def __turn_left(self) -> None:
        self.__agent.turn_left()

    def _perform_action(self, index: int, is_start: bool) -> None:
        self.__actions[index]()

    def __is_food(self) -> bool:
        fx = self.__agent.fx
        fy = self.__agent.fy
        return self.__field.check(fx, fy, FieldFlags.FOOD) and not self.__field.check(fx, fy, FieldFlags.VISITED)

    def _perform_perceive(self, index: int) -> bool:
        return self.__perceptions[index]()

    def _perform_get_fitness(self) -> float:
        return self.__field.get_fitness()

    def draw(self) -> None:
        marks = {
            FieldFlags.NONE: '  ',
            FieldFlags.FOOD: '△ ',
            FieldFlags.VISITED: '○ ',
            FieldFlags.VISITED | FieldFlags.FOOD: '◎ ',
        }
        for y in range(self.__field.height):
            for x in range(self.__field.width):
                if self.__agent.x == x and self.__agent.y == y:
                    if self.__agent.dx == 1:
                        sys.stdout.write('→ ')
                    elif self.__agent.dx == -1:
                        sys.stdout.write('← ')
                    elif self.__agent.dy == 1:
                        sys.stdout.write('↓ ')
                    else:
                        sys.stdout.write('↑ ')
                else:
                    sys.stdout.write(marks[self.__field.get_flag(x, y)])
            sys.stdout.write('\n')

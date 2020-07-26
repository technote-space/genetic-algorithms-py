import sys
from target import AbstractTarget
from .implements import Agent, Field, FieldFlags
from .settings import Settings
from .ga_settings import GaSettings


class SantaFeTrail(AbstractTarget):
    """
    Description:
    ------------
    Santa Fe Trail
    """

    def __init__(self):
        super().__init__()

        self.__settings = Settings()
        self.__ga_settings = GaSettings()
        self.__field = Field()
        self.__agent = Agent(self.__field)
        self.__actions = {
            0: {
                "func": self.__go_forward,
                "label": "前進",
            },
            1: {
                "func": self.__turn_left,
                "label": "左回転",
            },
            2: {
                "func": self.__turn_right,
                "label": "右回転",
            },
        }
        self.__perceptions = {
            0: {
                "func": self.__is_food,
                "label": "餌",
            },
        }

    @property
    def settings(self):
        return self.__settings

    @property
    def ga_settings(self):
        return self.__ga_settings

    def __go_forward(self):
        self.__agent.go_forward()
        if self.__field.is_finished:
            self._on_finished()

    def __turn_right(self):
        self.__agent.turn_right()

    def __turn_left(self):
        self.__agent.turn_left()

    def _perform_action(self, index):
        self.__actions[index]["func"]()

    def __is_food(self):
        fx = self.__agent.fx
        fy = self.__agent.fy
        return self.__field.check(fx, fy, FieldFlags.FOOD) and not self.__field.check(fx, fy, FieldFlags.VISITED)

    def _perform_perceive(self, index):
        return self.__perceptions[index]["func"]()

    def get_action_expression(self, index):
        return self.__actions[index]["label"]

    def get_perceive_expression(self, index):
        return self.__perceptions[index]["label"]

    def _perform_get_fitness(self):
        return self.__field.get_fitness()

    def draw(self):
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

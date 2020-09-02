import random
from typing import Optional, List
from task import AbstractAtariSettings


class Settings(AbstractAtariSettings):
    """
    Description:
    ------------
    設定
    """

    @property
    def name(self) -> str:
        return 'Breakout'

    @property
    def perception_number(self) -> int:
        return 1

    @property
    def start_action_index(self) -> Optional[List[int]]:
        return [0] * random.randint(0, 100) + [1]

    @property
    def start_action_index_expression(self) -> Optional[List[str]]:
        return [
            'for index in [0] * random.randint(0, 100) + [1]:',
            '{',
            'self.__context.action(index, True)',
            '}'
        ]

    @property
    def action_limit(self) -> int:
        return 1000

    @property
    def fps(self) -> float:
        return 60

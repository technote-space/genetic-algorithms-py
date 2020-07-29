from typing import Optional
from target import AbstractAtariSettings


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
        return 3 * 16

    @property
    def action_frame(self) -> int:
        return 4

    @property
    def start_action_index(self) -> Optional[int]:
        return 1

    @property
    def action_limit(self) -> int:
        return 1000

    @property
    def fps(self) -> float:
        return 60

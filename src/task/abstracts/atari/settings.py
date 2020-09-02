from gym.spaces import Discrete  # type: ignore
from gym.core import Env  # type: ignore
from abc import abstractmethod
from ..gym import AbstractGymSettings


class AbstractAtariSettings(AbstractGymSettings):
    """
    Description:
    ------------
    Atari用の設定の基底クラス
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def perception_number(self) -> int:
        pass

    def _calc_action_number(self, env: Env) -> int:
        if type(env.action_space) is Discrete:  # type: ignore
            return env.action_space.n - 1  # type: ignore

        raise Exception('Not implemented')

    @property
    def fps(self) -> float:
        return 60

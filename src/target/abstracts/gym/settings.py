from gym.spaces import Discrete  # type: ignore
from gym.core import Env  # type: ignore
from abc import abstractmethod
from typing import Optional
from .. import AbstractSettings


class AbstractGymSettings(AbstractSettings):
    """
    Description:
    ------------
    Gym用の設定の基底クラス
    """

    __gym_id: str
    __env: Env
    __action_number: Optional[int]

    def __init__(self, gym_id: str, env: Env) -> None:
        self.__gym_id = gym_id
        self.__env = env  # type: ignore
        self.__action_number = None

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def gym_id(self) -> str:
        return self.__gym_id

    @property
    def action_limit(self) -> int:
        return self.__env.spec.max_episode_steps  # type: ignore

    @property
    @abstractmethod
    def perception_number(self) -> int:
        pass

    @property
    def action_number(self) -> int:
        if self.__action_number is not None:
            return self.__action_number

        if type(self.__env.action_space) is Discrete:  # type: ignore
            self.__action_number = self.__env.action_space.n  # type: ignore
            return self.__action_number  # type: ignore

        raise Exception('Not implemented')

    @property
    def fps(self) -> float:
        return 30

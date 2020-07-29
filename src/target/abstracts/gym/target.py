import gym  # type: ignore
from gym.core import Env  # type: ignore
from abc import abstractmethod
from typing import Callable, Any
from .. import AbstractTarget
from ...interfaces import ISettings, IGaSettings


class AbstractGymTarget(AbstractTarget):
    """
    Description:
    ------------
    Gym用の学習対象の基底クラス
    """

    __env: Env
    __closed: bool
    __settings: ISettings
    __ga_settings: IGaSettings
    __observation: Any  # type: ignore
    __reward: float

    def __init__(self, gym_id: str, settings: Callable[[str, Env], ISettings], ga_settings: Callable[[], IGaSettings]) -> None:
        super().__init__()

        self.__env = gym.make(gym_id)  # type: ignore
        self.__closed = False
        self.__settings = settings(gym_id, self.__env)  # type: ignore
        self.__ga_settings = ga_settings()
        self.__observation = self.__env.reset()  # type: ignore
        self.__reward = 0

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        if not self.__closed and self.__env:  # type: ignore
            self.__closed = True
            self.__env.close()  # type: ignore

    @property
    def settings(self) -> ISettings:
        return self.__settings

    @property
    def ga_settings(self) -> IGaSettings:
        return self.__ga_settings

    @property
    def observation(self) -> Any:  # type: ignore
        return self.__observation  # type: ignore

    # noinspection PyMethodMayBeStatic
    def _get_action(self, index: int) -> Any:  # type: ignore
        return index

    def _perform_action(self, index: int) -> None:
        observation, reward, done, _ = self.__env.step(self._get_action(index))  # type: ignore
        self.__observation = observation  # type: ignore
        self.__reward += reward  # type: ignore

        if done:  # type: ignore
            self._on_finished()

    @abstractmethod
    def _perform_perceive(self, index: int) -> bool:
        pass

    # noinspection PyMethodMayBeStatic
    def _correction_fitness(self) -> float:
        return 0

    def _perform_get_fitness(self) -> float:
        fitness: float = self.__reward / self.__env.spec.reward_threshold  # type: ignore
        if fitness > 1:
            surplus = fitness - 1
            fitness = 1 + surplus * 0.01
        return fitness + self._correction_fitness()

    def _perform_render(self) -> None:
        if not self.__closed:
            self.__env.render()  # type: ignore

    # noinspection PyMethodMayBeStatic
    def get_action_expression(self, index: int) -> str:
        return f'{index}'

    @abstractmethod
    def get_perceive_expression(self, index: int, observation_name: str) -> str:
        pass

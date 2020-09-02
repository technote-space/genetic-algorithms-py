import gym
import time
import os
from .finished import Finished


class Context:
    def __init__(self):
        self.__action_limit = 200
        self.__step_limit = 2000
        self.__env = None
        self.__reward = None
        self.__step = None
        self.__action_step = None
        self.__context = None

    @property
    def __has_finished(self):
        return self.__context[2] or self.__action_step >= self.__action_limit or self.__step >= self.__step_limit

    def reset(self):
        if self.__env:
            self.__env.close()

        self.__reward = 0
        self.__step = 0
        self.__action_step = 0
        self.__env = gym.make("MountainCar-v0")
        self.__context = (self.__env.reset(), 0, False, {})

    def __print_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{self.__step}/{self.__step_limit}', f'{self.__action_step}/{self.__action_limit}')
        print()
        print(f'reward: {self.__reward:.3f}')

    @staticmethod
    def __get_action(index, _is_start):
        if index == 0:
            return 0

        if index == 1:
            return 1

        if index == 2:
            return 2

        raise Exception("Unexpected error")

    def action(self, index, is_start=False):
        self.__context = self.__env.step(self.__get_action(index, is_start))
        self.__reward += self.__context[1]
        self.__step += 1
        self.__action_step += 1
        self.__print_status()
        if self.__has_finished:
            raise Finished()

        self.__env.render()
        time.sleep(0.0333)

        return True

    def perception(self, index):
        self.__step += 1
        if self.__has_finished:
            self.__print_status()
            raise Finished()

        if index == 0:
            return -1.2 <= self.__context[0][0] < -0.9

        if index == 1:
            return -0.9 <= self.__context[0][0] < -0.6

        if index == 2:
            return -0.6 <= self.__context[0][0] < -0.3

        if index == 3:
            return -0.3 <= self.__context[0][0] < 0

        if index == 4:
            return 0 <= self.__context[0][0] < 0.3

        if index == 5:
            return 0.3 <= self.__context[0][0] < 0.6

        if index == 6:
            return -0.07 <= self.__context[0][1] < -0.035

        if index == 7:
            return -0.035 <= self.__context[0][1] < 0

        if index == 8:
            return 0 <= self.__context[0][1] < 0.035

        if index == 9:
            return 0.035 <= self.__context[0][1] < 0.07

        raise Exception("Unexpected error")

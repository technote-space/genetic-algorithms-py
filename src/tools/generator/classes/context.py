from typing import List, Optional
from target import ITarget
from .base import Base


class Context(Base):
    """
    Description:
    ------------
    Context
    """

    __target: ITarget
    __fps: float
    __gym_id: str
    __action_limit: int
    __step_limit: int
    __action_number: int
    __perception_number: int

    def __init__(self, directory: str, target: ITarget, fps: float, gym_id: str, action_limit: int, step_limit: int, action_number: int, perception_number: int) -> None:
        super().__init__(directory)
        self.__target = target
        self.__fps = fps
        self.__gym_id = gym_id
        self.__action_limit = action_limit
        self.__step_limit = step_limit
        self.__action_number = action_number
        self.__perception_number = perception_number

    def _get_file_name(self) -> str:
        return 'context'

    def _get_imports(self) -> Optional[List[str]]:
        return [
            'import gym',
            'import time',
            'import os',
            'from .finished import Finished',
        ]

    def __get_class_source(self) -> List[str]:
        return [
            'def __init__(self):',
            '{',
            f'self.__action_limit = {self.__action_limit}',
            f'self.__step_limit = {self.__step_limit}',
            'self.__env = None',
            'self.__reward = None',
            'self.__step = None',
            'self.__action_step = None',
            'self.__context = None',
            '}',
            '@property',
            'def __has_finished(self):',
            '{',
            'return self.__context[2] or self.__action_step >= self.__action_limit or self.__step >= self.__step_limit',
            '}',
            'def reset(self):',
            '{',
            'if self.__env:',
            '{',
            'self.__env.close()',
            '}',
            'self.__reward = 0',
            'self.__step = 0',
            'self.__action_step = 0',
            f'self.__env = gym.make("{self.__gym_id}")',
            'self.__context = (self.__env.reset(), 0, False, {})',
            '}',
            'def __print_status(self):',
            '{',
            "os.system('cls' if os.name == 'nt' else 'clear')",
            "print(f'{self.__step}/{self.__step_limit}', f'{self.__action_step}/{self.__action_limit}')",
            'print()',
            "print(f'reward: {self.__reward:.3f}')",
            '}',
        ]

    def __get_action_helper(self) -> List[str]:
        sleep_time = 1.0 / self.__fps
        actions = []
        for index in range(self.__action_number):
            actions.extend([
                f'if index == {index}:',
                '{',
                f'return {self.__target.get_action_expression(index)}',
                '}',
            ])

        get_action = [
                         '@staticmethod',
                         'def __get_action(index):',
                         '{',
                     ] + actions + [
                         'raise Exception("Unexpected error")',
                         '}'
                     ]

        return get_action + [
            'def action(self, index):',
            '{',
            'self.__context = self.__env.step(self.__get_action(index))',
            'self.__reward += self.__context[1]',
            'self.__step += 1',
            'self.__action_step += 1',
            'self.__print_status()',
            'if self.__has_finished:',
            '{',
            'raise Finished()',
            '}',
            'self.__env.render()',
            f'time.sleep({sleep_time:.4f})',
            '',
            'return True',
            '}',
        ]

    def __get_perception_helper(self) -> List[str]:
        perceptions = []
        for index in range(self.__perception_number):
            perceptions.extend([
                f'if index == {index}:',
                '{',
                f'return {self.__target.get_perceive_expression(index, "self.__context[0]")}',
                '}',
            ])
        return [
                   'def perception(self, index):',
                   '{',
                   'self.__step += 1',
                   'if self.__has_finished:',
                   '{',
                   'self.__print_status()',
                   'raise Finished()',
                   '}',
               ] + perceptions + [
                   'raise Exception("Unexpected error")',
                   '}',
               ]

    def _get_source_code(self) -> List[str]:
        return [
                   'class Context:',
                   '{',
               ] + self.__get_class_source() + self.__get_action_helper() + self.__get_perception_helper() + ['}']

    def _is_package(self) -> bool:
        return True

from typing import List, Optional
from .base import Base


class Runner(Base):
    """
    Description:
    ------------
    Runner
    """

    __step_limit: int

    def __init__(self, directory: str, step_limit: int) -> None:
        super().__init__(directory)
        self.__step_limit = step_limit

    def _get_file_name(self) -> str:
        return 'runner'

    def _get_imports(self) -> Optional[List[str]]:
        return [
            'import time',
            'import sys',
            'from .finished import Finished',
        ]

    def _get_source_code(self) -> List[str]:
        return [
            'class Runner:',
            '{',
            'def __init__(self, context, algorithm):',
            '{',
            f'sys.setrecursionlimit({max(500, min(2500, self.__step_limit))})',
            'self.__context = context',
            'self.__algorithm = algorithm',
            '}',
            'def start(self):',
            '{',
            'while True:',
            '{',
            'try:',
            '{',
            'self.__episode()',
            '}',
            'except Finished:',
            '{',
            'pass',
            '}',
            'time.sleep(2)',
            '}',
            '}',
            'def __episode(self):',
            '{',
            'self.__context.reset()',
            'self.__algorithm.start()',
            '}',
            '}',
        ]

    def _is_package(self) -> bool:
        return True

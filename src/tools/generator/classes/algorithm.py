from typing import List, Optional
from .base import Base


class Algorithm(Base):
    """
    Description:
    ------------
    Algorithm
    """

    __lines: List[str]
    __start: int
    __start_actions: List[str]

    def __init__(self, directory: str, lines: List[str], start: int, start_actions: List[str]) -> None:
        super().__init__(directory)
        self.__lines = lines
        self.__start = start
        self.__start_actions = start_actions

    def _get_file_name(self) -> str:
        return 'algorithm'

    def _get_imports(self) -> Optional[List[str]]:
        return None

    def _get_source_code(self) -> List[str]:
        return [
                   'class Algorithm:',
                   '{',
                   'def __init__(self, context):',
                   '{',
                   'self.__context = context',
                   '}',
                   'def start(self):',
                   '{',
               ] + self.__start_actions + [
                   f'self.__func{self.__start}()',
                   '}',
               ] + self.__lines + ['}']

    def _is_package(self) -> bool:
        return True

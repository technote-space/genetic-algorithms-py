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

    def __init__(self, directory: str, lines: List[str], start: int) -> None:
        super().__init__(directory)
        self.__lines = lines
        self.__start = start

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
                   f'self.__func{self.__start}()',
                   '}',
               ] + self.__lines + ['}']

    def _is_package(self) -> bool:
        return True

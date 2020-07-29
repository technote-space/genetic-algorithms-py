import os
from abc import ABCMeta, abstractmethod
from typing import List, Optional


class Base(metaclass=ABCMeta):
    """
    Description:
    ------------
    基底クラス
    """

    __directory: str

    def __init__(self, directory: str) -> None:
        self.__directory = directory

    @abstractmethod
    def _get_file_name(self) -> str:
        pass

    @abstractmethod
    def _get_imports(self) -> Optional[List[str]]:
        pass

    @abstractmethod
    def _get_source_code(self) -> List[str]:
        pass

    @abstractmethod
    def _is_package(self) -> bool:
        pass

    def make(self) -> None:
        package_dir = 'packages' if self._is_package() else ''
        with open(os.path.join(os.getcwd(), self.__directory, package_dir, f'{self._get_file_name()}.py'), mode='w') as f:
            f.write(self.__program())

    def __get_lines(self) -> List[str]:
        imports = self._get_imports()
        if imports is None:
            return self._get_source_code()

        return imports + ['', ''] + self._get_source_code()

    def __program(self) -> str:
        indent = 0
        closed = False
        results = []

        for line in self.__get_lines():
            line = line.strip()
            new_line = ''
            skip = len(line) > 0 and ('}' == line[0] or '{' == line[0])

            if len(line) > 0 and '}' == line[0]:
                indent -= 1
                closed = True
            else:
                if closed and line != 'else:':
                    new_line = '\n'

                closed = False

            if not skip:
                if len(line) > 0:
                    results.append(new_line + '    ' * indent + line)
                else:
                    results.append('')

            if len(line) > 0 and '{' == line[0]:
                indent += 1

        return '\n'.join(results) + '\n'

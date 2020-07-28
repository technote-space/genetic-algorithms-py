from .base import Base


class Algorithm(Base):
    """
    Description:
    ------------
    Algorithm
    """

    def __init__(self, directory, lines, start) -> None:
        super().__init__(directory)
        self.__lines = lines
        self.__start = start

    def _get_file_name(self):
        return 'algorithm'

    def _get_imports(self):
        return None

    def _get_source_code(self):
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

    def _is_package(self):
        return True

from .base import Base


class Finished(Base):
    """
    Description:
    ------------
    終了
    """

    def _get_file_name(self):
        return 'finished'

    def _get_imports(self):
        return None

    def _get_source_code(self):
        return [
            'class Finished(Exception):',
            '{',
            'pass',
            '}',
        ]

    def _is_package(self):
        return True

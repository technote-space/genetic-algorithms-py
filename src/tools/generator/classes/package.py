from .base import Base


class Package(Base):
    """
    Description:
    ------------
    Package
    """

    def _get_file_name(self):
        return '__init__'

    def _get_imports(self):
        return [
            'from .context import Context',
            'from .algorithm import Algorithm',
            'from .finished import Finished',
            'from .runner import Runner',
        ]

    def _get_source_code(self):
        return [
            "__all__ = ['Context', 'Algorithm', 'Finished', 'Runner']",
        ]

    def _is_package(self):
        return True

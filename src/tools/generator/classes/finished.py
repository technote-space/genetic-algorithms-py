from typing import List, Optional
from .base import Base


class Finished(Base):
    """
    Description:
    ------------
    終了
    """

    def _get_file_name(self) -> str:
        return 'finished'

    def _get_imports(self) -> Optional[List[str]]:
        return None

    def _get_source_code(self) -> List[str]:
        return [
            'class Finished(Exception):',
            '{',
            'pass',
            '}',
        ]

    def _is_package(self) -> bool:
        return True

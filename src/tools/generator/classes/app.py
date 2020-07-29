from typing import List, Optional
from .base import Base


class App(Base):
    """
    Description:
    ------------
    App
    """

    def _get_file_name(self) -> str:
        return 'app'

    def _get_imports(self) -> Optional[List[str]]:
        return [
            'from packages import Context, Algorithm, Runner'
        ]

    def _get_source_code(self) -> List[str]:
        return [
            'def main():',
            '{',
            'context = Context()',
            'algorithm = Algorithm(context)',
            'runner = Runner(context, algorithm)',
            'runner.start()',
            '}',
            '',
            '',
            'if __name__ == "__main__":',
            '{',
            'main()',
            '}',
        ]

    def _is_package(self) -> bool:
        return False

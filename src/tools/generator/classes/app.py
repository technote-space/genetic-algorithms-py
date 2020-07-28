from .base import Base


class App(Base):
    """
    Description:
    ------------
    App
    """

    def _get_file_name(self):
        return 'app'

    def _get_imports(self):
        return [
            'from packages import Context, Algorithm, Runner'
        ]

    def _get_source_code(self):
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

    def _is_package(self):
        return False

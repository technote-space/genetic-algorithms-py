import os
import subprocess


class Process:
    """
    Description:
    ------------
    プロセスツール
    """

    __file: str

    def __init__(self) -> None:
        self.__file = os.path.join(os.getcwd(), 'PID')
        self.__kill()
        self.__create()

    def __kill(self) -> None:
        if os.path.exists(self.__file):
            with open(self.__file, mode='r') as f:
                pid = f.read()
            if 'python' in str(subprocess.run(["ps", "-p", pid], stdout=subprocess.PIPE).stdout):  # type: ignore
                subprocess.run(["kill", "-9", pid], stdout=subprocess.PIPE)  # type: ignore
            os.remove(self.__file)

    def __create(self) -> None:
        with open(self.__file, mode='w') as f:
            f.write(str(os.getpid()))

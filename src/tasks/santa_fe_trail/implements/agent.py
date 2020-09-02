from .field import Field


class Agent:
    """
    Description:
    ------------
    Agent
    """

    __field: Field
    __x: int
    __y: int
    __dx: int
    __dy: int

    def __init__(self, field: Field) -> None:
        self.__field = field
        self.__x = 0
        self.__y = 0
        self.__dx = 1
        self.__dy = 0

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def dx(self) -> int:
        return self.__dx

    @property
    def dy(self) -> int:
        return self.__dy

    @property
    def fx(self) -> int:
        return self.x + self.dx

    @property
    def fy(self) -> int:
        return self.y + self.dy

    def set_dir(self, dx: int, dy: int) -> None:
        self.__dx = dx
        self.__dy = dy

    def go_forward(self) -> None:
        self.__x = min(max(0, self.fx), self.__field.width - 1)
        self.__y = min(max(0, self.fy), self.__field.height - 1)
        self.__field.on_visited(self.x, self.y)

    def turn_right(self) -> None:
        self.set_dir(-self.dy, self.dx)

    def turn_left(self) -> None:
        self.set_dir(self.dy, -self.dx)

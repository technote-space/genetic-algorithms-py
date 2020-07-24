class Agent:
    """
    Description:
    ------------
    Agent
    """

    def __init__(self, field):
        self.__field = field
        self.__x = 0
        self.__y = 0
        self.__dx = 1
        self.__dy = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy

    @property
    def fx(self):
        return self.x + self.dx

    @property
    def fy(self):
        return self.y + self.dy

    def set_dir(self, dx, dy):
        self.__dx = dx
        self.__dy = dy

    def go_forward(self):
        self.__x = min(max(0, self.fx), self.__field.width - 1)
        self.__y = min(max(0, self.fy), self.__field.height - 1)
        self.__field.on_visited(self.x, self.y)

    def turn_right(self):
        self.set_dir(-self.dy, self.dx)

    def turn_left(self):
        self.set_dir(self.dy, -self.dx)

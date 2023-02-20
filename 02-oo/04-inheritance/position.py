class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def moved_by(self, dx, dy):
        """
        Returns a new Position object that has been moved horizontally by dx
        and vertically by dy.
        """
        return Position(self.x + dx, self.y + dy)

    def __repr__(self):
        return f'Position({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, Position):
            raise NotImplemented()
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
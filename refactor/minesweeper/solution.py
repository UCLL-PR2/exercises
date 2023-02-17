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

    def move(self, dx, dy):
        return Position(self.x + dx, self.y + dy)

    @property
    def around(self):
        return (
            self.move(dx, dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if dx != 0 or dy != 0
        )


class Grid:
    def __init__(self, width, height, initializer):
        self.__grid = [
            [initializer(Position(x, y)) for x in range(width)]
            for y in range(height)
        ]

    @property
    def width(self):
        return len(self.__grid[0])

    @property
    def height(self):
        return len(self.__grid)

    def is_inside(self, position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def neighbors(self, position):
        return (pos for pos in position.around if self.is_inside(pos))

    def __getitem__(self, position):
        return self.__grid[position.y][position.x]

    def all_positions(self):
        return (
            Position(x, y)
            for y in range(self.height)
            for x in range(self.width)
        )


class Minefield:
    def __init__(self, width, height, contains_bomb_at):
        self.__grid = Grid(width, height, contains_bomb_at)

    @property
    def width(self):
        return self.__grid.width

    @property
    def height(self):
        return self.__grid.height

    @staticmethod
    def parse(string):
        def contains_bomb_at(position):
            return rows[position.y][position.x] == '*'

        rows = string.split("\n")
        width = len(rows[0])
        height = len(rows)

        return Minefield(width, height, contains_bomb_at)

    def __str__(self):
        def row_to_string(y):
            return "".join(
                cell_to_string(Position(x, y))
                for x in range(self.width)
            )

        def cell_to_string(position):
            if self.contains_bomb_at(position):
                return '*'
            else:
                return str(self.bomb_count_at(position))

        return "\n".join(row_to_string(y) for y in range(self.height))

    def contains_bomb_at(self, position):
        return self.__grid[position]

    def bomb_count_at(self, position):
        return sum(
            1
            for pos in self.__grid.neighbors(position)
            if self.contains_bomb_at(pos)
        )


def add_bomb_counts(string):
    minefield = Minefield.parse(string)
    return str(minefield)

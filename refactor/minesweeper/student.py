def add_bomb_counts(string):
    grid = [[c == '*' for c in s] for s in string.split("\n")]

    return "\n".join(
        "".join(
            '*' if grid[y][x] else str(sum(1
                for dx in [-1, 0, 1]
                for dy in [-1, 0, 1]
                if (dx != 0 or dy != 0) and 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and grid[y + dy][x + dx]
            ))
            for x in range(len(grid[0]))
        )
        for y in range(len(grid))
    )

from student import find_shortest_path


def test_find_shortest_path1():
    def distance(a, b):
        return table[a][b]

    table = [
        [0, 1, 5],
        [5, 0, 1],
        [1, 5, 0],
    ]
    expected = [0, 1, 2, 0]
    actual = find_shortest_path(distance, len(table))

    assert expected == actual


def test_find_shortest_path2():
    def distance(a, b):
        return table[a][b]

    table = [
        [0, 8, 3, 5],
        [12, 0, 15, 7],
        [4, 2, 0, 3],
        [2, 5, 4, 0],
    ]
    expected = [0, 2, 1, 3, 0]
    actual = find_shortest_path(distance, len(table))

    assert expected == actual

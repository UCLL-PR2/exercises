def cycle(values):
    # If values is an iterator, we need to make a copy
    values = list(values)
    while True:
        for value in values:
            yield value


def alternative_cycle(values):
    values = list(values)
    while True:
        yield from values  # "yield from xs" yields each element in xs in turn

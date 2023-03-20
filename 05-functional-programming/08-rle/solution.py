def rle_encode(data):
    data = iter(data)
    try:
        last_datum = next(data)
        count = 1
        for datum in data:
            if last_datum == datum:
                count += 1
            else:
                yield (last_datum, count)
                last_datum = datum
                count = 1
        yield (last_datum, count)
    except StopIteration:
        pass


def rle_decode(data):
    for datum, count in data:
        for _ in range(count):
            yield datum

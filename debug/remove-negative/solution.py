def remove_negatives(ns):
    i = len(ns) - 1
    while i >= 0:
        if ns[i] < 0:
            del ns[i]
        i -= 1

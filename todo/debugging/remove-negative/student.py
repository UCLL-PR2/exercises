def remove_negatives(ns):
    i = 0
    while i <= len(ns):
        if ns[i] < 0:
            del ns[i]
        i += 1

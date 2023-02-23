def remove_duplicates(xs):
    found = set()
    result = []
    for x in xs:
        if x not in found:
            result.append(x)
            found.add(x)
    return result


# Slow solution
def remove_duplicates_using_list(xs):
    result = []
    for x in xs:
        if x not in result:
            result.append(x)
    return result

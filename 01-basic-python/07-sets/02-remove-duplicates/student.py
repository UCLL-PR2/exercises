# Write your code here
def remove_duplicates(xs):
    seen = set()
    result = []
    for element in xs:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result
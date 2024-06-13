# Write your code here

def contains_duplicates(xs):
    seen = []
    for element in xs:
        if element not in seen:
            seen.append(element)
        else:
            return True
    return False 
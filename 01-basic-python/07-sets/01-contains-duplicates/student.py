# Write your code here
def contains_duplicates(xs):
    return not (len(xs) == len(set(xs)))
# Write your code here
def contains_duplicates(xs):
    for i in range(len(xs)):
        for k in range(1+i,len(xs)):
            if xs[k] == xs[i]:
                return True
    return False
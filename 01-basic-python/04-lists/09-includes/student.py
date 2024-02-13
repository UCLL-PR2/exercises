# Write your code here

def includes(xs, ys):
    for element in ys:
        if element not in xs:
            return False
    return True
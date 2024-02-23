# Write your code here
def drop_nth(xs, n):
    ys = xs
    del ys[n::]
    return ys
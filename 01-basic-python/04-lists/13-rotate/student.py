# Write your code here

def rotate(xs, n):
    counter = n
    while counter >= 0:
        number = xs.pop(n)
        xs.append(number)
        counter -= 1
    counter = 0
    while counter < n:
        number = xs.pop(0)
        xs.append(number)
        counter += 1
    return xs

print(rotate([1, 2], 0))
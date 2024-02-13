# Write your code here

def target_sum(ns, target):
    for first in ns:
        for second in ns:
            if first + second == target:
                return True
    return False
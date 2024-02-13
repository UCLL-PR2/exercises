# Write your code here

def target_sum(ns, target):
    for first in range(0, len(ns)):
        for second in range(0, len(ns)):
            if ns[first] + ns[second] == target and first != second:
                return True
    return False
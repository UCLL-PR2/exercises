# Write your code here
def target_sum(ns, target):
    for x in range(len(ns)):
        for y in range (x + 1 ,len(ns)):
            if ns[x] + ns[y]== target:
                return True
    return False
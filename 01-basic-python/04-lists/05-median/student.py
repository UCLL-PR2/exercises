# Write your code here
from math import floor

def median(ns):
    if len(ns) == 0:
        return 0
    mid = len(ns) / 2
    ns = sorted(ns)
    if len(ns) % 2 != 0:
        return ns[floor(mid)]
    else:
        first = int(mid) -1
        second = int(mid)
        return (ns[first] + ns[second]) / 2
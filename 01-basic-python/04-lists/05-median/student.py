# Write your code here
def median(ns):
    ns_sorted = sorted(ns)
    i = len(ns_sorted) // 2

    if len(ns_sorted) % 2 == 0:
        return (ns_sorted[i - 1] + ns_sorted[i]) / 2
    else:
        return ns_sorted[i]


    
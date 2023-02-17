def frequencies(xs):
    result = {}

    for x in xs:
        if x not in result:
            result[x] = 0

        result[x] += 1

    return result

    #Other solution 
    #return dict(zip(xs,[xs.count(i) for i in xs]))
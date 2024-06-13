# Write your code here
def coins(one, two, five, goal):
    for coin1 in range(one+1):
        for coin2 in range(two+1):
            for coin3 in range(five+1):
                if coin1 * 1 + coin2 * 2 + coin3 * 5 == goal:
                    return True
    return False

coins(0, 1, 0, 2)
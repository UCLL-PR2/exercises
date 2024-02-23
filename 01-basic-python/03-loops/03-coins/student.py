# Write your code here
def coins(one, two, five, goal):
    for x in range(0,one+1):
        for y in range(0,two+1):
            for z in range(0,five+1):
                if x*1 + y*2 + z*5 == goal:
                    return True
    return False
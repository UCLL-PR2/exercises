def key_values(dictionary) ->list:
    lijst = []
    for k in dictionary.keys():
        if k%2 == 0:
            lijst.append(k)
    return lijst
    # return [k for k in dictionary.keys() if k %2==0]


def key_check(dictionary,key) -> bool:
    return key in dictionary

def value_check(dictionary,value) -> bool:
    return value in list(dictionary.values())

def nested_dict(dictionary):
    lijst = []
    for value in dictionary.values():
        for value2 in value.values():
            lijst.append(value2)
    return lijst 
    # return [y for v in dictionary.values() for x,y in v.items()]

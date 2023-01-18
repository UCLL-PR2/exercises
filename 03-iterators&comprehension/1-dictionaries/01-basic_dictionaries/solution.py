def key_values(dictionary) ->list:
    return [k for k in dictionary.keys() if k %2==0]

def key_check(dictionary,key) -> bool:
    return key in dictionary

def value_check(dictionary,value) -> bool:
    return value in list(dictionary.values())

def nested_dict(dictionary):
    return [y for v in dictionary.values() for x,y in v.items()]

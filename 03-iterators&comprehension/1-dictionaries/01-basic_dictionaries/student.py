def key_values(dictionary:dict):
    lijst = []
    for k in dictionary.keys():
        if k%2 == 0:
            lijst.append(k)
    return lijst

def key_check(dictionary :dict,value):
    return value in dictionary

def value_check(dictionary :dict,value):

    return value in dictionary.values()

def nested_dict(dictionary:dict):
    lijst = []
    for value in dictionary.values():
        for value2 in value.values():
            lijst.append(value2)
    return lijst    

d = {
    "A" : {1:"Z",2:"C"},
    "B" : {3:"E",5:"V"},
    "C" : {4:"R",6:"G"},
}

print(nested_dict(d))
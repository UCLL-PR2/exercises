def create_dict():
    return {"Name": "John", "Age": 30, "City": "New York"}

def add_country(dictionary):
    dictionary["Country"] = "USA"
    return dictionary

def get_age(dictionary):
    return dictionary["Age"]

def update_age(dictionary, new_age):
    dictionary["Age"] = new_age
    return dictionary

def remove_city(dictionary):
    dictionary.pop("City", None)
    return dictionary

def check_country(dictionary):
    return "Country" in dictionary

def get_keys(dictionary):
    return list(dictionary.keys())

def get_values(dictionary):
    return list(dictionary.values())

def create_dict2():
    return {"Name": "Jane", "Age": 25, "City": "San Francisco"}

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

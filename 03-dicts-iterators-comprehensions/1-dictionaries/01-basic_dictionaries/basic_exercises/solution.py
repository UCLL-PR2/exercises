def create_dict() -> dict:
    return {"Name": "John", "Age": 30, "City": "New York"}

def add_country(dictionary: dict) -> dict:
    dictionary["Country"] = "USA"
    return dictionary

def get_age(dictionary: dict) -> int:
    return dictionary["Age"]

def update_age(dictionary: dict, new_age: int) -> dict:
    dictionary["Age"] = new_age
    return dictionary

def remove_city(dictionary: dict) -> dict:
    dictionary.pop("City", None)
    return dictionary

def check_country(dictionary: dict) -> bool:
    return "Country" in dictionary

def get_keys(dictionary: dict) -> list:
    return list(dictionary.keys())

def get_values(dictionary: dict) -> list:
    return list(dictionary.values())

def create_dict2() -> dict:
    return {"Name": "Jane", "Age": 25, "City": "San Francisco"}

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    return {**dict1, **dict2}

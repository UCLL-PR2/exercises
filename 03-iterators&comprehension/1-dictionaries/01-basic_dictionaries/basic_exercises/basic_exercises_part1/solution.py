def sum_dict_values(d: dict) -> int:
    return sum(d.values())

def odd_keys_dict(d: dict) -> dict:
    odd_keys_dict = {}
    for k, v in d.items():
        if k % 2 == 1:
            odd_keys_dict[k] = v
    return odd_keys_dict

    # Other solution
    # return {k: v for k, v in d.items() if k % 2 == 1}


def keys_with_value(d: dict, value) -> list:
    keys = []
    for k, v in d.items():
        if v == value:
            keys.append(k)
    return keys

    # Other solution
    # return [k for k, v in d.items() if v == value]


def double_dict_values(d: dict) -> dict:
    doubled_dict = {}
    for k, v in d.items():
        doubled_dict[k] = v * 2
    return doubled_dict

    # Other solution
    # return {k: v * 2 for k, v in d.items()}

def merge_dicts(d1: dict, d2: dict) -> dict:
    return {**d1, **d2}

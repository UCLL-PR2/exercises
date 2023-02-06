def elementwise_sum(list1: list, list2: list) -> list:
    result = []
    for x, y in zip(list1, list2):
        result.append(x + y)
    return result

    # Other solution
    # return [x + y for x, y in zip(list1, list2)]

def even_numbers(numbers: list) -> list:
    return list(filter(lambda x: x % 2 == 0, numbers))

    # Solution without filter function
    # result = []
    # for num in numbers:
    #     if num % 2 == 0:
    #         result.append(num)
    # return result

def square_numbers(numbers: list) -> list:
    return list(map(lambda x: x ** 2, numbers))

def multiple_of_five(list_of_dicts: list)-> list:
    return list(filter(lambda d: any(v % 5 == 0 for v in d.values()), list_of_dicts))

    # Solution without filter function
    # result = []
    # for d in list_of_dicts:
    #     has_multiple_of_five = False
    #     for v in d.values():
    #         if v % 5 == 0:
    #             has_multiple_of_five = True
    #             break
    #     if has_multiple_of_five:
    #         result.append(d)
    # return result

def map_lists_to_dict(list1: list, list2: list) -> dict:
    result = {}
    for k, v in zip(list1, list2):
        result[k] = v
    return result

    # Other solution
    # return {k: v for k, v in zip(list1, list2)}

def length_of_strings(strings: list) -> list:
    return list(map(len, strings))

def list_of_pairs(list1: list, list2: list) -> list:
    return list(zip(list1, list2))

def positive_numbers(numbers: list) -> list:
    return list(filter(lambda x: x > 0, numbers))

def cubes_of_numbers(numbers: list) -> list:
    return list(map(lambda x: x**3, numbers))

def string_key_dictionaries(dict_list: list) -> list:
    return list(filter(lambda x: all(map(lambda y: isinstance(y, str), x.keys())), dict_list))

def merge_lists(list1: list, list2: list) -> list:
    result = []
    for pair in zip(list1, list2):
        result.extend(pair)
    return result

    # Other solution
    # return [x for pair in zip(list1, list2) for x in pair]


def prime_dicts(dict_list: list) -> list:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    return [d for d in dict_list if any(is_prime(v) for v in d.values())]


def divisible_by_3(numbers: list) -> list:
    return list(filter(lambda x: x % 3 == 0, numbers))


def repeat_elements(list1: list, list2: list) -> list:
    return [x for pair in zip(list1, list1) for x in pair]

def palindrome_strings(strings: list) -> list:
    return list(filter(lambda x: x == x[::-1], strings))

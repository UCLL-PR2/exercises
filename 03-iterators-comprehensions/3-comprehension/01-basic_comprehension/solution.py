def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def long_strings(strings):
    return [string for string in strings if len(string) >= 4]

def string_lengths(strings):
    return {string: len(string) for string in strings}

def small_numbers(numbers):
    return {num for num in numbers if num < 10}

def squared_numbers(numbers):
    return (num**2 for num in numbers)

def positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def pair_lists(list1, list2):
    return [x for x in zip(list1,list2)]
    # return list(zip(list1,list2))

def absolute_numbers(numbers):
    return [abs(num) for num in numbers]

def vowel_words(words):
    vowels = 'aeiouAEIOU'
    return [word for word in words if word[0] in vowels]

def square_dict(numbers):
    return {num: num**2 for num in numbers}

# Basic Questions on Dictionaries in Python

1. Write a Python function **even_numbers** that takes in a list of numbers and returns a new list with only the even numbers using a list comprehension.

```python
Example:
Input: [1, 2, 3, 4, 5]
Output: [2, 4]
```
2. Write a Python function **long_strings** that takes in a list of strings and returns a new list with only the strings of length 4 or greater using a list comprehension.

```python
Example:
Input: ['cat', 'dog', 'elephant', 'bird']
Output: ['elephant', 'bird']
```
3. Write a Python function **string_lengths** that takes in a list of strings and returns a dictionary where each key is a string and each value is the length of the string using a dictionary comprehension.
  
```python
Example:
Input:  ['cat', 'dog', 'elephant', 'bird']
Output: {'cat': 3, 'dog': 3, 'elephant': 8, 'bird': 4}
```
4. Write a Python function **small_numbers** that takes in a list of numbers and returns a new set of all the numbers that are less than 10 using a set comprehension.

```python
Example:
Input: [1, 2, 3, 4, 11, 12, 13]
Output: {1, 2, 3, 4}
```
5. Write a Python function **squared_numbers** that takes in a list of numbers and returns a generator that generates the squares of all the numbers using a generator comprehension.

```python
Example:
Input: [1, 2, 3, 4, 5]
Output: <generator object squared_numbers at 0x...>
#The generator, when iterated, would return [1, 4, 9, 16, 25]
```

6. Write a Python function **positive_numbers** that takes in a list of numbers and returns a new list of all the positive numbers using a list comprehension.

```python
Example:
Input: [-1, -2, 0, 1, 2, 3]
Output: [1, 2, 3]
```

7. Write a Python function **pair_lists** that takes in two lists and returns a new list that contains pairs (a,b) where a is from the first list and b is from the second list using a list comprehension.

```python
Example:
Input: ([1, 2, 3], [4, 5, 6])
Output: [(1, 4), (2, 5), (3, 6)]
```

8. Write a Python function **absolute_numbers** that takes in a list of numbers and returns a new list with the absolute values of the numbers using a list comprehension.

```python
Example:
Input: [-1, -2, 0, 1, 2, 3]
Output: [1, 2, 0, 1, 2, 3]
```

9. Write a Python function **vowel_words** that takes in a list of words and returns a new list with only the words that start with a vowel using a list comprehension.

```python
Example:
Input: ['apple', 'banana', 'cherry', 'dog']
Output: ['apple', 'elephant']
```

10. Write a Python function **square_dict** that takes in a list of numbers and returns a dictionary where the keys are the numbers and the values are the square of the keys using a dictionary comprehension.

```python
Example:
Input: [1, 2, 3, 4, 5]
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
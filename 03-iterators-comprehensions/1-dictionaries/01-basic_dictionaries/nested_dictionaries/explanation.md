# Exercises nested dictionaries - difficulty level: **

- Write a function called **key_values** that loop over an given dictionary with integers as keys and puts all the even key numbers in a new list. This list is to be returned.

- Write a function called **key_check** where 2 parameters are passed down. A dictionary and a value. The function checks wether or not the dictionary contains the **value as a key**. If so the functions returns True else False.

- Write a function called **value_check** where 2 parameters are passed down. A dictionary and a value. The function checks wether or not the dictionary contains the **value as a value and not a key**. If so the functions returns True else False.

- Write a function called **nested_dict** where a nested dictionary is given as a parameter. The function takes the values of the nested dictionary and adds this to a new list. The list is to be returned.

```python
d = {
    "A" : {1:"Z",2:"C"},
    "B" : {3:"E",5:"V"},
    "C" : {4:"R",6:"G"},
}
print(nested_dict(d))

# Output should be ['Z', 'C', 'E', 'V', 'R', 'G']

```

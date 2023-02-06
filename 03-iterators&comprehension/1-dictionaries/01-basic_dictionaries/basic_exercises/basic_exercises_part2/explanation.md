# Basic exercises

- Define a function **create_dict** that creates a dictionary with the following keys and values: "Name": "John", "Age": 30, "City": "New York". The function should return the dictionary.

- Define a function **add_country** that takes a dictionary as an argument and adds a key "Country" with the value "USA" to the dictionary. The function should return the updated dictionary.

- Define a function **get_age** that takes a dictionary as an argument and returns the value of "Age".

- Define a function **update_age** that takes a dictionary and a new age as arguments and updates the value of "Age" to the new age. The function should return the updated dictionary.

- Define a function **remove_city** that takes a dictionary as an argument and removes the key "City". The function should return the updated dictionary.

- Define a function **check_country** that takes a dictionary as an argument and returns a Boolean indicating if the key "Country" exists in the dictionary.

- Define a function **get_keys** that takes a dictionary as an argument and returns a list of its keys.

- Define a function **get_values** that takes a dictionary as an argument and returns a list of its values.

- Define a function **create_dict2** that creates another dictionary with the following keys and values: "Country": "USA", "Gender": "Male", "City": "San Francisco". The function should return the dictionary.

- Define a function **merge_dicts** that takes two dictionaries as arguments and returns a new dictionary that is the result of merging the two dictionaries. For example:

```python
dict1 = {"Name": "John", "Age": 30, "City": "New York"}

dict2 = {"Country": "USA", "Gender": "Male", "City": "San Francisco"}


merge_dicts(dict1,dict2)
#result should be

{"Name":    "John", 
 "Age":     30, 
 "City":    "San Francisco",
 "Country": "USA", 
 "Gender":  "Male",}
```
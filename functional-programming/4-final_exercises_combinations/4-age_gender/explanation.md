# Exercises age & gender - difficulty level: ***

You need to write a Python program to read the data from the file and perform the following tasks:

The next code that reads the data is already provided:
```python
def read_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        data = [line.split(",") for line in lines]
        return data
```

1. Create a function **create_dictionary** that takes the data of the above function as input and creates a dictionary that maps each name to their age and gender. The dictionary should have the following format:

```python
{
    "Tom": (32, "Male"),
    "Jane": (25, "Female"),
    "John": (28, "Male"),
    "Mary": (36, "Female"),
    "Bob": (44, "Male"),
    "Sue": (19, "Female")
}
```

2. Create a function **older_than_30** that takes the above dictionary as input and that creates a list of tuples that contains the names of people who are older than 30 and their genders. The list should have the following format:

```python
[("Tom", "Male"), ("Mary", "Female"), ("Bob", "Male")]

```

3. Create a function **all_ages** that takes the above dictionary as input and creates a list of ages of all the people in the data.
4. Create a function **gender_totals** that takes the above dictionary as input and creates a dictionary that maps each gender to the total age of all the people of that gender. The dictionary should have the following format:

```python
{
    "Male": 104,
    "Female": 80
}
```
# Assignment

## `process_data`

Create a function `process_data(data)` that transforms a list of strings into a dictionary.

The input list has the following format:

```python
['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math']
```

It must be transformed into

```python
{
        'John Smith': {
            'age': 20,
            'courses': ['Math', 'Physics']
        },
        'Jane Doe': {
            'age': 21,
            'courses': ['Biology', 'Chemistry', 'Math']
        }
    }
```


## `average_age`

Create a function `average_age(dictionary)` that calculates the average age of the students in the input dictionary.

## `courses`

Create a function `courses(dictionary)` that returns a collection of all the courses taken by the students in the input dictionary.
Return them as a set.

## `most_common_course`

Create a function `most_common_course(data)` that returns the set of courses that is taken by the most number of students.
For example, say `Math` is taken by 5 students, `Spanish` by 3, and `Biology` by 5, the function should return `{'Math', 'Biology'}`.

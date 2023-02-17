# Assigment

- Create a function process_data(data: list) -> dict: that processes a list of strings containing student information and return a dictionary with the following structure:
    
```Python
{
        'John Smith': {
            'age': 20,
            'courses': ['Math', 'Physics']
        },
        'Jane Doe': {
            'age': 21,
            'courses': ['Biology', 'Chemistry']
        }
    }
```
    
The input list is in the following format:

```Python
['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry']
```
    
- Create a function avg_age(data: dict) that calculates the average age of the students in the input dictionary.
- Create a function courses(data: dict) that returns a collection of all the courses taken by the students in the input dictionary.
- Create a function most_common_course(data: dict) Return the course that is taken by the most number of students. If there is a tie, return the first course that appears in the input dictionary.
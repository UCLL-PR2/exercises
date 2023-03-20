# Dictionary Comprehension

One can also rapidly construct dictionaries using _dictionary comprehensions_.
Say for example we have a list of `Student`s and want to quickly find a `Student` object based on its `id`.
Using a list would require a linear search:

```python
def find_student_with_id(students, id):
    for student in students:
        if student.id == id:
            return student
```

By storing them in a dictionary, this search can be done much more efficiently:

```python
>>> students_by_id = {student.id: student for student in students}

>>> students_by_id[id]
```

You can run the provided `benchmark.py` script to check how much execution time is improved by using a dictionary:

```bash
$ py benchmark.py
13.86886960011907
0.009574900148436427
```

## Tasks

Write the following functions:

* `title_to_director(movies)` returns a `dict` whose keys are movie titles and values are the corresponding director.
* `director_to_titles(movies)` returns a `dict` where keys are directors and values are lists of movie titles by that director.
  You will need to combine different kinds of comprehensions for this one.
  Note that we are not looking for an efficient solution.

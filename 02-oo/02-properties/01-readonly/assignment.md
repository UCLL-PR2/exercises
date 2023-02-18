# Assignment

Say we have written the following class.

```python
class Person:
    def __init__(self, age):
        self.age = age
```

This class is used throughout our codebase, many times over.
However, there's a problem with it: `age` can take any value you want.
Somewhere, we made a mistake and in certain cases the `age` becomes negative.
This causes a lot of problems.

The problem with public attributes is that they're rather... dumb.
It's just a simple memory location that can be overwritten at whim.
We somehow want to make it smarter somehow, so that it can disallow negative values.

Enter properties.
Properties allow us to make "intelligent attributes".
In essence, there's two things we can do with attributes: we can read their value, and we can overwrite their value.
Properties make it possible for us to define what exactly should happen when someone tries to read or write it.
In the case of our `age`, properties allow us to prevent anyone from writing a negative value to it.

The nice thing about properties is that they obey the "Uniform Access Principle".
This simply means that the code used to read/write attributes is exactly the same as the code used to read/write properties.

```python
# In case age is a simple attribute
print(person.age)
person.age = 5

# In case age is a smart property
print(person.age)
person.age = 5
```

See! No difference at all.
This is great news: we can promote our dumb `age` attribute to a smart `age` property without having to change any of the client code!
This actually is a very important rule in general: we want to be able to make local changes (upgrading `age`) without having it global ramifications.


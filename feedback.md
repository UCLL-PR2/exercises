# Feedback

## F-strings

Don't build strings like

```python
def greet(name):
    return "Hello " + name
```

Use f-strings:

```python
def greet(name):
    return f"Hello {name}"
```

They are both more readable and more efficient.

## ToString methods

Drop all the to-string-like methods.
They are very uninteresting and unrealistic: there's no way an object would take care of its actual representation.
For example, what about localization?

## OO

### Drop multiple inheritance

MI is too advanced a concept.

### Missing Topics

* Access control: how to make members private/protected in python
* Properties (getters, setters)
* Static methods
* Abstract methods using abc module

### Validation

Never use `assert` to validate input.

Do not check parameter types.
Python encourages duck typing, not nominal typing.

# Efficient Circular Buffer

Write a `CircularBuffer` class.
It is basically a list to which items can be added, but it only "remembers" the last N items, where N is chosen at creation.
For example,

```python
# Create a buffer with maximum size N = 3
>>> buffer = CircularBuffer(3)
>>> len(buffer)
0

# Add items to it
>>> buffer.add('a')
>>> buffer.add('b')
>>> buffer.add('c')
>>> len(buffer)
3

# We can indexate the buffer
>>> buffer[0]
'a'

>>> buffer[1]
'b'

>>> buffer[2]
'c'

# Adding an extra item
>>> buffer.add('d')

# Length does not exceed 3
>>> len(buffer)
3

# Only 3 most recently added items are remembered
>>> buffer[0]
'b'

>>> buffer[1]
'c'

>>> buffer[2]
'd'
```

In order to make the tests pass, you will have to find an efficient implementation.

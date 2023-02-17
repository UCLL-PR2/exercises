# Assignment

Write a function `cakes(eggs, butter, flour)` that computes
the number of cakes you can bake using the given ingredients.
Each cake requires 5 eggs, 250g butter and 250g of flour.

For example, `cakes(18, 600, 1000)` should return `2`:

* 18 eggs are enough to make 3 cakes.
* 600g of butter is enough to make 2 cakes.
* 1000g of flour is enough to make 4 cakes.

The butter is the limiting factor: only 2 cakes can be made.

## Two kinds of division

Open the Python console.
Experiment to determine what the difference is between Python's two division operators `/` and `//`.
For example, you can try inputting the following lines (omit the `>>>`, it represents the Python prompt):

```python
>>> 5 / 2

>>> 5 // 2
```

## Minimum and maximum

Python has `min` and `max` built-in:

```python
# You can give the values to be compared as a series of arguments
min(3, 5, 2, 6, 1, 4)    # Returns 1
max(3, 5, 2, 6, 1, 4)    # Returns 6

# You can also pass a list
min([5, 2, 9, 4])        # Returns 2

# Works on all comparable values
min('t', 'd', 'p')                 # Returns 'd'
max('zebra', 'aardvark', 'mule')   # Returns 'zebra'
```

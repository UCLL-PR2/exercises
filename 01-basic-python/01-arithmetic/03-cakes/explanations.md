# Assignment - difficulty level: *

Translate this JavaScript function `cakes(eggs, butter, flour)` that computes
the number of cakes you can bake using the given ingredients.
Each cake requires 5 eggs, 250g butter and 250g of flour.

```javascript
function cakes(eggs, butter, flour)
{
    // Do NOT rely on floor in your translation
    // Use integer division as explained below
    const maxByEggs = Math.floor(eggs / 5);
    const maxByButter = Math.floor(butter / 250);
    const maxByFlour = Math.floor(flour / 250);

    return Math.min(maxByEggs, maxByButter, maxByFlour);
}
```

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
min('t', 'd', 'p')       # Returns 'd'
```

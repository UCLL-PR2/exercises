# Group By

Write a function `group_by(xs, key_function)` that groups elements with the same key in a dictionary.
The key of an element can be found using `key_function`.
A few examples might make this clearer:

## Example 1

```python
def age(person):
    return person.age


>>> group_by([
    Person(name='John', age=14),
    Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
], age)
{
    14: [Person(name='John', age=14)],
    15: [Person(name='Sophie', age=15), Person(name='Morgan', age=15)],
    17: [Person(name='Marc', age=17), Person(name='Chris', age=17)]
}
```

The above code groups `Person`s by age.

## Example 2

```python
def card_suit(card):
    return card.suit


>>> group_by([
    Card(value=2, suit='hearts'),
    Card(value=5, suit='clubs'),
    Card(value=4, suit='hearts'),
    Card(value=10, suit='hearts'),
])
{
    'hearts': [Card(value=2, suit='hearts'), Card(value=4, suit='hearts'), Card(value=10, suit='hearts')],
    'clubs': [Card(value=5, suit='clubs')]
}
```

Here, the same function is used to group cards by suit.

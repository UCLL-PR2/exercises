# Overriding

```python
class Parent:
    def method(self):
        return "Parent.method"

class Child(Parent):
    def other_method(self):
        return "Parent.other_method"
```

Consider the two classes above.

* `Parent` has one method named `method`.
* `Child` has two method: `method` (inherited from `Parent`) and `other_method`.

Let's try something new.
What happens if we write this:

```python
class Parent:
    def method(self):
        return "Parent.method"

class Child(Parent):
    def method(self):
        return "Child.method"
```

Here, `Child` declares a method with exactly the same name as the one in `Parent`.
But is this allowed? The answer is yes. This idea of redefining a method with the same name is called _overriding_ (not overwriting).

What happens is what you would expect happens: the `Child` implementation of `method` "wins".
Take a look at this code:

```python
>>> parent = Parent()
>>> parent.method()
"Parent.method"

>>> child = Child()
>>> child.method()
"Child.method"
```

In this example, one could say that it makes little sense to have `Child` inherit from `Parent` since it overrides all of its parent methods anyway.
Nothing that is inherited survives.
This is true, but there are cases where it still could be useful.

## Task

Create the classes `Customer`, `Item`, `AgeRestrictedItem` and `ShoppingList`.

A `Customer` has attributes `name` and `age`.
We keep it simple: no checks of any kind need to be performed.

An `Item` has a `name` and a `price`.
Also, an `Item` has a method `item.can_be_sold_to(customer)` that checks if it's okay to sell the `item` to the given `customer`.

By default an `Item` can be sold to anyone without restriction.
However, there's a separate class `AgeRestrictedItem` that checks that the `customer` is at least 18.
In other words, `AgeRestrictedItem` is a kind of item (inherits from `Item`) and then overrides the `can_be_sold_to` method.

Lastly, there's a `ShoppingList` class.

* A `ShoppingList` has an `owner` (a `Customer`) and a list of items.
* The `owner` cannot be changed once the `ShoppingList` is created.
* `len(shopping_list)` returns the number of items in the list.
* `shopping_list[i]` returns the `i`th item in the list.
* `shopping_list.add(item)` adds the `item` to the `shopping_list`.
  This is only valid if the `item` can indeed be sold to the owner of the list, otherwise a `ValueError` is thrown.

# Exercise classes & dictionaries: - difficulty level: **

## `Item`

Create a class called `Item` that has two members:

* `name`: a string
* `price`: a float

Both properties should be readonly.

## `Order`

Create a class called `Order` that keeps track of a list of items.
`Order`s should have the following members:

* `order.add_item(item)` adds the given `Item` object to the `items` list.
* `order.remove_item(item)` removes the given `Item` object from the `items` list.
* `order.total_price` the sum of all the prices.
* `len(order)` returns the number of items.
* `order[index]` returns the `index`th item.

## `Customer`

Create a class called `Customer` that has two attributes:

* `name`: a string
* `orders`: a list of `Order` objects

`Customer` objects should have the following members:

* `customer.add_order(order)` adds the given `Order` object to the `orders` list.
* `customer.remove_order(order)` removes the given `Order` object from the `orders` list.
* `customer.total_spent` returns the total amount of money the customer has spent on orders.
* `customer.order_count` returns the number of orders the customer has placed.
* `customer.average_order_size` returns the average size (total price) of the customer's orders.

## `OrderHistory`

Create a class called `OrderHistory` that has one attribute: `customers` (a dictionary where the keys are customer names (strings) and the values are `Customer` objects).
`OrderHistory` objects should have the following methods:

* `history.add_customer(self, customer)` adds the given `Customer` object to the `customers` dictionary.
* `history.remove_customer(self, customer)` removes the `Customer` object with the given name from the `customers` dictionary.
* `history.total_sales(self)` returns the total amount of money that has been spent by all customers.
* `history.customer_names(self)` returns a list of the names of all customers.
* `history.top_spender(self)` returns the name of the customer who has spent the most money.

Write a test function called `test_order_history` that creates a few `Item`, `Order`, `Customer`, and `OrderHistory` objects and tests the methods of these classes to ensure they are working correctly.

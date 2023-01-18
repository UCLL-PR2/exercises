Create a class called `Item` that has two attributes: `name` (a string) and `price` (a float).

Create a class called `Order` that has one attribute: `items` (a list of `Item` objects). The `Order` class should have the following methods:
- `add_item(self, item: Item)`: adds the given `Item` object to the `items` list and updates the total price of the order.
- `remove_item(self, item: Item)`: removes the given `Item` object from the `items` list and updates the total price of the order.
- `get_item_names(self) -> list`: returns a list of the names of the items in the order.

Create a class called `Customer` that has two attributes: `name` (a string) and `orders` (a list of `Order` objects). The `Customer` class should have the following methods:
- `add_order(self, order: Order)`: adds the given `Order` object to the `orders` list.
- `remove_order(self, order: Order)`: removes the given `Order` object from the `orders` list.
- `get_total_spent(self) -> float`: returns the total amount of money the customer has spent on orders.
- `get_order_count(self) -> int`: returns the number of orders the customer has placed.
- `get_average_order_size(self) -> float`: returns the average size (total price) of the customer's orders.

Create a class called `OrderHistory` that has one attribute: `customers` (a dictionary where the keys are customer names (strings) and the values are `Customer` objects). The `OrderHistory` class should have the following methods:
- `add_customer(self, customer: Customer)`: adds the given `Customer` object to the `customers` dictionary.
- `remove_customer(self, customer: Customer)`: removes the `Customer` object with the given name from the `customers` dictionary.
- `get_total_sales(self) -> float`: returns the total amount of money that has been spent by all customers.
- `get_customer_names(self) -> list`: returns a list of the names of all customers.
- `get_top_spender(self) -> str`: returns the name of the customer who has spent the most money.

Write a test function called `test_order_history` that creates a few `Item`, `Order`, `Customer`, and `OrderHistory` objects and tests the methods of these classes to ensure they are working correctly. For this exercise you have to run the tests.py file to run the tests instead of the command **scripting test**.
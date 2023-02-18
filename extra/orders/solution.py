class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class Order:
    def __init__(self):
        self.__items = []

    @property
    def total_price(self):
        return sum(item.price for item in self.__items)

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

class Customer:
    def __init__(self, name):
        self.__name = name
        self.__orders = []

    @property
    def name(self):
        return self.__name

    def add_order(self, order):
        self.__orders.append(order)

    @property
    def total_spent(self):
        return sum([order.total_price for order in self.__orders])

    @property
    def order_count(self):
        return len(self.__orders)


class OrderHistory:
    def __init__(self):
        self.__customers = {}

    def add_customer(self, customer):
        self.__customers[customer.name] = customer

    @property
    def total_sales(self):
        return sum([customer.total_spent for customer in self.__customers.values()])

    @property
    def customer_names(self):
        return list(self.__customers.keys())

    @property
    def top_spender(self):
        return max(self.__customers.keys(), key=lambda x: self.__customers[x].total_spent)

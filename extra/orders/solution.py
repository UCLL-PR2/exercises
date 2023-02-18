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
    def __init__(self, name, orders):
        self.name = name
        self.orders = orders

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        self.orders.remove(order)

    @property
    def total_spent(self):
        return sum([order.total_price for order in self.orders])

    @property
    def order_count(self):
        return len(self.orders)

    @property
    def average_order_size(self):
        return self.get_total_spent() / self.get_order_count()


class OrderHistory:
    def __init__(self, customers):
        self.customers = customers

    def add_customer(self, customer):
        self.customers[customer.name] = customer

    def remove_customer(self, customer):
        del self.customers[customer.name]

    @property
    def total_sales(self):
        return sum([customer.get_total_spent() for customer in self.customers.values()])

    @property
    def customer_names(self):
        return list(self.customers.keys())

    @property
    def top_spender(self):
        return max(self.customers, key=lambda x: self.customers[x].get_total_spent())
class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Order:
    def __init__(self, items: list):
        self.items = items
        self.total_price = sum([item.price for item in items])
    
    def add_item(self, item: Item):
        self.items.append(item)
        self.total_price += item.price
    
    def remove_item(self, item: Item):
        self.items.remove(item)
        self.total_price -= item.price
    
    def get_item_names(self) -> list:
        return [item.name for item in self.items]
    
class Customer:
    def __init__(self, name: str, orders: list):
        self.name = name
        self.orders = orders
    
    def add_order(self, order: Order):
        self.orders.append(order)
    
    def remove_order(self, order: Order):
        self.orders.remove(order)
    
    def get_total_spent(self) -> float:
        return sum([order.total_price for order in self.orders])
    
    def get_order_count(self) -> int:
        return len(self.orders)
    
    def get_average_order_size(self) -> float:
        return self.get_total_spent() / self.get_order_count()
    
class OrderHistory:
    def __init__(self, customers: dict):
        self.customers = customers
    
    def add_customer(self, customer: Customer):
        self.customers[customer.name] = customer
    
    def remove_customer(self, customer: Customer):
        del self.customers[customer.name]
    
    def get_total_sales(self) -> float:
        return sum([customer.get_total_spent() for customer in self.customers.values()])
    
    def get_customer_names(self) -> list:
        return list(self.customers.keys())
    
    def get_top_spender(self) -> str:
        return max(self.customers, key=lambda x: self.customers[x].get_total_spent())
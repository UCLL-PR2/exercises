import pytest
from solution import *



@pytest.fixture
def item():
    return Item(name='Shampoo', price=4)


@pytest.fixture
def order():
    order = Order()
    order.add_item(Item(name='Shampoo', price=4))
    order.add_item(Item(name='Bread', price=3))
    order.add_item(Item(name='Peanuts', price=10))
    return order


@pytest.fixture
def order2():
    order = Order()
    order.add_item(Item(name='Paprika', price=2))
    order.add_item(Item(name='Lasagna', price=8))
    return order


@pytest.fixture
def empty_order():
    return Order()


def test_item():
    item = Item(name='Shampoo', price=4)
    assert item.name == 'Shampoo'
    assert item.price == 4


def test_item_price_is_readonly(item):
    with pytest.raises(AttributeError):
        item.price = 9


def test_item_name_is_readonly(item):
    with pytest.raises(AttributeError):
        item.name = 'Cheese'


def test_length_of_empty_order(empty_order):
    assert len(empty_order) == 0


def test_total_price_of_empty_order(empty_order):
    assert empty_order.total_price == 0


def test_adding_item_updates_length():
    order = Order()

    assert len(order) == 0
    order.add_item(Item('Coke', 2))
    assert len(order) == 1


def test_adding_item_updates_total_price():
    order = Order()

    assert order.total_price == 0
    order.add_item(Item('Coke', 2))
    assert order.total_price == 2
    order.add_item(Item('Bread', 3))
    assert order.total_price == 5


def test_removing_item_updates_length():
    order = Order()
    item = Item('Coke', 2)
    order.add_item(item)

    assert len(order) == 1
    order.remove_item(item)
    assert len(order) == 0


def test_removing_item_updates_total_price():
    order = Order()
    item = Item('Coke', 2)
    order.add_item(item)

    assert order.total_price == 2
    order.remove_item(item)
    assert order.total_price == 0


def test_order_indexing():
    order = Order()
    order.add_item(item1 := Item('Coke', 2))
    order.add_item(item2 := Item('Cheese', 3))
    order.add_item(item3 := Item('Cake', 4))

    assert len(order) == 3
    assert order[0] is item1
    assert order[1] is item2
    assert order[2] is item3


def test_customer_initialization():
    customer = Customer('Peter')
    assert customer.name == 'Peter'
    assert customer.total_spent == 0
    assert customer.order_count == 0


def test_add_order_to_customer(order, order2):
    customer = Customer('Scarlett')
    assert customer.total_spent == 0
    assert customer.order_count == 0

    customer.add_order(order)
    assert customer.total_spent == order.total_price
    assert customer.order_count == 1

    customer.add_order(order2)
    assert customer.total_spent == order.total_price + order2.total_price
    assert customer.order_count == 2


def test_order_history_initialization():
    history = OrderHistory()

    assert history.total_sales == 0
    assert history.customer_names == []


def test_adding_customer():
    soap = Item('Soap', 4)
    microwave = Item('Microwave', 350)
    history = OrderHistory()
    history.add_customer(customer := Customer('Emma'))

    assert history.total_sales == 0
    assert history.customer_names == [customer.name]
    assert history.top_spender == customer.name

    customer.add_order(order := Order())
    order.add_item(soap)
    assert history.total_sales == soap.price

    history.add_customer(customer2 := Customer('Chris'))
    assert history.total_sales == soap.price

    customer2.add_order(order2 := Order())
    order2.add_item(microwave)
    assert history.total_sales == soap.price + microwave.price
    assert history.top_spender == 'Chris'

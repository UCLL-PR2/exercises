import pytest
from solution import *



@pytest.fixture
def item():
    return Item(name='Shampoo', price=4)


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

import pytest
from solution import *


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in globals(), reason=f'{class_name} is not defined')


@pytest.fixture
def customer():
    return Customer('Chris', 20)


@pytest.fixture
def minor_customer():
    return Customer('Chris', 17)


@pytest.fixture
def adult_customer():
    return Customer('Chris', 18)


@pytest.fixture
def shopping_list(customer):
    return ShoppingList(customer)


@pytest.fixture
def shopping_list_minor(minor_customer):
    return ShoppingList(minor_customer)


@pytest.fixture
def shopping_list_adult(adult_customer):
    return ShoppingList(adult_customer)


@pytest.fixture
def unrestricted_item():
    return Item('banana', 10)


@pytest.fixture
def age_restricted_item():
    return AgeRestrictedItem('fireworks', 80)


@if_class_exists('Customer')
@pytest.mark.parametrize('name', ['John', 'Emma', 'Robin'])
@pytest.mark.parametrize('age', [10, 18, 29])
def test_customer(name, age):
    customer = Customer(name, age)
    assert customer.name == name
    assert customer.age == age


@if_class_exists('Item')
@pytest.mark.parametrize('name', ['cookies', 'cake'])
@pytest.mark.parametrize('price', [4, 15, 29])
def test_item(name, price):
    item = Item(name, price)
    assert item.name == name
    assert item.price == price


@if_class_exists('AgeRestrictedItem')
@pytest.mark.parametrize('name', ['cookies', 'cake'])
@pytest.mark.parametrize('price', [4, 15, 29])
def test_age_restricted_item(name, price):
    item = AgeRestrictedItem(name, price)
    assert item.name == name
    assert item.price == price


@if_class_exists('Item')
@if_class_exists('AgeRestrictedItem')
def test_age_restricted_item_is_child_class_of_item():
    assert hasattr(AgeRestrictedItem, '__mro__')
    assert Item in AgeRestrictedItem.__mro__


@if_class_exists('Customer')
@if_class_exists('ShoppingList')
def test_shopping_list_creation(customer):
    shopping_list = ShoppingList(customer)
    assert shopping_list.owner is customer
    assert len(shopping_list) == 0


@if_class_exists('Customer')
@if_class_exists('ShoppingList')
@if_class_exists('Item')
def test_shopping_list_adding_unrestricted_item(shopping_list, unrestricted_item):
    assert len(shopping_list) == 0
    shopping_list.add(unrestricted_item)
    assert len(shopping_list) == 1
    assert shopping_list[0] is unrestricted_item


@if_class_exists('Customer')
@if_class_exists('ShoppingList')
@if_class_exists('Item')
def test_shopping_list_adding_unrestricted_item_to_adults(shopping_list_adult, age_restricted_item):
    assert len(shopping_list_adult) == 0
    shopping_list_adult.add(age_restricted_item)
    assert len(shopping_list_adult) == 1
    assert shopping_list_adult[0] is age_restricted_item


@if_class_exists('Customer')
@if_class_exists('ShoppingList')
@if_class_exists('Item')
@if_class_exists('AgeRestrictedItem')
def test_shopping_list_adding_restricted_item_to_minors_list(shopping_list_minor, age_restricted_item):
    assert len(shopping_list_minor) == 0
    with pytest.raises(ValueError):
        shopping_list_minor.add(age_restricted_item)
    assert len(shopping_list_minor) == 0


@if_class_exists('Customer')
@if_class_exists('ShoppingList')
def test_shopping_list_cannot_change_owner(shopping_list):
    customer = Customer('Bart', 19)
    with pytest.raises(AttributeError):
        shopping_list.owner = customer

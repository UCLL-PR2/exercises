import pytest
import student
import solution


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Person:
    def __init__(self, age):
        self.age = age


@pytest.mark.skipif(not 'count_older_than' in dir(student), reason='count_older_than not found in student module')
@pytest.mark.parametrize("people", [
    [],
    [Person(5)],
    [Person(age) for age in [10, 18, 19, 25]],
    [Person(age) for age in range(100)],
])
@pytest.mark.parametrize("min_age", range(0, 100))
def test_count_older_than(people, min_age):
    expected = solution.count_older_than(people, min_age)
    actual = student.count_older_than(people, min_age)
    assert expected == actual


@pytest.mark.skipif(not 'indices_of_cards_with_suit' in dir(student), reason='indices_of_cards_with_suit not found in student module')
@pytest.mark.parametrize("cards", [
    [],
    [Card(5, 'hearts')],
    [Card(5, 'hearts'), Card(8, 'clubs'), Card(2, 'clubs')],
    [Card(5, 'hearts'), Card(8, 'clubs'), Card(2, 'clubs'), Card(3, 'spades'), Card(7, 'diamonds')],
    [Card(5, 'diamonds'), Card(8, 'clubs'), Card(2, 'clubs'), Card(3, 'spades'), Card(7, 'diamonds')],
])
@pytest.mark.parametrize('suit', ['hearts', 'diamonds', 'clubs', 'spades'])
def test_indices_of_cards_with_suit(cards, suit):
    expected = solution.indices_of_cards_with_suit(cards, suit)
    actual = student.indices_of_cards_with_suit(cards, suit)
    assert expected == actual

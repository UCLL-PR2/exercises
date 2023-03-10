from util import *


def count_older_than(people, min_age):
    def is_older(person):
        return person.age >= min_age
    return count(people, is_older)


def indices_of_cards_with_suit(cards, suit):
    def has_suit(card):
        return card.suit == suit
    return indices_of(cards, has_suit)

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.value, self.suit))

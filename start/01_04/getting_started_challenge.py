"""
Python Object-Oriented Programming Class Example
"""


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


if __name__ == "__main__":
    # instance of the class
    card1 = Card("Ace", "Spades")
    card2 = Card("Queen", "Hearts")
    card3 = Card("Jack", "Diamonds")
    card4 = Card("King", "Clubs")

    print(card1)
    print(card2)
    print(card3)
    print(card4)

from collections import Counter
import random


# A class to represent a card
class Card:
    def __init__(self, rank, suit):

        if rank == "Ace" or rank == "A":
            self.rank = 1

        elif rank == "Jack" or rank == "J":
            self.rank = 11

        elif rank == "Queen" or rank == "Q":
            self.rank = 12

        elif rank == "King" or rank == "Q":
            self.rank = 13

        else:
            self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


# A class to represent a hand of cards
class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, key=lambda x: x.rank, reverse=True)
        self.ranks = [card.rank for card in self.cards]
        self.suits = [card.suit for card in self.cards]

    def is_royal_flush(self):
        if self.is_straight_flush() and self.ranks[0] == 14:
            return True
        return False

    def is_straight_flush(self):
        if self.is_flush() and self.is_straight():
            return True
        return False

    def is_four_of_a_kind(self):
        counter = dict(Counter(self.ranks))
        if 4 in counter.values():
            return True
        return False

    def is_full_house(self):
        counter = dict(Counter(self.ranks))
        if 3 in counter.values() and 2 in counter.values():
            return True
        return False

    def is_flush(self):
        counter = dict(Counter(self.suits))
        if 5 in counter.values():
            return True
        return False

    def is_straight(self):
        if self.ranks[0] - self.ranks[-1] == 4:
            return True
        if self.ranks == [14, 5, 4, 3, 2]:
            return True
        return False

    def is_three_of_a_kind(self):
        counter = dict(Counter(self.ranks))
        if 3 in counter.values():
            return True
        return False

    def is_two_pairs(self):
        counter = dict(Counter(self.ranks))
        if len([x for x in counter.values() if x == 2]) == 2:
            return True
        return False

    def is_one_pair(self):
        counter = dict(Counter(self.ranks))
        if 2 in counter.values():
            return True
        return False

    def evaluate(self):
        if self.is_royal_flush():
            return 'Royal Flush'
        if self.is_straight_flush():
            return 'Straight Flush'
        if self.is_four_of_a_kind():
            return 'Four of a Kind'
        if self.is_full_house():
            return 'Full House'
        if self.is_flush():
            return 'Flush'
        if self.is_straight():
            return 'Straight'
        if self.is_three_of_a_kind():
            return 'Three of a Kind'
        if self.is_two_pairs():
            return 'Two Pairs'
        if self.is_one_pair():
            return 'One Pair'

        return 'High Card'


if __name__ == '__main__':
    # Create a deck of cards
    deck = [Card(rank, suit) for rank in range(1, 14) for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']]

    # Draw a hand of five cards from the deck
    hand = Hand(random.sample(deck, 5))

    # Evaluate the hand
    result = hand.evaluate()

    # Print the result
    print(result)


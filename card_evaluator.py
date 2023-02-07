# A class to represent a card
class Card:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @classmethod
    def from_string(cls, card_string):
        rank_string, suit = card_string.split(' of ')
        rank_index = cls.ranks.index(rank_string)
        return cls(rank_index, suit)

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

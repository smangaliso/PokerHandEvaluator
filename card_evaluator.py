# A class to represent a card
class Card:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

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

    @classmethod
    def from_string(cls, card_string):
        rank_string, suit = card_string.split(' of ')
        rank_index = cls.ranks.index(rank_string)
        return cls(rank_index, suit)

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

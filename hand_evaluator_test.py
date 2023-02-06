import unittest
from hand_evaluator import Hand
from card_evaluator import Card


class TestHandEvaluation(unittest.TestCase):
    def test_high_card(self):
        hand = Hand([Card(2, 'Spades'), Card(10, 'Clubs'), Card(7, 'Hearts'), Card(4, 'Diamonds'), Card(3, 'Spades')])
        self.assertEqual(hand.evaluate(), 'High Card')

    def test_pair(self):
        hand = Hand([Card(2, 'Spades'), Card(2, 'Clubs'), Card(7, 'Hearts'), Card(4, 'Diamonds'), Card(3, 'Spades')])
        self.assertEqual(hand.evaluate(), 'One  Pair')

    def test_two_pairs(self):
        hand = Hand([Card(2, 'Spades'), Card(2, 'Clubs'), Card(7, 'Hearts'), Card(7, 'Diamonds'), Card(3, 'Spades')])
        self.assertEqual(hand.evaluate(), 'Two Pairs')

    def test_three_of_a_kind(self):
        hand = Hand([Card(2, 'Spades'), Card(2, 'Clubs'), Card(2, 'Hearts'), Card(7, 'Diamonds'), Card(3, 'Spades')])
        self.assertEqual(hand.evaluate(), 'Three of a Kind')

    def test_straight(self):
        hand = Hand([Card(2, 'Spades'), Card(3, 'Clubs'), Card(4, 'Hearts'), Card(5, 'Diamonds'), Card(6, 'Spades')])
        self.assertEqual(hand.evaluate(), 'Straight')

    def test_flush(self):
        hand = Hand([Card(2, 'Spades'), Card(10, 'Spades'), Card(7, 'Spades'), Card(4, 'Spades'), Card(3, 'Spades')])
        self.assertEqual(hand.evaluate(), 'Flush')

    def test_full_house(self):
        hand = Hand([Card(2, 'Spades'), Card(2, 'Clubs'), Card(7, 'Hearts'), Card(7, 'Diamonds'), Card(7, 'Spades')])
        self.assertEqual(hand.evaluate(), 'Full House')

    def test_four_of_a_kind(self):
        hand = Hand([Card(2, 'Spades'), Card(2, 'Clubs'), Card(2, 'Hearts'), Card(2, 'Diamonds'), Card(7, 'Spades')])
        self.assertEqual(hand.evaluate(), 'Four of a Kind')

    def test_straight_flush(self):
        hand = Hand([Card(2, 'Spades'), Card(3, 'Spades'), Card(4, 'Spades'), Card(5, 'Spades'), Card(6, 'Spades')])
        self.assertEqual(hand.evaluate(), 'Straight Flush')


if __name__ == '__main__':
    unittest.main()

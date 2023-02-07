from hand_evaluator import Hand
from card_evaluator import Card


def main():
    cards = []
    while len(cards) < 5:
        card_string = input("Enter a card (e.g 'Ace of Spades'): ")
        try:
            card = Card.from_string(card_string)
            if card.suit not in Card.suits:
                raise ValueError(f"Invalid suit '{card.suit}'")
            cards.append(card)
        except Exception as e:
            print(f"Error: {e}")

    hand = Hand(cards)
    print(f"Hand ranking: {hand.evaluate()}")


if __name__ == "__main__":
    main()

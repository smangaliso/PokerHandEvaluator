from hand_evaluator import Hand
from card_evaluator import Card


def main():
    hand = []
    for i in range(5):
        try:
            card_string = input(f"Enter card {i + 1}: ")
            card = Card.from_string(card_string)
            hand.append(card)
        except ValueError as e:
            print("Invalid card format:", e)
        except KeyError as e:
            print("Invalid rank or suit:", e)

    hand = Hand(hand)
    ranking = hand.evaluate()
    print(f"Hand ranking: {ranking}")


if __name__ == "__main__":
    main()

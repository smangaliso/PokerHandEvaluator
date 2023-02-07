from flask import Flask, request, jsonify
from hand_evaluator import Hand
from card_evaluator import Card

app = Flask(__name__)


@app.route('/evaluate_hand', methods=['POST'])
def evaluate_hand():
    # Initialize a try-except block to catch any exceptions related to invalid input
    try:
        # Retrieve the list of cards from the request body, using the key "cards"
        cards = request.get_json()['hand']

        # Check if the number of cards is less than 5 or greater than 5
        if len(cards) < 5 or len(cards) > 5:
            # Return an error message and a 400 Bad Request status code
            return jsonify({"error": "Invalid input, cards must be exactly 5"}), 400

    except KeyError as e:
        # Return an error message and a 400 Bad Request status code if the "hand" key is missing from the request body
        return jsonify({"keyError": "make sure you have the correct key `hand`"}), 400

    except Exception as e:
        # Return an error message and a 400 Bad Request status code if any other exception occurs
        return jsonify({"error": str(e)}), 400

    # Check if the list of cards is empty
    if not cards:
        # Return an error message and a 400 Bad Request status code
        return jsonify({"error": "Invalid input, cards are missing"}), 400

    # Initialize another try-except block to catch any exceptions related to creating the Hand object
    try:
        # Try to convert the cards to Card objects
        hand = [Card.from_string(card) for card in cards]

        # Check if the suit of each card is recognized
        for card in hand:
            if card.suit not in Card.suits:
                return jsonify({"error": "Invalid input, suit not recognized"}), 400

        # Create the Hand object and evaluate the hand ranking
        hand = Hand(hand)
    except Exception as e:
        # Return an error message and a 400 Bad Request status code if any exception occurs
        return jsonify({"error": str(e)}), 400

    # Return the hand ranking as a JSON response
    return jsonify({'hand_ranking': hand.evaluate()})


if __name__ == '__main__':
    app.run(debug=True)

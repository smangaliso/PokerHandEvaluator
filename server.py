from flask import Flask, request, jsonify
from hand_evaluator import Hand
from card_evaluator import Card

app = Flask(__name__)


@app.route('/evaluate_hand', methods=['POST'])
def evaluate_hand():
    cards = request.get_json()['hand']
    hand = Hand([Card.from_string(card) for card in cards])
    return {'hand_ranking': hand.evaluate()}


if __name__ == '__main__':
    app.run(debug=True)

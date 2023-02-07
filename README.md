<h1>Poker Hand Evaluator </h1>

this software tool evaluates a poker hand. it allows a user to submit 5 cards and receive an answer that tells them the highest rank that can be obtained using those 5 cards.

<h3>Getting Started</h3>

1. Install the dependencies:

`pip install -r requirements.txt`

2. Start the development server:
`python server.py`

2.1 Alternatively run:
`python main.py`

3. if you started the development server, the API will be available at `http://localhost:5000`.

<h3>Endpoint</h3>
`/evaluate-hand`: Evaluates the ranking of a hand of cards

<h3>Input</h3>
The input for the API endpoint is in JSON format and must include a key `hand`.

for 2.1 enter one card and press enter.

Example input:

`{
"hand":["Ace of Spades", "10 of Clubs","10 of Hearts", "3 of Diamonds", "3 of Spades"]
}`

for 2.1 the following is the Example input:
`Ace of Spades`

<h3>Output</h3>
The output for the endpoint is in JSON object with the ranking of the hand

Example Output:

`{
"hand_ranking": "Two Pairs"
}`

<h3>Error Handling</h3>
Error Handling If the input is invalid, the API will return a JSON object with an error message and a 400 Bad Request status code.
Also with 2.1 if the input is invalid it will return a message, and prompt you to enter the card again.

Example error output:
`{
"error": "Invalid input, must have exactly 5 cards"
}`

2.1 error output:
`Error: not enough values to unpack (expected 2, got 1)`

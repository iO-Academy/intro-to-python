from random import shuffle


def output_card(card):
    return card['card'] + ' of ' + card['suit']


deck = [
    {"suit": "Hearts", "card": "Two", "value": 2},
    {"suit": "Hearts", "card": "Three", "value": 3},
    {"suit": "Hearts", "card": "Four", "value": 4},
    {"suit": "Hearts", "card": "Five", "value": 5},
    {"suit": "Hearts", "card": "Six", "value": 6},
    {"suit": "Hearts", "card": "Seven", "value": 7},
    {"suit": "Hearts", "card": "Eight", "value": 8},
    {"suit": "Hearts", "card": "Nine", "value": 9},
    {"suit": "Hearts", "card": "Ten", "value": 10},
    {"suit": "Hearts", "card": "Jack", "value": 10},
    {"suit": "Hearts", "card": "Queen", "value": 10},
    {"suit": "Hearts", "card": "King", "value": 10},
    {"suit": "Hearts", "card": "Ace", "value": 11},
    {"suit": "Spades", "card": "Two", "value": 2},
    {"suit": "Spades", "card": "Three", "value": 3},
    {"suit": "Spades", "card": "Four", "value": 4},
    {"suit": "Spades", "card": "Five", "value": 5},
    {"suit": "Spades", "card": "Six", "value": 6},
    {"suit": "Spades", "card": "Seven", "value": 7},
    {"suit": "Spades", "card": "Eight", "value": 8},
    {"suit": "Spades", "card": "Nine", "value": 9},
    {"suit": "Spades", "card": "Ten", "value": 10},
    {"suit": "Spades", "card": "Jack", "value": 10},
    {"suit": "Spades", "card": "Queen", "value": 10},
    {"suit": "Spades", "card": "King", "value": 10},
    {"suit": "Spades", "card": "Ace", "value": 11},
    {"suit": "Clubs", "card": "Two", "value": 2},
    {"suit": "Clubs", "card": "Three", "value": 3},
    {"suit": "Clubs", "card": "Four", "value": 4},
    {"suit": "Clubs", "card": "Five", "value": 5},
    {"suit": "Clubs", "card": "Six", "value": 6},
    {"suit": "Clubs", "card": "Seven", "value": 7},
    {"suit": "Clubs", "card": "Eight", "value": 8},
    {"suit": "Clubs", "card": "Nine", "value": 9},
    {"suit": "Clubs", "card": "Ten", "value": 10},
    {"suit": "Clubs", "card": "Jack", "value": 10},
    {"suit": "Clubs", "card": "Queen", "value": 10},
    {"suit": "Clubs", "card": "King", "value": 10},
    {"suit": "Clubs", "card": "Ace", "value": 11},
    {"suit": "Diamonds", "card": "Two", "value": 2},
    {"suit": "Diamonds", "card": "Three", "value": 3},
    {"suit": "Diamonds", "card": "Four", "value": 4},
    {"suit": "Diamonds", "card": "Five", "value": 5},
    {"suit": "Diamonds", "card": "Six", "value": 6},
    {"suit": "Diamonds", "card": "Seven", "value": 7},
    {"suit": "Diamonds", "card": "Eight", "value": 8},
    {"suit": "Diamonds", "card": "Nine", "value": 9},
    {"suit": "Diamonds", "card": "Ten", "value": 10},
    {"suit": "Diamonds", "card": "Jack", "value": 10},
    {"suit": "Diamonds", "card": "Queen", "value": 10},
    {"suit": "Diamonds", "card": "King", "value": 10},
    {"suit": "Diamonds", "card": "Ace", "value": 11},
]

shuffle(deck)

player1_card1 = deck.pop()
player1_card2 = deck.pop()
dealer_card1 = deck.pop()
dealer_card2 = deck.pop()

player1_score = player1_card1["value"] + player1_card2["value"]
dealer_score = dealer_card1["value"] + dealer_card2["value"]

print('Player drew: ' + output_card(player1_card1))
print('Player drew: ' + output_card(player1_card2))
print("Player current score: " + str(player1_score))

drawAgain = 'Y'
while player1_score < 21 and drawAgain != 'n':
    drawAgain = input('Would you like to draw another card? [Y/n]\n')
    if drawAgain == 'Y':
        player1_card3 = deck.pop()
        player1_score += player1_card3["value"]
        print('Player drew: ' + output_card(player1_card3))
        print("Player new score: " + str(player1_score))

print('\nDealer drew: ' + output_card(dealer_card1))
print('Dealer drew: ' + output_card(dealer_card2))
print("Dealer score: " + str(dealer_score) + '\n')

if player1_score > 21:
    print('Player bust! Dealer wins')
elif dealer_score > 21:
    print('Dealer bust! Player wins')
elif player1_score == dealer_score:
    print('Draw, nobody wins')
elif player1_score > dealer_score:
    print("Player wins!")
else:
    print("Dealer wins :(")







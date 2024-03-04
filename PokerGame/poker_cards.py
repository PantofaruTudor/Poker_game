import random

class Cards():
    class Suit():
        Spades = "\u2660"
        Hearts = "\u2665"
        Diamonds = "\2666"
        Clubs = "\u2663"

    class Ranks():
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9 
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13
        ACE = 14

    #suit:Suit    I SHOULD TRY USING ANNOTATIONS
    #rank:Ranks

    class Card():
        def __init__(self,rank,suit):
            self.suit = suit
            self.rank = rank
        
Cards_deck = []

for i in range(1,14):
    for s in ["\u2660","\u2665","\u2666","\u2663"]:
        Cards_deck.append(Cards.Card(i,s))




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

class Card():
    suit : Suit
    rank : Ranks

    def __str__(self):
        print
        return self.rank.value + self.suit.name

    
a = Card
print(a)
        
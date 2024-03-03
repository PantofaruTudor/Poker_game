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

    class Card():
        def __init__(self,rank,suit):
            self.suit = suit
            self.rank = rank
    """
        def show(self):
            print("{} of {}".format(self.rank,self.suit))"""



    card = Card(12,"\u2660")
    def __init__(self):
        
        self.deck = []
        self.create_deck()

    def create_deck(self):
        for i in range(14):
            for s in ["\u2660","\u2665","\u2666","\u2663"]:
                self.deck.append(Cards.Card(i,s))
    
    def Show_deck(self):
        for i in self.deck:
            print("{} of {}".format(i.rank,i.suit))
    


    
Cards_deck=Cards()
Cards_deck.Show_deck()
Available_card = []



#x = input("how many players?")
#for i in range x:
#random.shuffle(Deck) 


#def create_deck() -> List[Card]:
 #   return [Card()]
    
#deck: List[Card]  #PRIMUL PAS: SA CREEZ DECK-UL 

"""
class Players():
    deck=[]    
    def add_set(self,value,name):
    """    

#a = Card
#print(a)
        
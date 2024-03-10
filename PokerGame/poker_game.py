import random
import time
from poker_cards import Cards_deck,Cards

class player():
    def __init__(self,bet):
        self.bet = bet
        self.deck = []
    def inList(self,card):
        self.deck.append(card)
    def show(self):
        print(self.deck[0].suit,self.deck[0].rank)
winner = False
n=int(input("Welcome to the game. How many players will join?"))
bet = 2
Players = [player]
for i in range(1,n+1):
    pl = player(int(input(f"Bet for player {i}: ")))
    Players.append(pl)
    
random.shuffle(Cards_deck)
community_cards = []

#----------------------------------------------PRE-FLOP

for i in range(1,n+1):
    for j in range(2):
        flop = random.choice(Cards_deck)
        Players[i].inList(flop)
        Cards_deck.remove(flop)
    #Players[i].show() ASTA E PRE-FLOP, FIECARE PLAYER ARE PRIMELE 2 CARTI

#----------------------------------------------
        


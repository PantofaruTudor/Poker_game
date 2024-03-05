import random
from poker_cards import Cards_deck

class player():
    def __init__(self,bet):
        self.bet = bet
        self.deck = []

winner = False
n=int(input("Welcome to the game. How many players will join?"))
bet = 2
Players = [player]
for i in range(1,number+1):
    p = player
    p.bet = int(input(f"Bet for player {i}: "))
    p.deck = []
    Players.append(p)

random.shuffle(Cards_deck)
community_cards = []

"""
for i in range(len(Cards_deck)):
    print(f"{Cards_deck[i].rank} of {Cards_deck[i].suit}")"""

#----------------------------------------------PRE-FLOP

for i in range(1,n+1):
    for d in range(2):
        flop = random.choice(Cards_deck)
        Players[i].deck.append(flop)
        Cards_deck.remove(flop)


#def Pre_flop():


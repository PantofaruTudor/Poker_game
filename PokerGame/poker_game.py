import random
import time
from poker_cards import Cards_deck

class player():
    def __init__(self,bet):
        self.bet = bet
        self.deck = []

winner = False
n=int(input("Welcome to the game. How many players will join?"))
bet = 2
Players = [player]
for i in range(1,n+1):
    pl = player
    pl.bet = int(input(f"Bet for player {i}: "))
    flop = random.choice(Cards_deck)
    Cards_deck.remove(flop)
    pl.deck.append(flop)
    Players.append(pl)
    print(f"Player {i} has {Players[i].deck[0].rank} of {Players[i].deck[0].suit}")

random.shuffle(Cards_deck)
community_cards = []

"""
for i in range(len(Cards_deck)):
    """

#----------------------------------------------PRE-FLOP

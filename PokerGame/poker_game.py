import random
import time
from poker_cards import Cards_deck,Cards

class player():
    def __init__(self,bet):
        self.bet = bet
        self.deck = []
        self.active = True
    def inList(self,card):
        self.deck.append(card)
    def show(self):
        for i in range(2):
            print(self.deck[i].suit,self.deck[i].rank)

def Flop(deck,dealer):
    for _ in range(3):
        card = random.choice(deck)
        dealer.append(card)
        deck.remove(card)

def Pre_flop(deck,players_list):
    for i in range(1,n+1):
        for j in range(2):
            card = random.choice(deck)
            players_list[i].inList(card)
            deck.remove(card)

winner = False
n = int(input("Welcome to the game. How many players will join?"))
min_bet = 2
prize_pool = 0
Pot = []
Players = [player]
Dealer = []

for i in range(1,n+1):
    Pot.append(int(input(f"Pot for player {i} :")))

for i in range(1,n+1):
    pl = player(min_bet)
    Pot[i] -= min_bet
    Players.append(pl)

    
random.shuffle(Cards_deck) 
prize_pool += min_bet*n
Pot = [x-min_bet for x in Pot]
Pre_flop(Cards_deck,Players)
Flop(Cards_deck,Dealer) 

CALL = False
CHECK = False
FOLD = False
RAISE = False
MIN_BET = True




while winner == False:
    if len(Dealer)!=5:
        for i in range(1,n+1):
            if Players[i].active == True:
                response = str(input(f"Player{i}: "))
                if response == "fold":
                    Players[i].active = False
                    break                    #TREBUIE SCHIMBAT AICI CONDITIA, TREBUIE SA INTREB PRIMA DATA DACA E ACTIV JUCATORUL(FOLD)

                bet = int(input(f"Bet for player{i}:"))
                if bet < min_bet:
                    print("Please enter a higher or equal bet.")
                    break
                else:
                    min_bet , Players[i].bet = bet
                    prize_pool =+ bet
                    
        card = random.choice(Cards_deck)
        Dealer.append(card)
        Cards_deck.remove(card)

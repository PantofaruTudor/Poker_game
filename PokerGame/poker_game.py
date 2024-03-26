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
    
def Flops(deck,players_list,dealer):
    for i in range(1,n+1):
        for _ in range(2):
            card = random.choice(deck)
            players_list[i].inList(card)
            deck.remove(card)

    for _ in range(2):
        card = random.choice(deck)
        dealer.append(card)
        deck.remove(card)

def Raise(prize_pool,Pot,i,min_bet):
    bet = int(input(f"Bet for player{i}:"))
    if bet < min_bet:
        while True:
            print("Please enter a higher or equal bet.")
            bet = int(input(f"Bet for player{i}:"))
            if bet > min_bet:
                return bet
            else:
                continue

    elif bet > Pot[i-1]:
        while True:
            print("You do not have enough money for this bet!")
            bet = int(input(f"Bet for player{i}:"))
            if bet <= Pot[i-1]:
                Pot[i-1] -= bet
                return bet
            else:
                continue
    else:
        Players[i].bet = bet
        prize_pool += bet
        Pot[i-1] -= bet
        return bet
        

def Call(prize_pool,min_bet,Pot):
    prize_pool += min_bet
    Pot[i-1] -= min_bet

winner = False
n = int(input("Welcome to the game. How many players will join?"))
min_bet = 2
prize_pool = 0
Pot = []
Players = [player]
Dealer = []

for i in range(1,n+1):
    Pot.append(200) #o sa schimb la final 

for i in range(n):
    pl = player(min_bet)
    Pot[i] -= min_bet
    Players.append(pl)

    
random.shuffle(Cards_deck) 
prize_pool += min_bet*n
Flops(Cards_deck,Players,Dealer) 
Active_players = 0

while len(Dealer)!=5:

    card = random.choice(Cards_deck)
    Dealer.append(card)
    Cards_deck.remove(card)
    for i in range(len(Dealer)):
        print(Dealer[i].rank,Dealer[i].suit)
    print()

    CALL = False
    for i in range(1,n+1):
        if Players[i].active == True:
            response = str(input(f"Player{i}: "))
            #TREBUIE SA TESTEZ FUNCTIILE SI DACA FACE UPDATE LA VARIABILE
            if response == "check":
                if CALL == True:
                    while True:
                        print("You can only choose FOLD/RAISE/CALL")
                        response = str(input(f"Player{i}: "))
                        if response == "call":
                            Call(prize_pool,min_bet,Pot)
                            CALL = True
                            break
                        elif response == "raise":
                            min_bet = Raise(prize_pool,Pot,i,min_bet)
                            prize_pool += min_bet
                            break
                        elif response == "fold":
                            Active_players +=1
                            Players[i].active = False
                            break

            elif response == "fold":
                Active_players += 1
                Players[i].active = False  

            elif response == "call":
                Call(prize_pool,min_bet,Pot)
                prize_pool += min_bet
                CALL = True
            elif response == "raise":
                min_bet = Raise(prize_pool,Pot,i,min_bet)
                prize_pool += min_bet

    if Active_players == n-1:
        print("There could be only one winner!")
        break
    

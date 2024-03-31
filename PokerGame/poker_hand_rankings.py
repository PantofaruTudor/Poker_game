#THIS IS WHERE I WILL MAKE THE RANKINGS
from poker_game import Players,n,Dealer

def deck_merge(DL_deck,PL_deck):
    mrg_deck = []
    n = len(DL_deck)
    m = len(PL_deck)
    i,j = 0
    while i != n and j != m:
        if DL_deck[i].rank <= PL_deck[j].rank:
            mrg_deck.append(DL_deck[i])
            i += 1
        else:
            mrg_deck.append(PL_deck[j])
            j += 1
    while i < n:
        mrg_deck.append(DL_deck[i])
        i += 1
            
def Royal_Flush(deck):
    royal = True
    royal_index = 10
    suit = deck[2].suit
    for i in range(2,7):
        if deck[i].rank == royal_index and deck[i].suit == suit:
            continue
        else:
            royal = False
            break
    return royal

def Straight_Flush(deck):
    str_flush = True
    #suit = 
    i = 6
    if deck[i].rank == deck[i-1].rank+1 == deck[i-2].rank+2:
        for j in range(4,2):
            if deck[j].rank == deck[j-1]+1




    
        
            
        
        

#def winner(n):
        
for i in n:
    if Players[i].active==True:

#THIS IS WHERE I WILL MAKE THE RANKINGS
from poker_game import Players,n,Dealer

def deck_merge(DL_deck,PL_deck):
    mrg_deck = []
    n = len(DL_deck)
    m = len(PL_deck)
    i,j = 0
    while i != n and j != m:
        if DL_deck[i]<PL_deck[j]:
            mrg_deck.append(DL_deck[i])
            
def Royal_Flush(DL_deck,PL_deck,index):
    royal = True
    i = 0
    j = 0
    
        
            
        
        

#def winner(n):
        
for i in n:
    if Players[i].active==True:

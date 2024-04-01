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
    suit = deck[i].suit
    if (deck[i].rank == deck[i-1].rank+1 == deck[i-2].rank+2) and (deck[i].suit == deck[i-1].suit == deck[i-2].suit):
        for j in range(4,2):
            if deck[j].rank == deck[j-1].rank+1 and deck[j].suit == deck[j-1].suit:
                continue
            else:
                str_flush = False
                break
    elif (deck[i-1].rank == deck[i-2].rank+1 == deck[i-3].rank+2) and (deck[i-1].suit == deck[i-2].suit == deck[i-3].suit):
        for j in range(3,1):
            if  deck[j].rank == deck[j-1].rank+1 and deck[j].suit == deck[j-1].suit:
                continue
            else:
                str_flush = False
                return str_flush
            
    #MAI POATE EXISTA O VARIANTA IN CAZUL IN CARE 1 EGAL CU 2 DAR 2 NU EGAL CU 3

def Four_of_a_kind(deck):
    FOAK = False
    index = 0
    ranks = [0 for _ in range(15)]
    for i in range(7):
        ranks[deck[i].rank] += 1
    
    for i in range(7,0,-1):
        if ranks[deck[i].rank] == 4:
            FOAK = True
            index = deck[i].rank
            return FOAK,index
        
    return FOAK

def Full_House(deck):
    F_house = False
    anterior = 0
    posterior = 0
    ranks = [0 for _ in range(15)]
    for i in range(7):
        ranks[deck[i].rank] += 1

    for i in range(15,1):
        if ranks[i] == 2:
            posterior = i
            if anterior != 0:
                F_house = True
                return F_house,anterior,posterior
        elif ranks[i] ==3:
            anterior = i
            if posterior !=0:
                F_house = True
                return F_house,anterior,posterior
            
    return F_house

def Flush(deck):
    flush = False
    suits = [0 for _ in range(5)]
    for i in range(7):
        if deck[i].suit == "\u2660":
            suits[0]+=1
            if suits[0]==5:
                flush = True
                return flush
        elif deck[i].suit == "\u2665":
            suits[1]+=1
            if suits[1]==5:
                flush = True
                return flush
        elif deck[i].suit == "\u2666":
            suits[2]+=1
            if suits[2]==5:
                flush = True
                return flush
        else:
            suits[3]+=1
            if suits[3]==5:
                flush = True
                return flush

    return flush

def Straight(deck):
    


    
        
            
        
        

#def winner(n):
        
for i in n:
    if Players[i].active==True:

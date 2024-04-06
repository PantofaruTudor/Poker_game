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
    return mrg_deck

def index(deck): #aici se indexeaza de cate ori apare fiecare card
    ind = [0 for _ in range(15)]
    for i in range(7):
        ind[deck[i].rank] +=1
    return ind

            
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
    straight = True 
    i = 6
    if (deck[i].rank == deck[i-1].rank+1 == deck[i-2].rank+2):
        if deck[i].suit != deck[i-1].suit or deck[i-1].suit != deck[i-2].suit:
            str_flush = False
        for j in range(4,2):
            if deck[j].rank != deck[j-1].rank+1:  
                return False
            elif deck[j].suit != deck[j-1].suit:
                str_flush = False
                
    elif (deck[i-1].rank == deck[i-2].rank+1 == deck[i-3].rank+2): 
        if deck[i-1].suit != deck[i-2].suit or deck[i-2].suit != deck[i-3].suit: 
            str_flush = False
        for j in range(3,1):
            if  deck[j].rank == deck[j-1].rank+1:
                return False
            elif deck[j].suit != deck[j-1].suit:
                str_flush = False

    if str_flush == False:
        return straight
    else:
        return True
    #AM INCERCAT SA COMBIN STRAIGHT FLUSH SI STRAIGHT(TREBUIE TESTAT)
    #MAI POATE EXISTA O VARIANTA IN CAZUL IN CARE 1 EGAL CU 2 DAR 2 NU EGAL CU 3

def Four_of_a_kind(deck,index):
    FOAK = False
    ind = 0

    for i in range(7,0,-1):
        if index[deck[i].rank] == 4:
            FOAK = True
            ind = deck[i].rank
            return FOAK,ind
        
    return FOAK

def Full_House(deck,index):
    F_house = False
    anterior = 0
    posterior = 0

    for i in range(15,1):
        if index[deck[i].rank] == 2:
            posterior = i
            if anterior != 0:
                F_house = True
                return F_house,anterior,posterior
        elif index[deck[i].rank] ==3:
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
"""
def Straight(deck):
    straight = False
    i = 6
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
            
"""
def three_kind(deck):
    for i in range(6,1,-1):
        if deck[i].rank == deck[i-1].rank == deck[i-2].rank:
            return True
    return False

def Two_Pair(deck,index):
    r_a = 0
    r_b = 0

    for i in range(14,1,-1):
        if index[i]>=2:
            if r_a == 0:
                r_a = i
            elif i != r_a and index[i] >= 2:
                r_b = i
                return True,r_a,r_b

    return False,0,0

def Pair(deck,index):
    for i in reversed(deck):
        if index[i] == 2:
            return True,i

#TREBUIE SA GASESC O METODA SA POT REFOLOSI DOAR O SINGURA DATA VECTORUL INDEX
    

        

    
    
    
        

    
        
            
        
        

#def winner(n):
        
#for i in n:
 #   if Players[i].active==True:

import random
import pandas as pd

values={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
         '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, 'A_as1': 1}

playermatrix1=[["H"]*10, #1
               ["H"]*10,
               ["H"]*10,
               ["H"]*10,
               ["H"]*10, #5
               ["H"]*10,
               ["H"]*10,
               ["H"]*10,
               ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
               ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
               ["D"]*10,
               ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"], #14
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S"]*10, #17
               ["S"]*10,
               ["S"]*10,
               ["S"]*10,
               ["S"]*10
               ]

playermatrix2=[ ["H"]*10, #1
                ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
                ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
                ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
                ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
                ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"], #6
                ["D", "D", "D", "D", "D", "S", "S", "H", "H", "H"], #7
                ["S", "S", "S", "S", "D", "S", "S", "S", "S", "S"],
                ["S"]*10,
                ["S"]*10,
                ["H"]*10]

playermatrix3=[ [], #1
                ["SP", "SP", "SP", "SP", "SP", "SP", "H", "H", "H", "H"],
                ["SP", "SP", "SP", "SP", "SP", "SP", "H", "H", "H", "H"],       
                ["H", "H", "H", "SP", "SP", "H", "H", "H", "H", "H"],
                ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"], #5
                ["SP", "SP", "SP", "SP", "SP", "H", "H", "H", "H", "H"],
                ["SP", "SP", "SP", "SP", "SP", "SP", "H", "H", "H", "H"],
                ["SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP"],
                ["SP", "SP", "SP", "SP", "SP", "S", "SP", "SP", "S", "S"], #9
                ["S"]*10,
                ["SP"]*10]

vals = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, 
            '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 
            'Q': 0, 'K': 0, 'A': 0}

df = pd.DataFrame(vals, index=[0])

df.loc[len(df), :] = [1, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1, -1]
df.loc[len(df), :] = [0, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1, 0]
df.loc[len(df), :] = [1, 1, 2, 2, 1, 1, 0, 0, -2, -2, -2, -2, 0]
df.loc[len(df), :] = [1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -1, -1, -1]
df.loc[len(df), :] = [1, 1, 2, 2, 2, 1, 0, -1, -2, -2, -2, -2, 0]
df.loc[len(df), :] = [1, 1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1, -1]
df.loc[len(df), :] = [0.5, 1, 1, 1.5, 1, 0.5, 0, -0.5, -1, -1, -1, -1, -1]
df.loc[len(df), :] = [1, 1, 2, 2, 2, 1, 0, 0, -2, -2, -2, -2, -1]
df.loc[len(df), :] = [1, 1, 1, 1, 1, 1, 1, 1, -2, -2, -2, -2, 1]

df.rename({0: 'No Strategy',
           1: 'Hi-Lo',
           2: 'Hi-Opt I',
           3: 'Hi-Opt II',
           4: 'KO',
           5: 'Omega II',
           6: 'Red 7',
           7: 'Halves',
           8: 'Zen Count',
           9: '10 Count'}, inplace=True)

def card_counter(cards, strategy='No Strategy'):
    count = sum([df.loc[strategy][card].item() for card in cards])
    return count

def true_counter(count, remaining, strategy='No Strategy'):
    if strategy == 'No Strategy':
        return count
    else:
        return int(round(count/remaining*52))
    
def betting_coefficient(true_count):
    if true_count <= 1:
        bc = 1
    else:
        bc = true_count
    return bc

def new_deck(nr):
    deck=['A', '2','3','4','5','6','7','8','9','10','J','Q','K']*4*nr
    random.shuffle(deck)
    return deck
    
def add_card(player, deck):
    new_card=deck.pop()
    player.append(new_card)
    
def card_value(card):
    return values[card]

def dealer_turn(deck, dealer):
    used_cards = 0
    summa=card_value(dealer[0])+card_value(dealer[1])
    if summa==21:
        return "blackjack", used_cards
    while summa<=16:
        add_card(dealer, deck)
        used_cards += 1
        summa+=card_value(dealer[-1])
    if summa>21:
        if 'A' in dealer:
            summa-=10
    return summa, used_cards
        

def split(player_deck, deck):
    used_cards = 0        
    player_deck_new1 = []
    player_deck_new2 = []

    player_deck_new1.append(player_deck[0])
    add_card(player_deck_new1, deck)
    used_cards += 1

    player_deck_new2.append(player_deck[1])
    add_card(player_deck_new2, deck)
    used_cards +=1

    return [player_deck_new1, player_deck_new2, used_cards]    

def player_turn(deck, player, dealercard):
    used_cards = 0
    summa = card_value(player[0])+card_value(player[1])
    if summa==21:
        return "blackjack", used_cards
    while 1:
        if len(player)==2 and card_value(player[0])==card_value(player[1]):
            step=playermatrix3[card_value(player[0])-1][card_value(dealercard)-2]
        elif len(player)==2 and player[0]=="A" or player[1]=="A":
            if player[0]=="A":
                notA=player[1]
            else:
                notA=player[0]
            step=playermatrix2[card_value(notA)-1][card_value(dealercard)-2]
        else:
            #print(summa-1, dealercard)
            step=playermatrix1[summa-1][card_value(dealercard)-2]
        if step=="S":
            return summa, used_cards
        elif step=="H":
            add_card(player, deck)
            used_cards += 1
            summa+=card_value(player[-1])
            if summa>21:
                for i in range(len(player)):
                    if player[i]=='A':
                        player[i]="A_as1"
                        summa-=10
                        break
                if summa>21:
                    return summa, used_cards
        elif step=="D":
            add_card(player, deck)
            used_cards += 1
            summa+=card_value(player[-1])
            if summa>21:
                for i in range(len(player)):             
                    if player[i]=='A':
                        player[i]="A_as1"
                        summa-=10
                        break         
            return (summa, 1), used_cards
                    
            
        else:                                      #ez a split
        
            player_new = split(player, deck)       #valahol itt is jelezni kell a duplapénzt
            player1 = player_new[0]
            player2 = player_new[1]
            used_cards += player_new[2]
            result = []
            
            summa1=card_value(player1[0])+card_value(player1[1])
            if summa1==21:
                result.append("blackjack") 
            while len(result) < 1:
                if len(player1)==2 and player1[0]=="A" or player1[1]=="A":      #első splitre ki kell breakelni
                    if player1[0]=="A":
                        notA1=player1[1]
                    else:
                        notA1=player1[0]
                    step1=playermatrix2[card_value(notA1)-1][card_value(dealercard)-2]
                else:
                    #print(summa1-1, dealercard)
                    step1=playermatrix1[summa1-1][card_value(dealercard)-2]
                if step1=="S":
                    result.append(summa1)    
                elif step1=="H":
                    add_card(player1, deck)
                    summa1+=card_value(player1[-1])
                    if summa1>21:
                        for i in range(len(player1)):
                            if player1[i]=='A':
                                player1[i]="A_as1"
                                summa1-=10
                                break
                        if summa1>21:
                            result.append(summa1)
                elif step1=="D":
                    add_card(player1, deck)
                    used_cards += 1
                    summa1+=card_value(player1[-1])
                    if summa1>21:
                        for i in range(len(player1)):             #dupla pénzt kell jelezni valahol
                            if player1[i]=='A':
                                player1[i]="A_as1"
                                summa1-=10
                                break         
                    result.append((summa1, 1))
                    

            summa2=card_value(player2[0])+card_value(player2[1])
            if summa2==21:
                result.append("blackjack") 
                return result, used_cards
            while 1:
                if len(player2)==2 and player2[0]=="A" or player2[1]=="A":      #második splitre
                    if player2[0]=="A":
                        notA2=player2[1]
                    else:
                        notA2=player2[0]
                    step2=playermatrix2[card_value(notA2)-1][card_value(dealercard)-2]
                else:
                    #print(summa2-1, dealercard)
                    step2=playermatrix1[summa2-1][card_value(dealercard)-2]
                if step2=="S":
                    result.append(summa2)
                    return result, used_cards
                elif step2=="H":
                    add_card(player2, deck)
                    used_cards += 1
                    summa2+=card_value(player2[-1])
                    if summa2>21:
                        for i in range(len(player2)):
                            if player2[i]=='A':
                                player2[i]="A_as1"
                                summa2-=10
                                break
                        if summa2>21:
                            result.append(summa2)
                            return result, used_cards
                elif step2=="D":
                    add_card(player2, deck)
                    used_cards += 1
                    summa2+=card_value(player2[-1])
                    if summa2>21:
                        for i in range(len(player2)):             #dupla pénzt kell jelezni valahol
                            if player2[i]=='A':
                                player2[i]="A_as1"
                                summa2-=10
                                break         
                    result.append((summa2, 1))
                    return result, used_cards

    
        
def game(deck, nr):
    dealer=[]
    player=[]
    add_card(player, deck)
    add_card(dealer, deck)
    add_card(player, deck)
    add_card(dealer, deck)
    used_cards = 4
    end_player, used = player_turn(deck, player, dealer[0])
    used_cards += used
    
    if type(end_player) == list:                                  #itt kell most a double-t tovább vinni
        result = []
        
        if type(end_player[0]) == tuple:
            if end_player[0][0]!="blackjack" and end_player[0][0]>21:        
                result.append(("L", 1))

            end_dealer, used = dealer_turn(deck, dealer)             #az első split double downnal
            used_cards += used
            if end_player[0][0]=="blackjack":
                if end_dealer=="blackjack":
                    result.append(("T", 1))
                else:
                    result.append(("B", 1))
            elif end_dealer=="blackjack":
                result.append(("L", 1))
            elif end_dealer>21:
                result.append(("W", 1))
            elif end_player[0][0]>end_dealer:
                result.append(("W", 1))
            elif end_player[0][0]<end_dealer:
                result.append(("L", 1))
            else:
                result.append(("T", 1))
            
        else:    
        
            if end_player[0]!="blackjack" and end_player[0]>21:        
                result.append(("L", 0))

            end_dealer, used = dealer_turn(deck, dealer)             #az első split double nélkül
            used_cards += used
            if end_player[0]=="blackjack":
                if end_dealer=="blackjack":
                    result.append(("T", 0))
                else:
                    result.append(("B", 0))
            elif end_dealer=="blackjack":
                result.append(("L", 0))
            elif end_dealer>21:
                result.append(("W", 0))
            elif end_player[0]>end_dealer:
                result.append(("W", 0))
            elif end_player[0]<end_dealer:
                result.append(("L", 0))
            else:
                result.append(("T", 0))
                
                
        if type(end_player[1]) == tuple:
            if end_player[1][0]!="blackjack" and end_player[1][0]>21:        
                result.append(("L", 1))
                return result, used_cards

            end_dealer, used = dealer_turn(deck, dealer)             #a második split double downnal
            used_cards += used
            if end_player[1][0]=="blackjack":                           
                if end_dealer=="blackjack":
                    result.append(("T", 1))
                    return result, used_cards
                else:
                    result.append(("B", 1))
                    return result, used_cards
            elif end_dealer=="blackjack":
                result.append(("L", 1))
                return result, used_cards
            elif end_dealer>21:
                result.append(("W", 1))
                return result, used_cards
            elif end_player[1][0]>end_dealer:
                result.append(("W", 1))
                return result, used_cards
            elif end_player[1][0]<end_dealer:
                result.append(("L", 1))
                return result, used_cards
            else:
                result.append(("T", 1))
                return result, used_cards

        else:    
            
            if end_player[1]!="blackjack" and end_player[1]>21:        
                result.append(("L", 0))
                return result, used_cards

            end_dealer, used = dealer_turn(deck, dealer)             #a második split double nélkül
            used_cards += used
            if end_player[1]=="blackjack":
                if end_dealer=="blackjack":
                    result.append(("T", 0))
                    return result, used_cards
                else:
                    result.append(("B", 0))
                    return result, used_cards
            elif end_dealer=="blackjack":
                result.append(("L", 0))
                return result, used_cards
            elif end_dealer>21:
                result.append(("W", 0))
                return result, used_cards
            elif end_player[1]>end_dealer:
                result.append(("W", 0))
                return result, used_cards
            elif end_player[1]<end_dealer:
                result.append(("L", 0))
                return result, used_cards
            else:
                result.append(("T", 0))
                return result, used_cards

        
        
    elif type(end_player) == tuple:
        if end_player[0]!="blackjack" and end_player[0]>21:        #ez a nem split de double
            return ("L", 1), used_cards
        end_dealer, used = dealer_turn(deck, dealer)
        used_cards += used
        if end_player[0] == "blackjack":
            if end_dealer == "blackjack":
                return ("T", 1), used_cards
            else:
                return ("B", 1), used_cards
        elif end_dealer == "blackjack":
            return ("L", 1), used_cards
        elif end_dealer>21:
            return ("W", 1), used_cards
        elif end_player[0]>end_dealer:
            return ("W", 1), used_cards
        elif end_player[0]<end_dealer:
            return ("L", 1), used_cards
        else:
            return ("T", 1), used_cards
        

    else:
        if end_player!="blackjack" and end_player>21:        #ez a nem split nem double
            return ("L", 0), used_cards
        end_dealer, used = dealer_turn(deck, dealer)
        used_cards += used
        if end_player == "blackjack":
            if end_dealer == "blackjack":
                return ("T", 0), used_cards
            else:
                return ("B", 0), used_cards
        elif end_dealer == "blackjack":
            return ("L", 0), used_cards
        elif end_dealer>21:
            return ("W", 0), used_cards
        elif end_player>end_dealer:
            return ("W", 0), used_cards
        elif end_player<end_dealer:
            return ("L", 0), used_cards
        else:
            return ("T", 0), used_cards

def start_playing(n, nr, money, minbet, strategy):
    deck = new_deck(nr)
    deck_for_count = deck
    nr_game = 0
    num_cards_out = 0
    win = 0
    while (money>0 and nr_game<n):
        if len(deck)<20: #újrakeverünk
            print("Just a few cards left, reshuffling")
            deck = new_deck(nr)
            deck_for_count = deck
            num_cards_out = 0
        while 1:
            if num_cards_out == 0:
                bet = minbet
            else:
                bet = minbet*betting_coefficient(true_counter(card_counter(deck_for_count[-num_cards_out:], strategy), nr*52-num_cards_out, strategy))
                #print(bet)
                #print(true_counter(card_counter(deck_for_count[-num_cards_out:], strategy),nr*52-num_cards_out,))
            if (bet >= minbet and bet <= money):
                break
            else:
                #print("Invalid value, stop playing")
                bet = 0
                break

        if bet == 0:
            break
        else:
            end, used_cards = game(deck, nr)   #itt is a split
            #print("jatek vege", num_cards_out)
            num_cards_out += used_cards
            
            if type(end) == list:
                nr_game += 2
                if end[0][0] == "T":      #elso split
                    #print("Tie :|")
                    pass
                elif end[0][0] == "B":
                    #print("You won :)")
                    money += round(bet*1.5, 0)
                    win += 1

                elif end[0][0] == "W":
                    #print("You won :)")
                    if end[0][1] == 1:
                        money += 2*bet
                    else:
                        money += bet
                    win += 1
                else:
                    #print("You lost :(")
                    if end[0][1] == 1:
                        money -= 2*bet
                    else:
                        money -= bet
                    
                if end[1][0] == "T":         #második split
                    #print("Tie :|")
                    pass
                elif end[1][0] == "B":
                    #print("You won :)")
                    money += round(bet*1.5, 0)
                    win += 1

                elif end[1][0] == "W":
                    #print("You won :)")
                    if end[1][1] == 1:
                        money += 2*bet
                    else:
                        money += bet
                    win += 1
                else:
                    #print("You lost :(")
                    if end[1][1] == 1:
                        money -= 2*bet
                    else:
                        money -= bet
                
                
            else:    
                nr_game += 1       #ha nem volt split
                if end[0] == "T":
                    #print("Tie :|")
                    pass
                elif end[0] == "B":
                    #print("You won :)")
                    money += round(bet*1.5, 0)
                    win += 1

                elif end[0] == "W":
                    #print("You won :)")
                    if end[1] == 1:
                        money += 2*bet
                    else:
                        money += bet
                    win += 1
                else:
                    #print("You lost :(")
                    if end[1] == 1:
                        money -= 2*bet
                    else:
                        money -= bet
    
    #print("-----------------------------------------------------")
    #print("Your strategy was ", strategy, ".", sep="")
    #print("You played ", nr_game, " games, won ", win, " out of these.", sep="")
    #print("Your balance is ", int(money), ".", sep="")
    return money

stats=[]
for j in range(2, 9): 
    print(j)
    stats.append([])
    for i in ['Hi-Lo','Hi-Opt I','Hi-Opt II','KO','Omega II','Red 7','Halves','Zen Count','10 Count']:
        ertek=sum(start_playing(round(j*52/8), j, 10000, 1, i) for _ in range(round(10000/(j*52/8))))/round(10000/(j*52/8))
        stats[-1].append(ertek)
        print(i, ertek)
        
names=['Hi-Lo','Hi-Opt I','Hi-Opt II','KO','Omega II','Red 7','Halves','Zen Count','10 Count']

import matplotlib.pyplot as plt

x=[2, 3, 4, 5, 6, 7, 8]
for i in range(len( stats[0])):
    plt.plot(x, [stats[j][i] for j in range(len(stats))], label=names[i])
leg = plt.legend(loc='lower right')
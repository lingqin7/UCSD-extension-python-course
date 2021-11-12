card_deck=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]

dict={"J":10,"Q":10,"K":10,"A":11}

import random

credit = 5

def two_cards(param1, param2):
    return param1 + param2
    
def you_busted():
    print ("You busted.\n")
    print ("Dealer wins.\n")
    return -1
    
def dealer_busted():
    print ("Dealer busted.\n")
    print ("You win!!!\n")
    return 1
    
def who_wins():
    if (total > dealer_total):
        print ("\nYou win!!!\n")
        return 1
    elif (total < dealer_total):
        print ("\nDealer wins.\n")
        return -1
    else:
        print ("\nPush.\n")
        return 0

def who_wins_when_i_have_a_balckjack():        
    if (card_deck2[3]<10):
        print ("\nDealer doesn't have Blackjack.\n")
        print ("You win!!!\n")
        return 1
    else:
        print ('\nDealer has', card_deck[1],'\t', card_deck[3])
        print ("\nDealer total", two_cards(card_deck2[1],card_deck2[3])) 
        if (two_cards(card_deck2[1],card_deck2[3])<21):
            print ("\nDealer doesn't have Blackjack.\n")
            print ("You win!!!\n")
            return 1
        else:
            print ("\nDealer also has Blackjack.\n")
            print ("Push.\n")
            return 0
    
print ("\n#################################################")
print ("Welcome to the Unofficial One-deck Blackjack Game")
print ("#################################################\n")

print ("Special Rule 1: There will be no splitting or doubling-down")
print ("Special Rule 2: The Ace card is always counted as 11\n")

#For sake of easier code writing: 
#only one game can be played before reshuffling, 
#and although cards are still randomly shuffled, 
#they are not drawn in a strict order as in real life situation.  
#(dealer draws from the 11th card when the player signals "Stand") 

play = input ("Deal cards? (Y/N): ") 
while (play != "N" and credit > 0):  
    
    print ("\nCurrent credit", credit) 
    
    print ("\nGood Luck!\n")

    random.shuffle (card_deck)
    
    card_deck2 = card_deck.copy()
    
    print ("shuffling...    done.\n")

    for pos, val in enumerate(card_deck2):
        #print (pos, ":", val)
        if type (val) == str:
            card_deck2[pos] = dict[val]
    #covert J,Q,K,A to integers in the list copy card_deck2. 
    #Later card_deck will be shown, but calculation is done 
    #on its copy card_deck2 with all integers
    
    if (card_deck2[0]==card_deck2[2]==11 or card_deck2[1]==card_deck2[3]==11):
        continue
    #in the quite unlikely event (2/169) of being dealt two Ace acrds to begin 
    #for either dealer or the player, go back to the top of the whole loop 
    #and perform another random shuffling to avoid this circumstance of busting 
    #at the beginning of the game. (because Ace card is always counted as 11)
    
    print ('You have  ',card_deck[0],"\t",card_deck[2],"\n")
    total = two_cards(card_deck2[0],card_deck2[2])
    print ("Total", total,"\n")
    
    print ('Dealer has  ?\t', card_deck[3],"\n")
    
    if (total==21):
        print ("Blackjack!!!")
        credit = credit + who_wins_when_i_have_a_balckjack()
        print ("Current credit", credit,"\n")
        play = input ("Deal cards again? (Y/N): ")
        
    if (total < 21):
        decision = input ('Hit (H) or Stand (S)? ')
        if (decision == 'H'):
            print ('\nYou have  ',card_deck[0],"\t",card_deck[2],"\t",card_deck[4])
            total = total + card_deck2[4]
            print ("\nTotal", total,"\n")
            if (total > 21):
                credit = credit + you_busted()
                print ("Current credit", credit,"\n")
                play = input ("Deal cards again? (Y/N): ")
            else:
                decision = input ('Hit (H) or Stand (S)? ')
                
                if (decision == 'H'):
                    print ('\nYou have  ',card_deck[0],"\t",card_deck[2],"\t",card_deck[4],"\t",card_deck[5])
                    total = total + card_deck2[5]
                    print ("\nTotal", total,"\n")                    
                    if (total > 21):
                        credit = credit + you_busted()
                        print ("Current credit", credit,"\n")
                        play = input ("Deal cards again? (Y/N): ")
                    else: 
                        decision = input ('Hit (H) or Stand (S)? ')
                        
                        if (decision == 'H'):
                            print ('\nYou have  ',card_deck[0],"\t",card_deck[2],"\t",card_deck[4],"\t",card_deck[5],'\t',card_deck[6])
                            total = total + card_deck2[6]
                            print ("\nTotal", total,'\n')                   
                            if (total > 21):
                                credit = credit + you_busted()
                                print ("Current credit", credit,"\n")
                                play = input ("Deal cards again? (Y/N): ")
                            else: 
                                decision = input ('Hit (H) or Stand (S)? ')
                                
                                if (decision == 'H'):
                                    print ('\nYou have  ',card_deck[0],"\t",card_deck[2],"\t",card_deck[4],"\t",card_deck[5],'\t',card_deck[6],'\t',card_deck[7])
                                    total = total + card_deck2[7]
                                    print ("\nTotal", total,'\n')
                                    if (total > 21):
                                        credit = credit + you_busted()
                                        print ("Current credit", credit,"\n")
                                        play = input ("Deal cards again? (Y/N): ")
                                    else: 
                                        print ("You have reached the end of the program. Select Stand (S) now.")
                                        decision = input ('Hit (H) or Stand (S)? ')
            
        if (decision == "S"):
            print ('\nDealer has', card_deck[1],'\t', card_deck[3])    
            dealer_total = two_cards(card_deck2[1],card_deck2[3])
            print ("\nDealer total", dealer_total,'\n')
            
            if (dealer_total ==21):
                print ("Blackjack!!!\n")
            
            if (dealer_total >= 17):
                print (f"Let's see. You have {total} and dealer has {dealer_total}.")
                credit = credit + who_wins()
                print ("Current credit", credit,"\n")
                play = input ("Deal cards again? (Y/N): ")
            else:
                print ("Dealer must draw another card...")
                print ('\nDealer has', card_deck[1],'\t', card_deck[3], '\t', card_deck[10])
                dealer_total=dealer_total + card_deck2[10]
                print ("\nDealer total", dealer_total,'\n')
            
                if (dealer_total>21):
                    credit = credit + dealer_busted()
                    print ("Current credit", credit,"\n")
                    play = input ("Deal cards again? (Y/N): ")
                elif (dealer_total >= 17):
                    print (f"Let's see. You have {total} and dealer has {dealer_total}.")
                    credit = credit + who_wins()
                    print ("Current credit", credit,"\n")
                    play = input ("Deal cards again? (Y/N): ")
                else:
                    print ("Dealer must draw another card...")
                    print ('\nDealer has', card_deck[1],'\t', card_deck[3], '\t', card_deck[10], '\t', card_deck[11])
                    dealer_total=dealer_total + card_deck2[11]
                    print ("\nDealer total", dealer_total,'\n')
                    
                    if (dealer_total>21):
                        credit = credit + dealer_busted()
                        print ("Current credit", credit,"\n")
                        play = input ("Deal cards again? (Y/N): ")
                    elif (dealer_total >= 17):
                        print (f"Let's see. You have {total} and dealer has {dealer_total}.")
                        credit = credit + who_wins()
                        print ("Current credit", credit,"\n")
                        play = input ("Deal cards again? (Y/N): ")
                    else:
                        print ("Dealer must draw another card...")
                        print ('\nDealer has', card_deck[1],'\t', card_deck[3], '\t', card_deck[10], '\t', card_deck[11], '\t', card_deck[12])
                        dealer_total=dealer_total + card_deck2[12]
                        print ("\nDealer total", dealer_total,'\n')
                        
                        if (dealer_total>21):
                            credit = credit + dealer_busted()
                            print ("Current credit", credit,"\n")
                            play = input ("Deal cards again? (Y/N): ")
                        elif (dealer_total >= 17):
                            print (f"Let's see. You have {total} and dealer has {dealer_total}.")
                            credit = credit + who_wins()
                            print ("Current credit", credit,"\n")
                            play = input ("Deal cards again? (Y/N): ")
                        else:
                            print ("You have reached the end of the program. \nIt is unbelievable that the dealer is still under 17 after 5 cards are dealt.")
                            play = input ("Deal cards again? (Y/N): ")
            
    if (credit == 0):
        print ("\nUnfortunately you have run out of credits. \n\nThe good news is that for a limited time only, you can borrow for a special low 39.99% APR.\n")
        joke = input ("Interested? Y/N: ")
        credit = input ("\nJust kidding! Enter the number of credits you want to add: ")
        credit = int (credit)

print ("\n#########################################")                
print ("Thank you for playing. Come again soon!!!") 
print ("#########################################\n")        
        
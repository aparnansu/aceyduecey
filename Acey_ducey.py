#Unit 5: Assignment two
#Play Acey Ducey
#
# Author: Aparna.N

import random
from play_cards import Playcards,card

ante=100
ac=Playcards()
random.shuffle(ac.cards)



while(True):
    #deal two cards
    card_one=ac.deal()
    card_two=ac.deal()
    if(card_one is None or card_two is None):
        print("Card deck is empty")
        break
    print("picked the cards ",card_one.getString(), card_two.getString())
    user_input=input("Do you want to pick the third card? Press (Y/N)")
    if(user_input!='Y' and user_input!='y'):
        break
    card_one=card('Q','H')
    card_two=card('9','H')
    if(card_one.actual_value!=card_two.actual_value):
        bet=int(input("What is the money that you want to bet?(between 1 and 100)"))
        card_three=ac.deal()#deal third card
        card_three=card('10','S')
        if(card_three is None):
            print("Card deck is empty")
            break
        print("picking third card ", card_three.getString())

        print("condition 1:",card_three.actual_value>card_one.actual_value)
        print("condition 2:",card_three.actual_value<card_two.actual_value)
        
        if((card_three.actual_value>card_one.actual_value and card_three.actual_value<card_two.actual_value)or
           (card_three.actual_value>card_two.actual_value and card_three.actual_value<card_one.actual_value)):
            ante-=bet
            print("You have won $",bet,"!!")
            bet*=2
        elif(card_three.actual_value==card_one.actual_value or card_three.actual_value==card_two.actual_value):
            ante+=bet*2            
            print("You lose your bet $",(bet*2) )
            bet=0
        else:
            print("You lost your bet $", bet)
            ante+=bet
            bet=0
            
        
        
    if(ante<=0):
        print("There is no more money left to bet")
        break

    
    user_input=input("Do you want to play again? Press (Y/N)")
    if(user_input!='Y' and user_input!='y'):
        break
print("GAME OVER. Dealer value: ", max(0, ante))



    

    
        
        
    




    
    

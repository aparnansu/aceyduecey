#The playing cards program
#Author: Aparn

from operator import itemgetter,attrgetter
import random
#card item
class card:
    def __init__(self,f_value,c_type):
        self.f_value=f_value
        self.c_type=c_type
        self.setActualValue(f_value)
       
        
    def setActualValue(self,f_value):
        if f_value=='J':
            self.actual_value=11
        elif f_value=='Q':
            self.actual_value=12
        elif f_value=='K':
            self.actual_value=13
        elif f_value=='A':
            self.actual_value=14                
        else:
            if(int(self.f_value) >= 2 and int(self.f_value)<=10):
                self.actual_value=int(self.f_value)
        
    def getString(self):
        return self.f_value+''+self.c_type     
         
#managing list of cards
class Playcards:

    cards=[]
    dealt_cards=[]
    def __init__(self):
        self.initialize_cards()

#create deck of cards
    def initialize_cards(self):
        s1=['C','D','H','S']
        s2=['2','3','4','5','6','7','8','9','10','J','Q','K','A']

        self.cards=[]
        for i in range(len(s1)):
            for j in range(len(s2)):
                newCard = card(s2[j],s1[i])
                self.cards.append(newCard)

#deal - return the topmost card from the deck   
       
    def deal(self):
        try:
            dealt_card= self.cards.pop(0)
            self.dealt_cards.append(dealt_card)
            #return (dealt_card.f_value)+(dealt_card.c_type)
            return dealt_card
            
        except (IndexError):
            print("The card deck is empty")

#shuffling cards
    def shuffle(self):
        #print("shuffling")
        self.cards=self.cards+self.dealt_cards
        self.dealt_cards=[]
        random.shuffle(self.cards)
        #self.fan()
        
       
#display deck
    def fan(self):
        printString=[]
        for card in self.cards:            
            printString.append(card.getString())
            #print(card.getString())
        print(printString)
        #k= len(printString)
        #print(k)
    
#check if deck is ordered - compare list of cards with sorted list            
    def isOrdered(self):    
        unsorted_list = self.cards
        sorted_list = self.Order()
        for i in range(len(unsorted_list)):
           if (unsorted_list[i]!=sorted_list[i]):
               return False
        return True            
    
# Sort the cards in order        
    def Order(self):
         return sorted(self.cards,key=attrgetter('c_type','actual_value'))

    def print_dealtcards(self):
        print(Playcards.dealt_cards[0])

#test_code
'''
pc=Playcards()
print("Initialized the cards")
for i in range(0, 55):
    card = pc.deal()
    if(card is not None):
        print("Dealing card", (i+1), card.getString())
    else:
        print("Nothing is returned")

pc.fan()
print("Shuffling cards")
pc.shuffle()
pc.fan()
print("The dealt card is",pc.deal())

if(pc.isOrdered()):
    print("The deck is ordered")
else:
    print("The deck is not in order")

pc.print_dealtcards()

'''




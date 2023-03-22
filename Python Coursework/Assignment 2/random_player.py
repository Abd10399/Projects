#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing previous modules
from card1 import *
from card2 import *
from game import *
import random


def draw(hand, top_discard_card):
    """(list,int or None) -> str
    Takes a list and an integer/None for parameters and returns whether the player will draw a card from stock or the discard pile randomly
    
    >>> random.seed(786)


    >>> draw([4,50,15,21], 6)
    'stock'

    >>> draw([14,50,15,21],9)
    'discard'
        
    >>> draw([14,50,15,21],20)
    'discard'

    """
    #Checks whether or not there is a top discard card
    if top_discard_card == None:
        return 'stock'
    #Generates random number between 0 and 1 and chooses the respective probability for stock or discard
    if random.random()>0.5:
        return 'stock'
    else:
        return 'discard'
    
def discard(hand):
    """(list) -> int
    Given a list, selects a random number from the list
    
    >>> random.seed(786)
    
    >>> discard([4, 50, 15, 21])
    15
    
    >>> discard([44, 50, 15, 21])
    44
    
    >>> discard([46, 50, 15, 21])
    15
    
    """
    #Generates and returns a random integer between 0 and lenght of the list
    return hand[random.randint(0,len(hand)-1)]
    
#End of Program
    
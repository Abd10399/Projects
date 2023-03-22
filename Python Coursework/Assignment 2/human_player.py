#Author: Mohammad Abdullah
#Student ID: 260980866

from card2 import *



#Defining functions


def draw(hand, top_discard_card):
    """(list,int or None) -> str
    Takes a list and an integer/None for parameters and returns whether the player will draw a card from stock or the discard pile
    
    >>> draw([10, 50, 15, 11], 26)
    Draw location: stock
    'stock'

    >>> draw([4, 50, 15, 21], 5)
    Draw location: stock
    'stock'

    >>> draw([10, 50, 15, 21], 10)
    Draw location: discard
    'discard'

    """
    
    #Asks user for input
    input1 = input("Draw location: ")
    
    #Returns the input
    return input1

def discard(hand):
    """(list) -> int
    Given a list of cards, displays them and asks user to select from an index and then returns the corresponding card #
    
    >>> discard([4, 50, 15, 21])
    0       TWO of SPADES
    1       ACE of DIAMONDS
    2       FIVE of CLUBS
    3       SEVEN of HEARTS
    Choice: 2
    15

    >>> discard([14, 52, 15, 21])
    0       FIVE of DIAMONDS
    1       ACE of SPADES
    2       FIVE of CLUBS
    3       SEVEN of HEARTS
    Choice: 3
    21

    >>> discard([20, 52, 15, 30])
    0       SIX of SPADES
    1       ACE of SPADES
    2       FIVE of CLUBS
    3       NINE of DIAMONDS
    Choice: 0
    20

    """
    #Iterates through each index of the list for printing the UI
    for i in range(len(hand)):
        
        #Creates a UI with the index of the corresponding element, 2 tabs and it's string representation
        print(str(i) + "\t\t" + card_to_string(hand[i]))
        
    choice = int(input("Choice: "))
    
    #return the user's choice's corresponding card number
    return hand[choice]

#End of Program
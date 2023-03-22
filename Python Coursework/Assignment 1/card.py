#Author: Mohammad Abdullah, Student ID: 260980866

#Defining the global variables
HEARTS = 0 
DIAMONDS = 1
CLUBS = 2
SPADES = 3

TWO = 0
THREE = 1
FOUR = 2
FIVE = 3
SIX = 4
SEVEN = 5
EIGHT = 6
NINE = 7
TEN = 8
JACK = 9
QUEEN = 10
KING = 11
ACE = 12

#Defining the functions for the program
def get_suit(card):
    """ (int) ->int
    Calculates and returns the suit of the card from 0 to 3
    
    >>> get_suit(21)
    0
    
    >>> get_suit(19)
    2
    
    >>> get_suit(4)
    3
    """
    
    #Checks whether the card num % 4 is 0, since if it is then its divisible by 4
    #If its divisible by 4, then the suit must be Spade, which is 3 according to data
    #This is why we must return the (modulus of 4)-1 to get the correct suit according to the remainder.
    if card % 4 == 0: 
        return 3
    else:
        return (card % 4) - 1

def get_rank(card):
    """ (int) ->int
    Calculates and returns the rank of the card as provided from 1 to 12
    
    >>> get_rank(5)
    1
    
    >>> get_rank(49)
    12
    
    >>> get_rank(10)
    2
    """
    
    #Checks if card is divisbile by 4
    if card % 4 == 0:
        #If Divisible, then returns the value of the floor division by 4 minus 1
        #If we dont subtract 1, then answer will be 1 greater than the expected answer
        return (card // 4) - 1
    else:
        return (card // 4)
    
    
def same_rank(card1, card2):
    """ (int,int) -> Bool
    Checks whether card1 and card2 have the same rank
    
    >>> same_rank(1, 3)
    True
    
    >>> same_suit(16,17)
    False
    
    >>> same_suit(6,52)
    False
    """
    
    #Checks whether the card representations are of the same rank or not
    if get_rank(card1) == get_rank(card2):
        return True
    else:
        return False

def same_suit(card1, card2):
    """ (int,int) -> Bool
    Checks whether card1 and card2 belong to the same suit
    
    >>> same_suit(16,5)
    False
    
    >>> same_suit(13,5)
    True
    
    >>> same_suit(1,1)
    True
    """
    
    #Checks whether the card representations are of the same suit or not
    if get_suit(card1) == get_suit(card2):
        return True
    else:
        return False
        
    
def same_color_suit(card1, card2):
    """ (int,int) -> Bool
    Checks whether the integer representation of card1 and card2 are cards of the same color
    
    >>> same_color_suit(1, 3)
    False
    
    >>> same_color_suit(1, 2)
    True
    
    >>> same_color_suit(1, 50)
    True
    """
    #Gets values of suit for card1 and card2 and puts them in variables a and b
    a = get_suit(card1)
    b = get_suit(card2)
    #Checks whether the cards have the same suit (and hence same color)
    if same_suit(card1,card2):
        return True
    elif a+b == 1 or a+b == 5: #Checks whether cards have unlike suits of the same colour
        return True
    
    return False
    
    
    
    
    
    
    
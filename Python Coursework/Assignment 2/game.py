#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing important modules
from card2 import *
from card1 import *

#Defining the major functions:

def calculate_winner(points):
    """(list) -> list
    Takes a list of scores and returns the index of the lowest score(s)
    
    >>> calculate_winner([100, 5, 20, 5])
    [1, 3]

    >>> calculate_winner([100, 5, 20, 5, 14, 5])
    [1, 3, 5]

    >>> calculate_winner([1])
    [0]

    """
    #Initializing the variables of list and minimum
    list1 = []
    minimum = points[0]
    
    #Loops through the indexes of the list points, assigns the minimum value to
    for element in points:
        if element < minimum:
            minimum = element #Assigns the current element as the new minimum
            
    #Runs another for loop to check for the index of the minimum element and append it to the list
    for i in range(len(points)):
        if points[i] == minimum:
            list1.append(i)
            
    #Returns the final list
    return list1

            
def calculate_round_points(hand):
    """(list) -> int
    Returns the amount of points calculated by the cards in the player's "hand" (list)
    
    >>> calculate_round_points([49, 50, 51, 52])
    4

    >>> calculate_round_points([49, 50, 51, 48])
    13

    >>> calculate_round_points([5, 50, 51, 48])
    15

    """
    #Initializes the total sum
    total_sum = 0
    
    #Loop through each card in the hand
    for element in hand:
        
        #Checking and computing the value of each card in the hand and adding it to the total appropriately
        if get_rank(element) >= 0 and get_rank(element) <=8:
            total_sum += get_rank(element) + 2
        elif get_rank(element) >= 9 and get_rank(element) <=11:
            total_sum += 10
        elif get_rank(element) == 12:
            total_sum += 1
    
    #Returning the total
    return total_sum

def is_valid_group(cards):
    """(list) -> Bool
    Takes a list of cards and returns whether or not they make a valid group (atleast 3 cards of the same rank)

    >>> is_valid_group([1, 2, 3, 52])
    False

    >>> is_valid_group([1, 3, 52])
    False
        
    >>> is_valid_group([9,10,11,12])
    True

    """
    #Checks if there are atleast 3 cards
    if len(cards) < 3:
        return False
    
    #Checks whether all of the cards are of the same rank
    return all_same_rank(cards)


def is_valid_sequence(cards):
    """(list) -> Bool
    Checks whether the cards in the list "cards" form a valid sequence (same suit, increasing rank)
    
    >>> is_valid_sequence([34, 38, 30])
    True

    >>> is_valid_sequence([18,14,10])
    True

    >>> is_valid_sequence([19,14,10])
    False

    """
    #Sort the list in ascending order (since ranks increase with card number)
    cards.sort()
    
    #Checks if there are atleast 3 cards
    if len(cards) < 3:
        return False
    
    #Check if the cards have the same suit
    if all_same_suit(cards):
        for i in range(len(cards)-1):
            if get_rank(cards[i]) > get_rank(cards[i+1]):
                return False
        #If it passes all the tests, return true
        return True
    else:
        return False
    
#End of Program
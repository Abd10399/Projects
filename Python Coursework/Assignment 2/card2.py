#Author: Mohammad Abdullah
#Student ID: 260980866

from card1 import *
#Defining the global Variables

SUITS = [0,1,2,3]
RANKS = [0,1,2,3,4,5,6,7,8,9,10,11,12]
SUITS_STR = ["HEARTS", "DIAMONDS", "CLUBS", "SPADES"]
RANKS_STR = ['TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE','TEN', 'JACK', 'QUEEN', 'KING', 'ACE']

#Defining the functions

def get_card(suit, rank):
    """(int,int) -> int
    Takes the suit and rank of the card and returns the specific card's integer representation

    >>> get_card(2,7)
    31

    >>> get_card(1,5)
    22

    >>> get_card(1,10)
    42
    
    """
    #4 Ranks, which is why we multiply rank by 4, and suits are actually 4 in number but are measured from 0-3 which is why we add 1
    return (4*rank) + (suit+1)

def card_to_string(card):
    """(int) -> str
    Takes the integer representation of card and tells us it's rank and suit in the form "Rank" of "Suit"
    
    >>> card_to_string(49)
    'ACE of HEARTS'
    
    >>> card_to_string(50)
    'ACE of DIAMONDS'
    
    >>> card_to_string(51)
    'ACE of CLUBS'

    """
    #Uses functions from card1 to get the rank and suit and displays it using the global variables declared at the top
    return RANKS_STR[get_rank(card)] + " of " + SUITS_STR[get_suit(card)]

def hand_to_string(hand):
    """(list) -> str
    Takes a list called hand and returns all the names of the different card pieces which are in the list

    >>> hand_to_string([1, 2, 3, 4])
    'TWO of HEARTS, TWO of DIAMONDS, TWO of CLUBS, TWO of SPADES'

    >>> hand_to_string([1, 10, 3, 6])
    'TWO of HEARTS, FOUR of DIAMONDS, TWO of CLUBS, THREE of DIAMONDS'

    >>> hand_to_string([1, 10, 15, 6])
    'TWO of HEARTS, FOUR of DIAMONDS, FIVE of CLUBS, THREE of DIAMONDS'
        
    """
    #Initializes an empty string which will be returned
    new_str = ''
    counter = 0 #Used to check whether the end of loop is reached
    
    #loops through elements of the list sequentially
    for element in hand:
        new_str += card_to_string(element)
        
        #Checks to see if the last element is reached for adding the comma and space
        if counter != len(hand) -1:
            new_str += ", "
            counter += 1
    #Returns final concatenated string
    return new_str
        
def get_deck():
    """(None) -> str
    Returns a list containing 52 unique cards
    
    >>> deck = get_deck()
    >>> len(deck)
    52

    >>> get_deck()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

    >>> deck = get_deck()
    >>> last_card = deck[-1]
    >>> last_card
    52

    
    """
    #Creates an empty list
    list1 = []
    #Iterates 52 times, from 1 to 52 inclusive and adds all the corresponding numbers to list1
    for i in range(1,53):
        list1.append(i)
    #Returns the curated list
    return list1

def all_same_suit(cards):
    """(list) -> Bool
    Takes a list of cards and checks whether they're all in the same suit
    
    >>> all_same_suit([1, 2, 3, 4])
    False

    >>> all_same_suit([1, 5, 5, 5])
    True

    >>> all_same_suit([1, 5, 9, 13])
    True

    """
    #Checks for empty list -> must return True then
    if cards == []:
        return True
    #Checks suit of the 1st card and assigns it to test_card
    test_card = get_suit(cards[0])
    
    #Loops through the list of cards checking whether the suits of all the cards match the suit of test_card.
    for element in cards:
        if not(get_suit(element) == test_card):
            return False #If even 1 card is different, then function returns false
        
    #Returns True if all cards are the same
    return True
        
def all_same_rank(cards):
    """(list) -> Bool
    Checks whether all the items (cards) in the list "cards" are of the same rank
    
    >>> all_same_rank([4, 52])
    False

    >>> all_same_rank([1,4])
    True

    >>> all_same_rank([1,52])
    False
    
    """
    #Checks for empty list -> must return True then
    if cards == []:
        return True
    #Checks rank of the 1st card and assigns it to test_card
    test_card = get_rank(cards[0])
    
    #Loops through the list checking whether the ranks of all the cards match or not
    for element in cards:
        if not(get_rank(element) == test_card):
            return False
    
    #If they are all same, return's True
    return True

        
#End of Program
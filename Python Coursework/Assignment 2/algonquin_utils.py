#Author: Mohammad Abdullah
#Student ID: 260980866

#Defining the Global Variables

CONSONANTS = "bcdghkmnpstwyzj"
VOWELS = "aeio"
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

#Helper functions
def is_valid_punctuation(str1):
    """(str1) -> Bool
    Checks whether the punctuation is valid or not
    
    >>> is_valid_punctuation(" ")
    True
    
    >>> is_valid_punctuation("!")
    True
    
    >>> is_valid_punctuation("@")
    False
    """
    #Simply returns a boolean that tells us whether this is a defined punctuation/space
    return (str1 in PUNCTUATION) or (str1 == " ")
    

def is_valid_diphthong(str1):
    """(str) -> Bool
    Checks whether the Diphthon is Valid or not
    
    >>> is_valid_diphthong("ey")
    True
    
    >>> is_valid_diphthong("yo")
    False
    
    >>> is_valid_diphthong("wew")
    False
    
    """
    str2 = str1.lower() #Converts to lowercase
    if len(str2) == 2: #Checks lenght and whether it's part of the defined global variables or
        return str2 in DIPHTHONGS
    else:
        return False


#Required Functions


def is_valid_consonant(str1):
    """(str) -> Bool
    Checks whether the consonant is Valid or not
    
    >>> is_valid_consonant("a")
    False

    >>> is_valid_consonant("z")
    True

    >>> is_valid_consonant("n")
    True
    
    """
    str2 = str1.lower() #Converts to Lower Case
    if len(str2) == 1: #Confirms lenght and checks through the global variables
        return str2 in CONSONANTS
    else:
        return False
    
def is_valid_vowel(str1):
    """(str) ->Bool
    Checks whether the vowel is valid
    
    >>> is_valid_vowel("a")
    True
    
    >>> is_valid_vowel("c")
    False
    
    >>> is_valid_vowel("e")
    True
    
    """
    str2 = str1.lower()
    if len(str2) == 1:
        return (str2 in VOWELS) or (str2 in VOWELS_WITH_ACCENT)
    else:
        return False
    
def is_valid_single_word(str1):
    """(str) -> Bool
    Checks whether the string is a valid single word
    
    >>> is_valid_single_word("larry")
    False
    
    >>> is_valid_single_word("aay")
    True
    
    >>> is_valid_single_word("BlaCk")
    Fales
    
    """
    for s in str1: #Loops through str1
        if not(is_valid_vowel(s)) and not(is_valid_consonant(s)): #Confirms usage of any unknown characters that return False
            return False
    return True
            
def is_valid_phrase(str1):
    """(str) -> Bool
    Checks whether str1 is a valid phrase
    
    >>> is_valid_phrase("l o l")
    False
    
    >>> is_valid_phrase("ayayayaya")
    True
    
    >>> is_valid_phrase('Andi ejayan?')
    True
    
    """
    #Loops through the string
    for s in str1:
        #Makes sure that it encompases all possible script that we have been provided with
        if not(is_valid_vowel(s)) and not(is_valid_consonant(s)) and not(is_valid_punctuation(s)):
            return False
        #Returns Boolean value
    return True
        
#End of Program
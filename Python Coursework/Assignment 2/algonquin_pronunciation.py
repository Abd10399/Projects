#Author: Mohammad Abdullah
#Student ID: 260980866

import algonquin_utils as au #Shortened to make it easier to call functions from that module.

#Following lines of code are all for defining the required functions.

def get_consonant_pronunciation(str1):
    """(str) -> str
    Checks whether str1 is a valid consonant and returns it's pronunciation
    
    >>> get_consonant_pronunciation('d')
    'D'
    
    >>> get_consonant_pronunciation("J")
    'GE'
    
    >>> get_consonant_pronunciation("z")
    'Z'
    
    """
    str2 = str1.lower() #Converts string to lower case to make checking easier
    if au.is_valid_consonant(str2):
        #Checks whether str2 is included in the list provided
        if str2 in ["b", "c", "d", "g", "h", "k", "m", "n", "p", "s", "t", "w", "y", "z"]:
            return str2.upper()
        elif str2 == "j": #Since j has a different pronunciation compared to its Upper Case letter.
            return "GE"
        
    return ""
    
def get_vowel_pronunciation(str1):
    """(str) -> str
    Checks whether str1 is a valid vowel and returns it's pronunciation
    
    >>> get_vowel_pronunciation("o")
    'U'
    
    >>> get_vowel_pronunciation("r")
    ""
    
    >>> get_vowel_pronunciation("ì")
    'EE'
    
    """
    #Converts string to lower case
    str2 = str1.lower()
    #Sequentially checks for what the vowel's pronunciation is and whether the string itself is valid
    if au.is_valid_vowel(str2):
        if str2 in ["a","à"]:
            return "A"
        elif str2 in ["e","è"]:
            return "E"
        elif str2 == "i":
            return "I"
        elif str2 == "ì":
            return "EE"
        elif str2 == "o":
            return "U"
        elif str2 == "ò":
            return "O"
        
    return "" #Returns Empty string in case no voewl

    
def get_diphthong_pronunciation(str1):
    """(str) -> str
    Checks whether str1 is a valid dipthon and returns it's pronunciation
    
    >>> get_diphthong_pronunciation("ay")
    'EYE'
    
    >>> get_diphthong_pronunciation("ey")
    'AY'
    
    >>> get_diphthong_pronunciation("yo")
    ''
    
    """
    
    str2 = str1.lower() #Converts everything to lowercase to ease checking
    if au.is_valid_diphthong(str1):
        #Sequentially checks for the diphthon's pronunciation and whether the string itself is valid
        if str2 == "aw":
            return "OW"
        elif str2 == "ay":
            return "EYE"
        elif str2 == "ew":
            return "AO"
        elif str2 == "ey":
            return "AY"
        elif str2 == "iw":
            return "EW"
        elif str2 == "ow":
            return "OW"
    else:
        return ""

def get_word_pronunciation(str1):
    """(str) -> str
    Checks whether str1 is a valid single word and then calculates and returns its pronunciation.
    
    >>> get_word_pronunciation("Kwey")
    'KWAY'
    
    >>> get_word_pronunciation("awayewey")
    'OWEYEAOAY'
    
    >>> get_word_pronunciation("awayeweyr")
    ''
    
    """
    
    new_str = "" #Creating a new variable in which we'll save the string
    flag = False #Initialised a boolean variable to help in decision making
    str2 = str1.lower()
    if au.is_valid_single_word(str2): #Checks whether the word is valid
        #Loops through the lenght of str2
        for i in range(len(str2)):
            
            if flag == True: #This is used to skip the iteration where we deal with "dj" or the diphthons
                flag = False
                continue
            
            #Checks first 2 indices whether or not they are comprised to dj (to add it's pronunciation)
            if str2[i:i+2] == "dj":
                new_str += "J"
                flag = True #Checks the flag to skip the next iteration
                
            #Checks first 2 iterations for Diphthons
            elif str2[i:i+2] in ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']:
                new_str += get_diphthong_pronunciation(str2[i:i+2])
                flag = True #Checks the flag to skip the next iteration
                
            #These 2 elif's check whether it is a vowel or a consonant
            elif str2[i] in "aeioàèìò":
                new_str += get_vowel_pronunciation(str2[i])
            elif str2[i] in "bcdghkmnpstwyzj":
                new_str += get_consonant_pronunciation(str2[i])
        
        return new_str #Final string that is repeatedly concatenated gets returned
            
    else:
        return ""
    
    
def tokenize_sentence(str1):
    """(str) -> list
    Converts str1 into a list by seperating the consonants/vowels with the punctuation/spaces and appends it all
    to a list. Also checks whether its a valid phrase or not first
    
    >>> tokenize_sentence("a test")
    ['a', ' ', 'test']
    
    >>> tokenize_sentence("loool")
    []
    
    >>> tokenize_sentence("Mino ishkwa nawakwe")
    ['Mino', ' ', 'ishkwa', ' ', 'nawakwe']
    
    """
    list1 = [] #Creates empty list
    
    #Initialising the variables
    
    new_str = "" #For consonants and vowels
    new_str1 = "" #For punctuation and spaces
    counter = 0
    
    
    if au.is_valid_phrase(str1): #Checking whether the string is a valid phrase or not
        
        #Looping through all characters in str1
        for char in str1:
            
            #Confirms whether the char is a consonant or a vowel
            if au.is_valid_consonant(char) or au.is_valid_vowel(char):
                #Checks whether or not to append the list with the string for the punctuation and spaces
                #This is necessary since we need to check if there is a change from letters to punctuation/spaces
                if len(new_str1) > 0: 
                    list1.append(new_str1)
                    new_str1 = "" #Reinitializes the variable since we'll be making a new string now
                new_str += char
                
            #Confirms whether the char is punctuation mark or space
            if au.is_valid_punctuation(char):
                #Similar process as described above but now for checking the other string (the string with letters)
                if len(new_str) > 0:
                    list1.append(new_str)
                    new_str = ""
                new_str1 += char
                
            #Checks whether the last character has been reached 
            if counter == (len(str1)-1):
                #Checks whether to append the string with letters or punctuations or both
                if len(new_str) > 0:
                    list1.append(new_str)
                if len(new_str1) > 0:
                    list1.append(new_str1)
                
            counter +=1 #Increments the counter (used instead of another for loop)
                
        
    return list1
                
    
def get_sentence_pronunciation(str1):
    """(str) -> str
    Completely Converts str1 (a string) if its valid, into its pronunciation fully.
    
    >>> get_sentence_pronunciation('Andi ejayan?') # Where are you going?
    'ANDI EGEEYEAN?'
    
    >>> get_sentence_pronunciation('boiiii    h t  e')
    'BUIIII    H T  E'
    
    >>> get_sentence_pronunciation('lets go')
    ''
    
    """
    #Initialises a new string
    new_str2 = ""
    
    #Converts the sentence into parts of strings
    list2 = tokenize_sentence(str1)
    if list2 == []:
        return ""
    
    #Loops through a list
    for element in list2:
        if get_word_pronunciation(element) != "":
            #Makes sure that the word has a valid pronunciation which is concatenated with the new string
            new_str2 += get_word_pronunciation(element)
        else:
            #Concatenates the punctuation/spaces to this (which don't need to be altered)
            new_str2 += element
            
    #Returns the final string
    return new_str2
    
#End of Program
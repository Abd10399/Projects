#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing Modules
import similarity_measures as s_m
#Helper Function

def breakdown_with_list(s,l):
    """(str,list) -> list
    Takes a string and a list and returns a list of strings in which there are no characters present which are included in the list

    >>> t = "Hello. My Name is [name]. Testing 123........"
    >>> l = [".","?","!"]
    >>> breakdown_with_list(t,l)
    ['Hello', 'My Name is [name]', 'Testing 123']

    >>> t = "Hello. My Name is [name]. Testing 123"
    >>> l = [".","?","!"]
    >>> breakdown_with_list(t,l)
    ['Hello', 'My Name is [name]', 'Testing 123']

    >>> t = "??????????????..........!!!!!!"
    >>> l = ["?",".","!"]
    >>> breakdown_with_list(t,l)
    []
    """
    #Initializing the list to be returned
    main_list = []
    
    temp_str = ""
    
    #Checking for list characters in the string
    for i in range(len(l)):
        if l[i] in s:
            break
        #Checking if all elements in l have been cross checked
        elif i == (len(l)-1):
            return [s]
        
    #Iterating through the string given
    for char in s:
        
        #Checks if the character is congurent with the list l and adds to the temp string accordingly
        if char not in l:
            temp_str += char
        else:
            #Stripping any unnecessary whitespaces and then appending to main list
            main_list.append(temp_str.strip())
            temp_str = ""
            
    #Checks if any characters are left over in temp_str at the end where the string had no elements from the list
    #if any letters/characters are left, they get appended to the list as well.
    if len(temp_str.strip())>0:
        main_list.append(temp_str.strip())
    
    #Making sure no empty strings end up in the list (in case of elipses)
    #If there are elipses (...) present, it will incur empty strings inside the list
    while "" in main_list:
        main_list.remove("")
        
    #Returning list
    return main_list
    


#Defining the Functions


def get_sentences(s):
    """(str) -> list
    Given a string returns a list of strings each representing one of the sentences from
    the input string.

    >>> text = "No animal must ever kill any other animal. All animals are equal."
    >>> get_sentences(text)
    ['No animal must ever kill any other animal', 'All animals are equal']

    >>> t = "Hello. My Name is [name]. Testing 123"
    >>> get_sentences(t)
    ['Hello', 'My Name is [name]', 'Testing 123']

    >>> t = "Hello. My Name is [name]. Testing 123........"
    >>> get_sentences(t)
    ['Hello', 'My Name is [name]', 'Testing 123']
    """
    
    #Calls the major helper function to help us out
    sentence_list = breakdown_with_list(s,[".","?","!"])
    
    #Returns sentence list
    return sentence_list
    
            
def get_word_breakdown(s):
    """(str) -> list
    Given a string returns a 2D lists of strings. Each sublist contains a string
    representing words from each sentence. Certain punctuation must be removed.

    >>> text = "All the habits of Man are evil. And, above all, no animal must ever tyrannise over his \
    own kind. Weak or strong, clever or simple, we are all brothers. No animal must ever kill \
    any other animal. All animals are equal."
    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> w = get_word_breakdown(text)
    >>> s == w
    True

    >>> t = "Hello. My Name is [name]. Testing, 123"
    >>> get_word_breakdown(t)
    [['hello'], ['my', 'name', 'is', '[name]'], ['testing', '123']]

    >>> t = "Hi, I hope that you're doing pretty well :)"
    >>> get_word_breakdown(t)
    [['hi', 'i', 'hope', 'that', 'you', 're', 'doing', 'pretty', 'well', ')']]
    """
    #Initializing word list & punctuation list (with whitespace included)
    word_list = []
    punctuation_list = [',', '-', '--', ':', ';', '"', "'", " ", '\n', '\t']
    
    #Since we need only lowercase, we convert s into lowercase
    new_str = s.lower()
    
    #Converts the string into sentences and assigns it to new_list
    new_list = get_sentences(new_str)
    
    #Iterates through new_list which contains sectences as each element of the list and appends to word_list
    for element in new_list:
        
        word_list.append(breakdown_with_list(element,punctuation_list))
        
    return word_list

def build_semantic_descriptors_from_files(l):
    """(list) -> dict
    Given a list of file names (strings) as input returns a
    dictionary of the semantic descriptors of all the words in the files received as input, with the files
    treated as a single text.

    >>> d = build_semantic_descriptors_from_files(['animal_farm.txt'])
    >>> d['animal']['must']
    3
    >>> d['evil'] == {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True

    >>> d = build_semantic_descriptors_from_files(['test.txt'])
    >>> d["draw"]["genuine"]
    4

    >>> d = build_semantic_descriptors_from_files(['test.txt'])
    >>> d["draw"]["rock"] == d["draw"]["examine"]
    True
    """
    #Initializing main string where the words will be stored
    f_content = ""
    #Iterating through the list "l" provided 
    for element in l:
        #Creating file object
        f_object = open(element, "r", encoding="utf-8")
        
        #Reading file content and storing it in a variable (its a string)
        f_content += f_object.read()
        
        #Closing file
        f_object.close()
    
            
    #Calls get_all_semantic_descriptors on a nested list of words & sentences made through calling the functions above
    main_dict = s_m.get_all_semantic_descriptors(get_word_breakdown(f_content))
    
    #Returns the variable
    return main_dict
    
#End of Module
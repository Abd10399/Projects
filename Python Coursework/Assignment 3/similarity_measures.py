#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing Modules
import vectors_utils

#Defining the Functions


def get_semantic_descriptor(w,s):
    """(str,list) -> dict
    Given a string w representing a single word and a list s representing all
    the words in a sentence, returns a dictionary representing the semantic descriptor vector of the
    word w computed from the sentence s.

    >>> s1 = ['all', 'the', 'habits', 'of', 'man', 'are', 'evil']
    >>> s2 = ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal']
    >>> desc1 = get_semantic_descriptor('evil', s1)
    >>> desc1['all']
    1
    >>> len(desc1)
    6
    >>> 'animal' in desc1
    False

    >>> s2 = ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal']
    >>> desc1 = get_semantic_descriptor('kill', s2)
    >>> desc1
    {'no': 1, 'animal': 2, 'must': 1, 'ever': 1, 'any': 1, 'other': 1}

    >>> s2 = ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal', 'before','before', "before"]
    >>> desc1 = get_semantic_descriptor('kill', s2)
    >>> desc1
    {'no': 1, 'animal': 2, 'must': 1, 'ever': 1, 'any': 1, 'other': 1, 'before': 3}
    """
    
    #Initializing the dictionary
    my_dict = {}
    
    #Checks if the word is in the list or not, returns an empty dictionary otherwise
    if w not in s:
        return my_dict
    
    #Loops through the sentence list
    for element in s:
        #Makes sure that the word w is not included
        if element != w:
            
            #Adds key-value pair and increments the value appropriately
            if element not in my_dict:
                my_dict[element] = 1
            else:
                my_dict[element] += 1
            
    #Returning dictionary
    return my_dict
        
def get_all_semantic_descriptors(list1):
    """(list) -> dict
    Takes input a 2D list representing words in a text. The function returns a dictionary "my_dict"
    such that for every word "w" that appears in at least one of the sentences, "my_dict[w]" is itself a dictionary
    which represents the semantic descriptor vector of w.

    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d['animal']['must']
    3
    >>> d['evil'] == {'all': 1, 'the': 1, 'habits': 1, 'of': 1, 'man': 1, 'are': 1}
    True

    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d["animal"]
    {'and': 1, 'above': 1, 'all': 1, 'no': 3, 'must': 3, 'ever': 3, \
    'tyrannise': 1, 'over': 1, 'his': 1, 'own': 1, 'kind': 1, 'kill': 2, 'any': 2, 'other': 2}

    >>> s = [['all', 'the', 'habits', 'of', 'man', 'are', 'evil'], \
    ['and', 'above', 'all', 'no', 'animal', 'must', 'ever', 'tyrannise', 'over', 'his', 'own', 'kind'], \
    ['weak', 'or', 'strong', 'clever', 'or', 'simple', 'we', 'are', 'all', 'brothers'], \
    ['no', 'animal', 'must', 'ever', 'kill', 'any', 'other', 'animal'], \
    ['all', 'animals', 'are', 'equal']]
    >>> d = get_all_semantic_descriptors(s)
    >>> d["brothers"]
    {'weak': 1, 'or': 2, 'strong': 1, 'clever': 1, 'simple': 1, 'we': 1, 'are': 1, 'all': 1}
    """
    
    #Initializing dictionary to be returned
    my_dict = {}
    
    #Iterating through rows
    for row in list1:
        
        #Iterating through each sublist
        for col in row:
            
            #Making sure that the key doesn't exist (otherwise it would be overwritten)
            if col not in my_dict:
                #Adding the key-value pair to my_dict by using get_semantic_descriptor function
                my_dict[col] = get_semantic_descriptor(col,row)
                
            else:
                #Adding the 2 semantic descriptor dictionaries together. This changes my_dict[col]
                vectors_utils.add_vectors(my_dict[col],get_semantic_descriptor(col,row))
    
    return my_dict

                
def get_cos_sim(d1,d2):
    """(dict,dict) -> num
    Given two dictionaries representing similarity descriptor vectors, returns the cosine
    similarity between the two.

    >>> round(get_cos_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    0.7

    >>> v1 = {'a' : 11, 'b' : 11, 'c' : 11}
    >>> v2 = {'a' : 12, 'c' : 614}
    >>> get_cos_sim(v1,v2)
    >>> round(get_cos_sim(v1,v2),2)
    0.59

    >>> get_cos_sim({"a":1},{"b":1})
    0.0
    """
    
    #Setting up variables
    
    dot_prod = vectors_utils.get_dot_product(d1,d2)
    
    norm1 = vectors_utils.get_vector_norm(d1)
    norm2 = vectors_utils.get_vector_norm(d2)
    
    #Returning after putting the variables in the formula
    return dot_prod/(norm1*norm2)

def get_euc_sim(d1,d2):
    """(dict,dict) -> num
    Returns the similarity between the two dictionaries using the negative euclidean distance.

    >>> round(get_euc_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    -6.71

    >>> round(get_euc_sim({"a":1},{"b":1}),3)
    -1.414

    >>> v1 = {'a' : 11, 'b' : 11, 'c' : 11}
    >>> v2 = {'a' : 12, 'c' : 614}
    >>> round(get_euc_sim(v1,v2),3)
    -603.101
    """
    
    #Subtracting the 2 vectors and putting the result into a variable
    new_vector = vectors_utils.sub_vectors(d1,d2)
    
    #Calculating norm of the new_vector and multiplying it by -1
    negative_euc_distance = -1 * vectors_utils.get_vector_norm(new_vector)
    
    #Returning answer
    return negative_euc_distance

def get_norm_euc_sim(d1,d2):
    """(dict,dict) -> num
    Returns the similarity between the two dictionaries using the negative euclidean distance of their normalized vectors.

    >>> round(get_norm_euc_sim({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 2)
    -0.77

    >>> round(get_norm_euc_sim({"a":1},{"b":1}),3)
    -1.414

    >>> round(get_norm_euc_sim(v1,v2),2)
    -0.91
    """
    
    #Converting the given dictionaries into a normal form after deep copying them
    new_d1 = {}
    new_d2 = {}
    
    for k in d1:
        new_d1[k] = d1[k]
    for k in d2:
        new_d2[k] = d2[k]
        
    #Normalizing new dictionaries
    vectors_utils.normalize_vector(new_d1)
    vectors_utils.normalize_vector(new_d2)
    
    #Returning the negative euclidean distance b/w the 2 new normalized vectors
    return get_euc_sim(new_d1,new_d2)


#End of Module
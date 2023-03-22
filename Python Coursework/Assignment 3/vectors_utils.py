#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing Math Module
import math
#Defining The functions

def add_vectors(d1,d2):
    """(dict,dict) -> None
    Given two dictionaries representing vectors, it adds the second vector to the first one.

    >>> v1 = {'a' : 1, 'b' : 3}
    >>> v2 = {'a' : 1, 'c' : 1}
    >>> add_vectors(v1, v2)
    >>> len(v1)
    3
    >>> v1['a']
    2
    >>> v1 == {'a' : 2, 'b' : 3, 'c' : 1}
    True

    >>> v1 = {'a' : 11, 'b' : 36}
    >>> v2 = {'a' : 12, 'c' : 14}
    >>> add_vectors(v1,v2)
    >>> v1
    {'a': 23, 'b': 36, 'c': 14}

    >>> v1 = {'a' : 11, 'b' : 36, 'c' : 614}
    >>> v2 = {'a' : 12, 'c' : 14}
    >>> add_vectors(v1,v2)
    >>> v1
    {'a': 23, 'b': 36, 'c': 628}

    """
    
    #Loops through second dictionary
    for k in d2:
        #Checks if they key already exists, if exists, adds values, otherwise creates an entry in the dictionary with value d2[k]
        if k in d1:
            d1[k] += d2[k]
        else:
            d1[k] = d2[k]
            
def sub_vectors(d1,d2):
    """(dict,dict) -> dict
    Given two dictionaries representing vectors, it returns a dictionary which is the result
    of subtracting the second vector from the first one.

    >>> d1 = {'a' : 3, 'b': 2}
    >>> d2 = {'a': 2, 'c': 1, 'b': 2}
    >>> d = sub_vectors(d1, d2)
    >>> d == {'a': 1, 'c' : -1}
    True

    >>> v1 = {'a' : 11, 'b' : 36, 'c' : 614}
    >>> v2 = {'a' : 12, 'c' : 14}
    >>> sub_vectors(v1,v2)
    {'a': -1, 'b': 36, 'c': 600}

    >>> v1 = {'a' : 11, 'b' : 36, 'c' : 614}
    >>> v2 = {'a' : 12, 'c' : 614}
    >>> sub_vectors(v1,v2)
    {'a': -1, 'b': 36}
    """
    
    #Creating an empty dictionary
    d_new = {}
    
    #Looping through the first dictionary and copying (keys & values) to d_new
    for k in d1:
        d_new[k] = d1[k]
        
    
    #Looping through second dictionary and subtracting from new_d
    for k in d2:
        #Checks if k is in d_new
        if k in d_new:
            #Subtracts the value of d2 which has key k from the key k in d_new
            d_new[k] -= d2[k]
            
            #Checks if subtraction yeiled 0, if yes it removes the key-value pair from the dictionary
            if d_new[k] == 0:
                del d_new[k]
        else:
            #If no item exists in d_new with key k, the value of -1*d2[k] is added to d_new (negative value)
            d_new[k] = -1*d2[k]
    
    return d_new
                
def merge_dicts_of_vectors(d1,d2):
    """(dict,dict) -> None
    The function modifies the first input by merging it with the second one.
    
    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d2 = {'p' : {'papaya' : 6}}
    >>> merge_dicts_of_vectors(d1, d2)
    >>> len(d1)
    2
    >>> len(d1['p'])
    3
    >>> d1['a'] == {'apple': 2}
    True

    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d2 = {'p' : {'papaya' : 6, 'peach' :10, 'strawberry' : 1}}
    >>> merge_dicts_of_vectors(d1,d2)
    >>> d1
    {'a': {'apple': 2}, 'p': {'pear': 1, 'plum': 3, 'papaya': 6, 'peach': 10, 'strawberry': 1}}

    >>> d1 = {'a' : {'apple': 2}, 'p' : {'pear': 1, 'plum': 3}}
    >>> d2 = {'p' : {'papaya' : 6, 'peach' :10, 'strawberry' : 1, 'grapes':9999}}
    >>> merge_dicts_of_vectors(d1,d2)
    >>> d1["p"]["grapes"]
    9999
    """
    
    #Looping through d2
    for k in d2:
        #Checks if k is in d1
        if k in d1:
            #Adds the values(inner dictionaries) together 
            add_vectors(d1[k],d2[k])
            
        else:
            #Adds the key-value pair to d1 if they dont have congurent keys
            d1[k] = d2[k]
            
def get_dot_product(d1,d2):
    """(dict,dict) -> num
    Given two dictionaries representing vectors, returns the dot product of the two
    vectors.

    >>> v1 = {'a' : 3, 'b': 2}
    >>> v2 = {'a': 2, 'c': 1, 'b': 2}
    >>> get_dot_product(v1, v2)
    10

    >>> v1 = {'a' : 11, 'b' : 36, 'c' : 614}
    >>> v2 = {'a' : 12, 'c' : 614}
    >>> get_dot_product(v1,v2)
    377128

    >>> v1 = {'a' : 11, 'b' : 36, 'c' : 0}
    >>> v2 = {'a' : 12, 'c' : 614}
    >>> get_dot_product(v1,v2)
    132
    """
    
    #Initializing variable to be returned
    dot_product = 0
    
    #Loops through d1 and checks if k(key) is in d2
    for k in d1:
        if k in d2:
            dot_product += d1[k]*d2[k]
    #Returns the dot product            
    return dot_product

def get_vector_norm(d1):
    """(dict) -> num
    Given a dictionary representing a vector, returns the norm of such vector.

    >>> v1 = {'a' : 3, 'b': 4}
    >>> get_vector_norm(v1)
    5.0

    >>> v1 = {'a' : 11, 'b' : 36, 'c' : 614}
    >>> round(get_vector_norm(v1),3)
    615.153

    >>> v1 = {'a' : 11, 'b' : 11, 'c' : 11}
    >>> round(get_vector_norm(v1),2)
    19.05
    """
    #Initializing variable to return
    norm = 0
    
    sum1 = 0
    
    #Looping through d1 and adding the squares of its entries
    for k in d1:
        sum1 += (d1[k])**2
    
    #Takes square root of the sum1
    norm = math.sqrt(sum1)
    
    return norm

def normalize_vector(d1):
    """(dict) -> None
    The function modifies the dictionary by dividing each value by the norm of the vector.

    v1 = {'a' : 3, 'b': 4}
    >>> normalize_vector(v1)
    >>> v1['a']
    0.6

    >>> v1 = {'a' : 11, 'b' : 11, 'c' : 11}
    >>> normalize_vector(v1)
    >>> round(v1['a'],3)
    0.577

    >>> v1 = {'a' : 11, 'b' : 36, 'c' : 614}
    >>> normalize_vector(v1)
    >>> round(v1['c'],3)
    0.998
    """
    #Makes sure that vector d1's norm isn't 0 so to not raise ZeroDivisionError
    norm1 = get_vector_norm(d1)
    if norm1 != 0:
        
        #Loops through d1
        for k in d1:
            #Multiplying each value by the inverse of its norm
            d1[k] /= norm1
        
        
#End of Module        
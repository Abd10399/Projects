#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing Modules
from similarity_measures import *
from file_processing import *
import matplotlib.pyplot as plt
#Defining Functions

def most_sim_word(str_w,choices,semantic_descriptors,similarity_fn):
    """(str,list,dict,function) -> str
    The function returns the element of choices which has the largest semantic similarity to word, with
    the semantic similarity computed using the data in semantic_descriptors and the similarity function similarity_fn.

    >>> choices = ['dog', 'cat', 'horse']
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
    >>> most_sim_word('feline', choices, sem_descs, get_cos_sim)
    'cat'

    >>> choices = ['dog', 'cat', 'horse']
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h}
    >>> most_sim_word('goat', choices, sem_descs, get_cos_sim)
    ''

    >>> choices = ['dog', 'cat', 'horse',"goat"]
    >>> c = {'furry' : 3, 'grumpy' : 5, 'nimble' : 4}
    >>> f = {'furry' : 2, 'nimble' : 5}
    >>> d = {'furry' : 3, 'bark' : 5, 'loyal' : 8}
    >>> h = {'race' : 4, 'queen' : 2}
    >>> a = {'furry': 10, 'king': 3,'nimble' : 10}
    >>> sem_descs = {'cat' : c, 'feline' : f, 'dog' : d, 'horse' : h, 'animal' : a}
    >>> most_sim_word('animal', choices, sem_descs, get_cos_sim)
    'cat'

    """
    
    #Checking if the word is not an empty string
    if str_w == "":
        return ""
    #Initializing a temp list to keep track of the numerical values
    temp_list = [] #Its elements have same order as the choices
    
    #Since if the semantic descriptor of the word itself doesn't exist then we can't compare anything
    try:
        temp_var = semantic_descriptors[str_w] #Increasing efficiency (outside the for loop)
    except KeyError:
        return ""
    
    for i in range(len(choices)):
        try:
            #Appends the calculated value to a temporary list
            temp_list.append(similarity_fn(temp_var,semantic_descriptors[choices[i]]))
            
        #If keys can't be compared due to no key being present
        except KeyError:
            temp_list.append(float("-inf"))
    
    #This checks whether all possible values are un-computable
            
    if max(temp_list) == float("-inf"):
        return ""
    #Max function returns the maximum value at the least index which is then converted back to string through slicing choices list
    return choices[temp_list.index(max(temp_list))]

def run_sim_test(filename,semantic_descriptors,similarity_fn):
    """(str,dict,function) -> float
    The function returns the percentage of questions on which most_sim_word guesses the answer correctly using the semantic
    descriptors stored in semantic_descriptors, and the similarity function similarity_fn.
    
    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_cos_sim)
    15.0
    
    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_euc_sim)
    20.0

    >>> descriptors = build_semantic_descriptors_from_files(['test.txt'])
    >>> run_sim_test('test.txt', descriptors, get_norm_euc_sim)
    15.0
    """
    #Initializing some variables that will be used later
    answer_test = ""
    word_test = ""
    #Initializing the return variable
    sum_1 = 0
    t_counter = 0
    
    f_object = open(filename, "r", encoding="utf-8")
    
    #Iterates through each line in the filename
    for line in f_object:
        
        #Since we get a nested list from get_word_breakdown, we take the first(only) sublist of the sentence which has all the words
        #Keep reassigning it to temp list at each iteration of the loop
        temp_list = get_word_breakdown(line)[0]
        
        #Assigns value of the word to word_test variable
        word_test = temp_list[0]
        
        #Assigns value of the answer to answer_test variable
        answer_test = temp_list[1]
        
        #Checks if most_sim_word gives the correct answer or not
        if most_sim_word(word_test,temp_list[2:],semantic_descriptors,similarity_fn) == answer_test:
            sum_1 +=1 #Increments success
            
        t_counter +=1 #Increments regardless of sucess
        
    f_object.close()
    
    #Returning the percentage
    
    return (sum_1/t_counter)*100
    
    
def generate_bar_graph(list_functions,filename):
    """(list,str) -> None
    Generates a bar graph where the performance of each function on the given file (filename) is plotted.
    """
    #Building Semantic Descriptors library from the 2 books
    desc_dict = build_semantic_descriptors_from_files(['war_and_peace.txt', 'swanns_way.txt'])
    
    #Initializing lists
    y_axis = []
    x_axis = []
    
    #Calling the functions by the number of times corresponding to the number of functions provided
    for i in range(len(list_functions)):
        y_axis.append(run_sim_test(filename,desc_dict,list_functions[i]))
        x_axis.append(list_functions[i].__name__)
    
    
    #Making the Bar Graph
    plt.bar(x_axis,y_axis)
    
    #Saving the picture
    plt.savefig("synonyms_test_results.png")
    
    #Showing the bar graph
    plt.show()
#End of Module
    
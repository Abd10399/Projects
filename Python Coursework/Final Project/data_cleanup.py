#Author: Mohammad Abdullah
#Student ID: 260980866

#Helper Functions
def fix_list(list1):
    """(list) -> list
    Takes a list as input,modifies it, and returns it so that it satisfies the conditions stipulated (5 columns)
    (1 column per element of list)
    
    >>> fix_list(["a","bcdd","asvdfdgd","asrffgg", "214215", "21542", "6485", "12451253"])
    ['a', 'bcdd asvdfdgd asrffgg', '214215', '21542.6485', '12451253']
    
    >>> fix_list(["a","bell","asrffgg", "214215", "6485", "12451253"])
    ['a', 'bell asrffgg', '214215', '6485', '12451253']

    >>> fix_list(["a","bell","asrffgg", "214215", "6485,455555", "12451253"])
    ['a', 'bell asrffgg', '214215', '6485.455555', '12451253']
    """
    #For the first 2 columns    
    #Looping indefinately until broken
    while True:
        try:
            #Checks if the element at the 2nd index can be converted into a number without error
            #If possible, then the first 2 columns are good to go
            int(list1[2])
            break
        except ValueError:
            #Concatenates the list's 2nd element with the 3rd one and deletes the third element
            list1[1] = list1[1] + " " + list1[2]
            list1.pop(2)
    
    #Checks if only the first 2 columns were erroneous
    if len(list1) == 5:
        list1[3] = list1[3].replace(",",".")
        #Returns list1
        return list1
    
    #Joining the 3rd and 4th columns (same algorithm as for the above)
    #This needs to be done only once since there can be only 1 decimal point
    list1[3] = list1[3] + "." + list1[4] #Joining through the decimal point
    list1.pop(4)
    
    return list1
    



#Defining the functions
def find_delim(line1):
    """(str) -> str
    The function returns the most commonly used delimiter in the input string.
    
    >>> find_delim("0 1 2 3,4")
    ' '
    >>> find_delim("a,b-2,c,6,d")
    ','
        
    >>> find_delim("a-b-2,c-6,d")
    '-' 
    
    """
    #Temporary Variables
    temp_count = 0
    temp_key = ""
    temp_bool = True
    #Defining a dictionary of the delimiters
    delimiter_dict = {"\t" : 0, " ": 0, "," : 0, "-" : 0}
    
    #Iterating through the input string
    for char in line1:
        if char in delimiter_dict:
            #Increments the number times a delimiter 
            delimiter_dict[char] +=1
            #Temp bool will be used to check whether or not to raise an assertion error
            temp_bool = False
    #Checks for the most common delimiter
    for k in delimiter_dict:
        if delimiter_dict[k] > temp_count:
            #Reassigns the variables as appropriate
            temp_key = k
            temp_count = delimiter_dict[k]
            
    if temp_bool:
        raise AssertionError("The is no tab, comma, space or dash in the string")
    else:
        #Returns the most common key
        return temp_key
    
    
def clean_one(input_filename, output_filename):
    """(str, str) -> int
    The function will read the input_filename, make changes to each of the lines and write the new
    version to output_filename.
    
    >>> clean_one('small_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    10

    >>> clean_one('large_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    17452

    >>> c1 = clean_one('small_raw_co2_data.txt', 'small_tab_sep_co2_data.tsv')
    >>> c2 = clean_one('large_raw_co2_data.txt', 'large_tab_sep_co2_data.tsv')
    >>> round((c2/c1),1)
    1745.2

    """
    #Counter
    counter = 0
    
    #Opening files to be read/written to
    r_object = open(input_filename, "r", encoding="utf-8")
    w_object = open(output_filename, "w", encoding ="utf-8")
    
    #Iterating through the lines
    for line in r_object:
        #Finds the most used delimiter (since comma may be used instead of a period)
        delim = find_delim(line)
        
        #Assigns to temp_list
        temp_list = line.split(delim)
        #Joins the iterables with a tab
        new_str = "\t".join(temp_list)
        
        #Writes to the output file
        w_object.write(new_str)
        
        #Increments the counter
        counter +=1
    
    #Closing the files
    w_object.close()
    r_object.close()
    
    #Returns the counter
    return counter
    
    
    
def final_clean(input_filename, output_filename):
    """(str, str) -> int
    The function will read the input_filename, make changes to each of the lines and write the new
    version to output_filename, whilst satisfying the given conditions.
    
    >>> final_clean('small_tab_sep_co2_data.tsv', 'small_clean_co2_data.tsv')
    10

    >>> final_clean('large_tab_sep_co2_data.tsv', 'small_clean_co2_data.tsv')
    17452

    >>> c1 = final_clean('small_tab_sep_co2_data.tsv', 'small_clean_co2_data.tsv')
    >>> c2 = final_clean('large_tab_sep_co2_data.tsv', 'large_clean_co2_data.tsv')
    >>> round(c2/c1,1)
    1745.2

    """
    
    #Counter
    counter = 0
    
    #Opening files to be read/written to
    r_object = open(input_filename, "r", encoding="utf-8")
    w_object = open(output_filename, "w", encoding ="utf-8")
    
    
    #Iterating through each line
    for line in r_object:
        
        #Setting up a temp variable
        temp_list = []
        
        #Splitting all the tabs and making a subsequent list
        temp_list = line.split("\t")
        
        #Checking the lenght of the list
        if len(temp_list) == 5:
            #Writes line whilst replacing all commas with dots
            w_object.write(line.replace(",","."))
            counter += 1
            #Goes to the next iteration
            continue
        
        #Calling a helper function to correct the list, and hence get the columns rectified
        new_list = fix_list(temp_list)
        
        #Joins the entries in new_list with a tab and writes to the output file
        new_str = "\t".join(new_list)
        w_object.write(new_str.replace(",","."))
        counter +=1
            
    #Closing the files
    w_object.close()
    r_object.close()
    
    return counter
    
#End of Code
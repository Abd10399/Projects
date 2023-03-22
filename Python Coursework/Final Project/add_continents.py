#Author: Mohammad Abdullah
#Student ID: 260980866

#Defining the functions

def get_iso_codes_by_continent(file_str):
    """(str) -> dict
    The function returns a dictionary mapping continents’ names (all upper case) to a list
    of ISO codes (strings) of countries that belongs to that continent.
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> len(d['ASIA'])
    50
    
    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> d["OCEANIA"]
    ['NRU', 'VUT', 'NZL', 'TON', 'KIR', 'WSM', 'PLW', 'TUV', 'NIU', 'PNG', 'SLB', 'FJI', 'AUS', 'MHL']

    >>> d = get_iso_codes_by_continent("iso_codes_by_continent.tsv")
    >>> d["SOUTH AMERICA"]
    ['URY', 'COL', 'BRA', 'GUY', 'ECU', 'VEN', 'PER', 'ARG', 'BOL', 'PRY', 'SUR', 'CHL']
    
    
    """
    #Empty Dictionary
    my_dict = {}
    #Opening the file
    r_object = open(file_str, "r", encoding="utf-8")
    
    #Iterating through the lines of the file
    for line in r_object:
        
        #Makes sure no trailing whitespacing are present
        line = line.strip()
        #Converting elements of each line into elements of a list
        list1 = line.split("\t")
        
        if list1[1].upper() in my_dict:
            #Appends the new iso to the list which is mapped by the respective continent
            my_dict[list1[1].upper()].append(list1[0])
        
        else:
            #Creates a key value pair if the key DNE
            my_dict[list1[1].upper()] = [list1[0]]
            
    #closing the file
    r_object.close()
    
    return my_dict

def add_continents_to_data(input_filename, continents_filename, output_filename):
    """(str,str,str) -> int
    The function will read the input_filename, make changes to each of the
    lines and write the new version to output_filename.
    
    >>> add_continents_to_data("small_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "small_co2_data.tsv")
    10

    >>> num = add_continents_to_data("large_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "small_co2_data.tsv")
    >>> num/17452
    1.0

    >>> c1 = add_continents_to_data("small_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "small_co2_data.tsv")
    >>> c2 = add_continents_to_data("large_clean_co2_data.tsv", "iso_codes_by_continent.tsv",
    "large_co2_data.tsv")
    >>> round(c2/c1,1)
    1745.2
    
    """
    #Counter
    counter = 0
    
    #Opening Files
    r_object = open(input_filename, "r", encoding="utf-8")
    w_object = open(output_filename, "w", encoding="utf-8")
    
    #Getting the dictionary from the continents_filename
    main_dict = get_iso_codes_by_continent(continents_filename)
    
    #Iterating through the input file line by line
    for line in r_object:
        
        #Temp Variables
        new_str = ""
        temp_list = []
        final_str = ""
        
        #Seperating elements of a line into a list
        temp_list = line.split("\t")
        
        #Checking the dictionary for the Continent of the country
        for k in main_dict:
            if (temp_list[0] in main_dict[k]) and len(new_str) == 0:
                new_str = k #Adding the continent name to the new_str
            
            elif temp_list[0] in main_dict[k]:
                new_str = new_str + "," + k #Incase there is another continent to which the country belongs
        
        #Changing the list as appropriate
        temp_list.insert(2, new_str)
        
        #Converting list back to a string to write to the file
        final_str = "\t".join(temp_list)
        w_object.write(final_str)
        counter += 1
        
    
    
    #Closing Files
    w_object.close()
    r_object.close()
    
    return counter
    
#End of Code
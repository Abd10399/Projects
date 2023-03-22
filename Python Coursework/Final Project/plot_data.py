#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing Modules
import matplotlib.pyplot as plt
from build_countries import *
import doctest


#Defining the functions

def get_bar_co2_pc_by_continent(main_dict, year_num):
    """(dict, int) -> list
    The function should create a bar plot representing the co2 emissions per capita (in tonnes) produced by all the countries
    in each continent. The bars should appear in alphabetical order, and this should return alist of the values being plotted.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_co2_pc_by_continent(d1, 2001)
    [0.20320332558992543, 67.01626016260163, 7.6609004739336495, 1.4196063588190764]

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d2, 2000)
    >>> round(data[1],3)
    2.698

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_by_continent(d2, 2000)
    >>> round(data[5],5)
    2.31592

    """
    
    #main dict has keys ISO and values as the country with the subsequent iso values
    
    #Some temporary variables
    x_list = []
    y_list = []
    nested_list = []
    temp_dict = {}
    
    country_list = []
    
    #We need a list of countries in the same continent
    #Iterating through the main dictionary
    for k in main_dict:
        #Appends the country object to a country list
        country_list.append(main_dict[k])
        
    
    #Using static method to return a dictionary mapping continents to a list of countries
    temp_dict = Country.get_countries_by_continent(country_list)
    
    #Calculating the data for a specific year
    for k in temp_dict:
        #Appends to the nested_list the continent and the total co2 emissions per capitia for the list of countries
        nested_list.append([k,Country.get_total_co2_emissions_per_capita_by_year(temp_dict[k], year_num)])
        #We have a nested list, in which first element of the inner list is the continent, while the second element is the per capitia co2
    
    #Sorting the list (alphabetically)
    nested_list.sort()
    
    #Assignings the values to the x and y lists
    for element in nested_list:
        x_list.append(element[0])
        y_list.append(element[1])
        
        
    
    #Plotting the bar graph
    plt.bar(x_list,y_list)
    #Making the title:
    plt.title("CO2 emissions per capita in " + str(year_num) + " by mohammad.abdullah@mail.mcgill.ca")
    #Labelling the axis
    plt.ylabel("co2 (in tonnes)")
    
    #Saving the File
    plt.savefig("co2_pc_by_continent_" + str(year_num) + ".png")
    
    plt.show()
    #Returning the values plotted
    return y_list
    
    
    
    
def get_bar_historical_co2_by_continent(main_dict, year_num):
    """(dict, int) -> list
    The function should create a bar plot representing the historical co2 emissions (in millions of tonnes) produced by
    all the countries in each continent
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_historical_co2_by_continent(d1, 2015)
    [4.877, 207.54500000000002, 359.367, 149.34300000000002]

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 2005)
    >>> round(data[3],4)
    374249.423

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_historical_co2_by_continent(d2, 2010)
    >>> round(data[0],3)
    34142.48

    """
    
    #Temporary Variables
    x_list = []
    y_list = []
    
    nested_list = []
    temp_dict = {}
    
    country_list = []
    
    #Creating the country list
    for k in main_dict:
        country_list.append(main_dict[k])
    
    #Using static method to return a dictionary mapping continents to a list of countries
    temp_dict = Country.get_countries_by_continent(country_list)
    
    #Calculating historical co2 per continent
    for k in temp_dict:
        nested_list.append([k,Country.get_total_historical_co2_emissions(temp_dict[k], year_num)])
        
    #Sorting the continents alphabetically
    nested_list.sort()
    
    #Assignings the values to the x and y lists
    for element in nested_list:
        x_list.append(element[0])
        y_list.append(element[1])
    
    
    
    
    #Plotting the bar graph
    plt.bar(x_list,y_list)
    #Making the title:
    plt.title("Historical CO2 emissions up to " + str(year_num) + " by mohammad.abdullah@mail.mcgill.ca")
    #Labelling the axis
    plt.ylabel("co2 (in millions of tonnes)")
    
    #Saving the File
    plt.savefig("hist_co2_by_continent_" + str(year_num) + ".png")
    
    plt.show()
    #Returning the values plotted
    return y_list
    
    
    
def get_bar_co2_pc_top_ten(main_dict, year_num):
    """(dict, int) -> list
    The function should create a bar plot representing the co2 emissions per capita (in tonnes) produced by the top 10
    producing countries in the dictionary. If less than 10 countries present, graph all of them
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d1, 2001)
    >>> len(data)
    5

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d2, 2000)
    >>> data[1]
    35.669432035737074

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_co2_pc_top_ten(d2, 2001)
    >>> data[3]
    20.95909090909091

    """
    
    #Temporary Variables
    x_list = []
    y_list = []
    country_list = []
    final_list = []
    
    temp_dict = {}
    
    #Creating a dictionary to pass to get_top_n
    
    #Creating country list
    for k in main_dict:
        #Excluding any countries which cant compute the per capita co2
        if main_dict[k].get_co2_per_capita_by_year(year_num) == None:
            continue #Goes to the next iteration
        country_list.append(main_dict[k])
    
    #Assigning temp_dict to this dictionary
    temp_dict = Country.get_co2_emissions_per_capita_by_year(country_list, year_num)
    
    #Passing temp_dict to get_top_n
    
    final_list = Country.get_top_n(temp_dict, 10)
    
    #Final list will contain tuples in the form of (iso_code, co2 per capita)
    
    for iso, co2 in final_list:
        #Assigning stuff to their values
        x_list.append(iso)
        y_list.append(co2)
    

    #Plotting the bar graph
    plt.bar(x_list,y_list)
    #Making the title:
    plt.title("Top 10 countries for CO2 emissions pc in " + str(year_num) + " by mohammad.abdullah@mail.mcgill.ca")
    #Labelling the axis
    plt.ylabel("co2 (in tonnes)")
    
    #Saving the File
    plt.savefig("top_10_co2_pc_" + str(year_num) + ".png")
    
    plt.show()
    #Returning the values plotted
    return y_list




def get_bar_top_ten_historical_co2(main_dict, year_num):
    """(dict, int) -> list
    The function should create a bar plot representing the historical co2 emissions (in millions of tonnes) produced by the
    top 10 producing countries in the dictionary. If less than 10 countries present, graph all of them

    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> get_bar_top_ten_historical_co2(d1, 2015) == [306.696, 166.33, 149.34300000000002, 48.923, 41.215, 3.748, 3.324, 1.553, 0.0]
    True

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_top_ten_historical_co2(d2, 2000)
    >>> data[0]
    301943.7180000001

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_bar_top_ten_historical_co2(d2, 1999)
    >>> data[1]
    75319.74099999998

    """
    #Temporary Variables
    x_list = []
    y_list = []
    country_list = []
    final_list = []
    
    temp_dict = {}
    
    #Creating a country list
    for key in main_dict:
        #Appends the country object to the country list
        country_list.append(main_dict[key])
        
    #Assigning values to a dictionary for further processing
    
    temp_dict = Country.get_historical_co2_emissions(country_list, year_num)
    #Keys are country objects and values are the historical co2 emissions of the country itself
    
    #Calling this on the get_top_n method to get a final list of tuples which will be unpacked into x and y coordinates
    final_list = Country.get_top_n(temp_dict, 10)
    
    for iso, co2 in final_list:
        #Assigning stuff to their values
        x_list.append(iso)
        y_list.append(co2)
    
    
    #Plotting the bar graph
    plt.bar(x_list,y_list)
    #Making the title:
    plt.title("‘Top 10 countries for historical CO2 up to " + str(year_num) + " by mohammad.abdullah@mail.mcgill.ca")
    #Labelling the axis
    plt.ylabel("co2 (in millions of tonnes)")
    
    #Saving the File
    plt.savefig("top_10_hist_co2_" + str(year_num) + ".png")
    
    plt.show()
    #Returning the values plotted
    return y_list
    
    
    
def get_plot_co2_emissions(main_dict, iso_list, min_year, max_year):
    """(dict, list, int, int) -> list
    The function should plot the co2 emissions of the selected countries (those whose
    ISO code appears in the input list) from min_year to max_year.
    
    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1800, 2000)
    >>> len(data[0]) # USA
    201

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1800, 2000)
    >>> data[3][190]
    1052.52

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> data = get_plot_co2_emissions(d2, ["USA", "CHN", "RUS", "DEU", "GBR"], 1800, 2000)
    >>> data[0][0]
    0.253

    """
    #iso_list has lenght <=5
    #list of styles
    style_list = ["o--g",".-b","o:r",".--c","o-m"] #5 elements (no more needed)
    
    #Temporary Variables
    x_list = []
    y_list = []
    final_list = []
    
    step_num = int((max_year - min_year) / 10)
    
    #Creating the 2D LIST
    
    
    #Iterating through the iso's
    for element in iso_list:
        inner_list = [] #Innerlist that will be appended to the final list later
        for i in range(min_year,max_year+1): #Looping through all years
            try: #Preventing any unforseen errors from occuring (unintentional)
                #Making sure that the year for co2 emissions is recorded
                if i not in main_dict[element].co2_emissions:
                    inner_list.append(0.0) #Appending 0 incase no data exists for that year
                else:
                    inner_list.append(main_dict[element].get_co2_emissions_by_year(i)) #Appending the co2 emissions for that year
            except:
                continue
        #Appending the inner list to the final list to create a 2D list
        final_list.append(inner_list)
    
    #Creating the x_list
    for i in range(min_year,max_year+ step_num, step_num):
        x_list.append(i)
        
    #Plotting the points with the style
    for i in range(len(iso_list)):
        y_list = []
        #Iterating through the years in x_list
        for j in range(len(x_list)):
            try:
                y_list.append(main_dict[iso_list[i]].co2_emissions[x_list[j]]) #Using that year to calculate co2 emission for specific country
            except:
                y_list.append(0.0)
        plt.plot(x_list,y_list,style_list[i])
        
    
    #Descriptors etc
    
    #Making the title:
    plt.title("‘CO2 emissions between " + str(min_year) + " and " + str(max_year) + " by mohammad.abdullah@mail.mcgill.ca")
    #Labelling the axis
    plt.ylabel("co2 (in millions of tonnes)")
    
    #Saving the File
    plt.savefig("co2_emissions_" + str(min_year) + "_"+ str(max_year) + ".png")
    #Making the legend
    plt.legend(iso_list)
    #Showing the plot
    plt.show()
    
    return final_list
    
    
#End of Code
    
if __name__ == "__main__":
    pass
    #doctest.testmod()
    
#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing Modules
import copy
import doctest
#Defining the class

class Country:
    """
    Defining a country
    
    Instance attributes: iso_code (a string), name (a string), continents (a list of strings), co2_emissions
                        (a dictionary mapping integers to floats), population (a dictionary mapping integers to integers)

    Class attributes: min_year_recorded (integer), max_year_recorded (integer).
    
    """
    min_year_recorded = float("inf")
    max_year_recorded = float("-inf")
    
    
    
    #Defining the constructor method
    def __init__(self, iso_code, name, continents, year, emissions, pop_year):
        """(Country, str, str, list, int, float, int)
        Initialises the object to its values accordingly (Constructor Function)

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.continents
        ['ASIA', 'EUROPE']

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.iso_code
        'RUS'

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.co2_emissions
        {2007: 1604.778}

        """
        #Checking for Assertion Error
        if len(iso_code) != 3 and iso_code != "OWID_KOS":
            raise AssertionError("Invalid ISO")
        
        #Initialising empty dictionaries
        co2_emissions = {}
        population = {}
        
        
        #Assignings the attributes to the object self
        self.iso_code = iso_code
        self.name = name
        self.continents = copy.copy(continents) #Copy of the list of continents
        self.year = year
        

        if emissions != -1:
            co2_emissions[year] = emissions #Adding the key-value pair to the dictionary
        
        if pop_year != -1:
            population[year] = pop_year #Adding the key-value pair to the dictionary
        
        #Assings the instance attributes to the object
        self.co2_emissions = co2_emissions
        self.population = population
        
        #Checking to update the max/min year
        if year > Country.max_year_recorded:
            Country.max_year_recorded = year
        if year < Country.min_year_recorded:
            Country.min_year_recorded = year
            
        
    def __str__(self):
        """(Country) -> str
        Returns the string representation of the country containing the name, continents, co2_emissions per year and population
        per year
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r)
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r).split("\\t")
        ['Russia', 'ASIA,EUROPE', '{2007: 1604.778}', '{2007: 14266000}']

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> str(r).count("\\t")
        3
        """
        #Setting up the return string
        new_str = self.name
        
        #Setting the continents
        if len(self.continents) >1:
            new_str = new_str + "\t" + self.continents[0] + "," + self.continents[1]
        else:
            new_str = new_str + "\t" + self.continents[0]
        
        #Setting the dictionaries up
        new_str = new_str + "\t" + str(self.co2_emissions) + "\t" + str(self.population)
        
        #Returning the string
        return new_str
    
    def add_yearly_data(self, str1):
        """(Country, str) -> None
        Updates the appropriate attributes of the country object.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.co2_emissions == {1949: 0.015, 2018: 9.439}
        True

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("2018\\t10.68\\t9805487")
        >>> r.population
        {2007: 14266000, 2018: 9805487}

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("1995\\t5.78145\\t6874125")
        >>> r.co2_emissions
        {2007: 1604.778, 1995: 5.78145}

        """
        
        #Splitting the input string into elements of a list
        temp_list = str1.split("\t")
        
        #Updating min/max year if need be
        if int(temp_list[0]) > Country.max_year_recorded:
            Country.max_year_recorded = int(temp_list[0])
        if int(temp_list[0]) < Country.min_year_recorded:
            Country.min_year_recorded = int(temp_list[0])
            
        #Updating the dictionaries
        if temp_list[1] != "":
            self.co2_emissions[int(temp_list[0])] = float(temp_list[1])
        if temp_list[2] != "":
            self.population[int(temp_list[0])] = int(temp_list[2])
        
        
            
    def get_co2_emissions_by_year(self,year_num):
        """(Country, int) -> float
        It returns the co2 emission of the country in the specified year if available.
        
        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_co2_emissions_by_year(1949)
        0.015

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("1995\\t5.78145\\t6874125")
        >>> r.get_co2_emissions_by_year(1995)
        5.78145

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("1995\\t5.78145\\t6874125")
        >>> r.get_co2_emissions_by_year(2007)
        1604.778
        
        """
        
        #Using try-catch to catch a possible key error
        try:
            #If key exists, it will return the co2_emissions in that year, otherwise will return 0.0
            return self.co2_emissions[year_num]
        except KeyError:
            return 0.0
        
    def get_co2_per_capita_by_year(self, year_num):
        """(Country, int) -> num/None
        It returns the co2 emission per capita in tonnes for the specified year if available.

        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> round(a.get_co2_per_capita_by_year(2018), 5)
        0.25427

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("1995\\t5.78145\\t6874125")
        >>> round(r.get_co2_per_capita_by_year(2007),4)
        112.4897

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("1995\\t5.78145\\t6874125")
        >>> round(r.get_co2_per_capita_by_year(1995),3)
        0.841
        
        """
        #Checking if all conditions are met
        #Assigning a temporary variable
        co2 = self.get_co2_emissions_by_year(year_num)
        
        #Checking the conditions
        if (co2) != 0.0 and (year_num in self.population):
            
            #Calculating and returning the final amount
            return (co2*10**6)/self.population[year_num]
        else:
            return None
        
    
    def get_historical_co2(self, year_num):
        """(Country, int) -> num
        It returns the historical (total) co2 emission in millions of tonnes that the country has produced for all years up
        to and including the specified year.
        
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> q.get_historical_co2(2000)
        45.277

        >>> a = Country("AFG", "Afghnistan", ["ASIA"], 1949, -1, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> a.get_historical_co2(2018)
        9.439
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> r.add_yearly_data("2018\\t9.439\\t37122000")
        >>> r.get_historical_co2(2018)
        1614.217
        
        """
        
        #Setting up a counter variable and a loop
        counter = 0.0
        
        #Loops through the years that are keys in the co2 dictionary
        for k in self.co2_emissions:
            
            #Checks if year_num is bigger than k, if true, it adds to the counter
            if k <= year_num:
                counter += self.get_co2_emissions_by_year(k)
                
        #Returns the counter
        return counter
        
    @classmethod
    def get_country_from_data(cls, str1):
        """(type, str) -> Country
        The method should return a new Country object created from the data in the input string.

        >>> a = Country.get_country_from_data("ALB\\tAlbania\\tEUROPE\\t1991\\t4.283\\t3280000")
        >>> a.__str__()
        'Albania\\tEUROPE\\t{1991: 4.283}\\t{1991: 3280000}'

        >>> a = Country.get_country_from_data("PAK\\tPakistan\\tASIA\\t1992\\t6.283\\t5589000")
        >>> a.continents
        ['ASIA']

        >>> a = Country.get_country_from_data("TUR\\tTurkey\\tASIA,EUROPE\\t1922\\t1.283\\t589000")
        >>> a.population
        {1922: 589000}

        """
        #Converting the string into elements of a list
        temp_list = str1.split("\t")
        
        #Continent sorting
        if "," in temp_list[2]:
            new_list = temp_list[2].split(",")
        else:
            new_list = [temp_list[2]]
        
        #Checking for Invalid Data
        for i in range(len(temp_list)):
            if len(temp_list[i]) == 0:
                temp_list.pop(i)
                temp_list.insert(i,"-1")
            
        
        return cls(temp_list[0], temp_list[1], new_list, int(temp_list[3]), float(temp_list[4]), int(temp_list[5]))
            
        
        
    @staticmethod
    def get_countries_by_continent(countries):
        """(list) -> dict
        The method returns a dictionary mapping a string representing a continent to a list of
        countries which all belong to that continent.
        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][1])
        'Russia\\tASIA,EUROPE\\t{2007: 1604.778}\\t{2007: 14266000}'

        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['ASIA'][0])
        'Afghanistan\\tASIA\\t{1949: 0.015, 2018: 9.439}\\t{1949: 7663783, 2018: 37122000}'

        >>> a = Country("AFG", "Afghanistan", ["ASIA"], 1949, 0.015, 7663783)
        >>> a.add_yearly_data("2018\\t9.439\\t37122000")
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [a, b, r]
        >>> d = Country.get_countries_by_continent(c)
        >>> str(d['EUROPE'][0])
        'Albania\\tEUROPE\\t{2007: 3.924}\\t{2007: 3034000}'
        """
        
        #Setting up the dictionary
        main_dict = {}
        
        #Sorting through the input list
        for c in countries:
            
            #Checking if more than 1 continent and looping as required
            for continent in c.continents:
                #Checking if there already exists the key
                if continent not in main_dict:
                    #Mapping the continent (key) to its value (Country object)
                    main_dict[continent] = [c]
                    
                else:
                    #Appending as required
                    main_dict[continent].append(c)
                    
        #Returning the dictionary
        return main_dict
    
                    
    @staticmethod
    def get_total_historical_co2_emissions(countries, year_num):
        """(list, int)-> float
        The method returns a float representing the total co2 emissions (in millions of tonnes)
        produced by all the countries in the input list for all years up to and including the specified year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> Country.get_total_historical_co2_emissions(c,2007)
        1721.161
        >>> Country.get_total_historical_co2_emissions(c,2000)
        49.56

        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> f = [q,q,q,q]
        >>> Country.get_total_historical_co2_emissions(f,2007)
        251.596

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> g = [r,q,r,q]
        >>> Country.get_total_historical_co2_emissions(g,2007)
        3335.354

        """
        #Setting up variable to be returned
        total_count = 0.0
        
        #Looping through the countries
        for c in countries:
            #Calling the function to get co2 of each country in the list
            total_count += c.get_historical_co2(year_num)
        
        #Returning the total count
        return total_count
    
    @staticmethod
    def get_total_co2_emissions_per_capita_by_year(countries, year_num):
        """(list, int) -> float
        Returns the Co2 emissions per capitia in tonnes produced by the countries in the given list in the specified year

        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> c = [b, r]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(c,2007), 5)
        92.98855

        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 334000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2000, 1604.778, 1266000)
        >>> c = [b, r]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(c,2007), 5)
        11.7485

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> g = [r,q]
        >>> round(Country.get_total_co2_emissions_per_capita_by_year(g,2007), 1)
        107.7


        """
        #Setting up variables
        total_co2 = 0.0
        total_pop = 0
        
        #Iterating through the countries list
        for c in countries:
            
            #Storing data in variables
            country_co2 = c.get_co2_emissions_by_year(year_num)
            #Incase of key error, goes to the next country
            try:
                country_pop = c.population[year_num]
            except KeyError:
                continue
            #Making sure the country is viable for calculation
            if country_co2 == 0.0 or country_pop == 0:
                continue
            #Changing the variables
            total_co2 += country_co2*10**6
            total_pop += country_pop
            
        #Checking if the total's are not 0
        if total_co2 == 0.0 or total_pop == 0:
            return 0.0
        
        return total_co2/total_pop
            
    @staticmethod
    def get_co2_emissions_per_capita_by_year(countries, year_num):
        """(list, int) -> dict
        The method returns a dictionary mapping objects of type Country to floats representing the co2 emissions
        per capita in tonnes produced by the country in the specified year.
        
        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> c = [b, r]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(c,2007)
        >>> len(d1)
        2
        >>> round(d1[r], 5)
        112.4897

        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> g = [r,q]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(g,2007)
        >>> round(d1[q],2)
        51.64
        
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> g = [r,q]
        >>> d1 = Country.get_co2_emissions_per_capita_by_year(g,2001)
        >>> print(d1[r])
        None
        """

        #An empty dictionary
        main_dict = {}
        
        #Iterating through the countries list
        for c in countries:
            
            #Making the key-value pair
            main_dict[c] = c.get_co2_per_capita_by_year(year_num)
        
        #Returning the main dictionary
        return main_dict
        
        
    @staticmethod
    def get_historical_co2_emissions(countries, year_num):
        """(list, int) -> dict
        The method returns a dictionary mapping objects of type Country to floats representing the total co2 emissions
        produced by that country for all years up to and including the specified year.

        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> d1 = Country.get_historical_co2_emissions(c,2007)
        >>> len(d1)
        3

        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> d1 = Country.get_historical_co2_emissions(c,2001)
        >>> d1[b]
        4.283

        >>> b = Country("ALB", "Albania", ["EUROPE"], 2007, 3.924, 3034000)
        >>> r = Country("RUS", "Russia", ["ASIA", "EUROPE"], 2007, 1604.778, 14266000)
        >>> q = Country("QAT", "Qatar", ["ASIA"], 2007, 62.899, 1218000)
        >>> b.add_yearly_data("1991\\t4.283\\t3280000")
        >>> q.add_yearly_data("1993\\t30.985\\t501000")
        >>> q.add_yearly_data("1989\\t14.292\\t462000")
        >>> c = [b, r, q]
        >>> d1 = Country.get_historical_co2_emissions(c,1988)
        >>> d1[r]
        0.0
        """
        
        #Creating a dictionary
        main_dict = {}
        
        #Iterating through the countries list
        for c in countries:
            #Mapping the key (country) to the data (historical co2)
            main_dict[c] = c.get_historical_co2(year_num)
            
        #Returning the main dictionary
        return main_dict
    
    @staticmethod
    def get_top_n(countries, n):
        """(dict, int) -> list
        Returns a list of tuples which are sorted in descending order and in a way such that the list only
        contains the top n number of tuples
        
        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 5, b: 5, c: 3, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t = Country.get_top_n(d, 10)
        >>> t
        [('BOL', 10), ('IRL', 9), ('NZL', 8), ('MAR', 7), ('PRY', 7), ('SEN', 6), ('ALB', 5), ('AUT', 5), ('PER', 4), ('BEL', 3)]

        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 10, b: 10, c: 10, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t = Country.get_top_n(d, 4)
        >>> t
        [('ALB', 10), ('AUT', 10), ('BEL', 10), ('BOL', 10)]

        >>> a = Country("ALB", "Albania", [], 0, 0.0, 0)
        >>> b = Country("AUT", "Austria", [], 0, 0.0, 0)
        >>> c = Country("BEL", "Belgium", [], 0, 0.0, 0)
        >>> d = Country("BOL", "Bolivia", [], 0, 0.0, 0)
        >>> e = Country("BRA", "Brazil", [], 0, 0.0, 0)
        >>> f = Country("IRL", "Ireland", [], 0, 0.0, 0)
        >>> g = Country("MAR", "Marocco", [], 0, 0.0, 0)
        >>> h = Country("NZL", "New Zealand", [], 0, 0.0, 0)
        >>> i = Country("PRY", "Paraguay", [], 0, 0.0, 0)
        >>> j = Country("PER", "Peru", [], 0, 0.0, 0)
        >>> k = Country("SEN", "Senegal", [], 0, 0.0, 0)
        >>> l = Country("THA", "Thailand", [], 0, 0.0, 0)
        >>> d = {a: 10, b: 10, c: 10, d: 10, e: 3, f: 9, g: 7, h: 8, i: 7, j: 4, k: 6, l: 0}
        >>> t = Country.get_top_n(d, 13)
        >>> t[8:]
        [('SEN', 6), ('PER', 4), ('BRA', 3), ('THA', 0)]
        """
        #Final list
        final_list = []
        #Some temp variables
        temp_list = []
        num_list = []
        
        #Iterating through the dictionary
        for element in countries:
            #Creating a 2D list with iso_codes as the first entry and the number as the second
            temp_list.append([element.iso_code,countries[element]])
            #Creating a reference list for the numbers which we'll sort
            num_list.append(countries[element])
            
        #Sorting the temporary list by the first element (ie. iso_code alphabetically)
        temp_list.sort()
        
        #Sorting the number list and converting it to descending order
        num_list.sort()
        num_list = num_list[::-1]
        
        #Iterating through the number_list (biggest to smallest number)
        for element in num_list:
            
            #Iterating through the temp_list which is alphabetically sorted
            #First number to come up will be the isocode which is alphabetically smaller than the other code with the same number
            for r in temp_list:
                
                #If an inner list's second element has the same number as the element in num_list we have a match  
                if r[1] == element:
                    #We append the final list with the iso_code and the number
                    final_list.append((r[0],element))
                    temp_list.remove(r) #Remove the row so that it isn't repeated while searching through temp_list
                    break #Go to the next element in num_list
                    
            
        #Checking if n is bigger than the lenght of the final_list
        if n> len(final_list):
            return final_list
        else:
            while len(final_list) > n:
                final_list.pop() #Removes the last element from the list until it's size is good
            
            return final_list
        
#Class Code ends here
        
#Code for function


def get_countries_from_file(str1):
    """(str) -> dict
    The function creates and return a dictionary mapping ISO country codes (strings) to objects
    of type Country based on the data in the file.
    
    >>> d1 = get_countries_from_file("small_co2_data.tsv")
    >>> len(d1)
    9
    >>> str(d1['ALB'])
    'Albania\\tEUROPE\\t{2002: 3.748}\\t{2002: 3126000}'

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> d2["RUS"].continents
    ['ASIA', 'EUROPE']

    >>> d2 = get_countries_from_file("large_co2_data.tsv")
    >>> d2["OWID_KOS"].name
    'Kosovo'
    
    """
    #Defining the dictionary
    main_dict = {}
    
    #Opening the file to read
    r_object = open(str1, "r", encoding="utf-8")
    
    #Iterating through each line
    for line in r_object:
        
        line = line.strip("\n")
        #Fixing input
        temp_list = line.split("\t")
        
        #Replacing empty strings with a -1 to prevent errors
        """
        for i in range(len(temp_list)):
            if len(temp_list[i]) == 0:
                temp_list.pop(i)
                temp_list.insert(i,"-1")
        """
        
        new_line = "\t".join(temp_list)
        #print(new_line)
        
        
        #Calling class method to create my Country object
        country1 = Country.get_country_from_data(new_line)
        
        #Mapping ISO to country object
        #Checking if the country already exists
        if country1.iso_code not in main_dict:
            main_dict[country1.iso_code] = country1
        else:
            #Adding co2 if it's not absent from the list
            
            #Checking if either of the population or co2 is missing and creating str2 as appropriate
            if temp_list[4] != "-1" and temp_list[5] != "-1":
                str2 = temp_list[3] + "\t" + temp_list[4] + "\t" + temp_list[5]
            elif temp_list[4] == "-1" and temp_list[5] != "-1":
                str2 = temp_list[3] + "\t" + "" + "\t" + temp_list[5]
            elif temp_list[4] != "-1" and temp_list[5] == "-1":
                str2 = temp_list[3] + "\t" + temp_list[4] + "\t" + ""
            #Adding the yearly data to the value inside the dictionary (which is a country object)
            main_dict[country1.iso_code].add_yearly_data(str2)
            
    
    r_object.close()
    
    return main_dict

if __name__ == "__main__":
    doctest.testmod()
#End of Code    
#Author: Mohammad Abdullah, Student ID: 260980866
#Defining the 24 global variables whose values will be used throughout the program
#Their assignments can also be seen here
SMOOTHIE1_NAME = "Pineapple Banana"
SMOOTHIE2_NAME = "Almond Basil"
SMOOTHIE3_NAME = "Purple Surprise"
SMOOTHIE4_NAME = "Onion Toffee"
 
SMOOTHIE1_COST = 4.99
SMOOTHIE2_COST = 6.49
SMOOTHIE3_COST = 2.99
SMOOTHIE4_COST = 9.99

SIZE1_NAME = "Small"
SIZE2_NAME = "Medium"
SIZE3_NAME = "Large"
SIZE4_NAME = "Galactic" 

SIZE1_COST = -2.0
SIZE2_COST = 0.0
SIZE3_COST = 2.0
SIZE4_COST = 100.0

TOPPING1_NAME = "no topping" 
TOPPING2_NAME = "cinnamon"
TOPPING3_NAME = "chocolate shavings"
TOPPING4_NAME = "shredded coconut"
 
TOPPING1_COST = 0.0
TOPPING2_COST = 1.0
TOPPING3_COST = 1.0
TOPPING4_COST = 1.0

#Making the first function that will that will be responsible for printing the main prompts of the program.
def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    """(string,string,float,string,float,string,float,string,float) -> string
    Prints out the formatting as well as the required data to help the user make their choice and records their choice.
    
    >>> pose_question_with_costs("Which size would you like?", "Small", -2.0, "Medium", 0.0,
        "Large", 2.0, "Galactic", 100.0)
    Which size would you like?
    1)  $ -2.0       Small
    2)  $ 0.0        Medium
    3)  $ 2.0        Large
    4)  $ 100.0      Galactic
    Your Choice (1-4): 4
    You have selected Galactic
    'Galactic'
    
    >>> pose_question_with_costs("Which would you want?", "Tiny", -20.0, "medium", 0.0,
        "Regular", 10.0, "Massive", 100.0)
    Which would you want?
    1)  $ -20.0          Tiny
    2)  $ 0.0        medium
    3)  $ 10.0       Regular
    4)  $ 100.0          Massive
    Your Choice (1-4): 4
    You have selected Massive
    'Massive'
    
    >>> pose_question_with_costs("Presumptive Statement", "test 1", -20.0, "test3", 0.0,
            "test4", 10.0, "test 10", 100.0)
    Presumptive Statement
    1)  $ -20.0          test 1
    2)  $ 0.0        test3
    3)  $ 10.0       test4
    4)  $ 100.0          test 10
    Your Choice (1-4): 2
    You have selected test3
    'test3'
    """
    #Printing the required parameters that have been passed to this function
    print(question)
    print("1) \t$",cost1, "\t \t", option1)
    print("2) \t$",cost2, "\t \t", option2)
    print("3) \t$",cost3, "\t \t", option3)
    #This is done to make sure there are no issues with the word "Galactic" while using tab (\t) since otherwise it would print
    #in an awkard position
    if option4 == "Galactic": 
        print("4) \t$",cost4, "\t", option4)
    else:
        print("4) \t$",cost4, "\t\t", option4)
    prompt = input("Your Choice (1-4): ")
    if prompt == "1":
        print("You have selected " + option1)
        return option1
    elif prompt == "2":
        print("You have selected " + option2)
        return option2
    elif prompt == "3":
        print("You have selected " + option3)
        return option3
    elif prompt == "4":
        print("You have selected " + option4)
        return option4
    else:
        return ""
    #The above if-else statements make sure that the correct input has been recorded by the program and shows it to the user
#The following function calculates the subtotal amount by summing the 3 corresponding values of parameters that have been passed to the
#function
def calculate_subtotal(smoothie_type, smoothie_size, topping):
    """ (string, string, string) -> float
    Calculates the subtotal by adding the corresponding values of the given parameters'
    
    >>> calculate_subtotal(SMOOTHIE3_NAME,SIZE1_NAME, TOPPING1_NAME)
    0.99
    
    >>> calculate_subtotal(SMOOTHIE4_NAME,SIZE4_NAME, TOPPING4_NAME)
    110.99
    
    calculate_subtotal(SMOOTHIE1_NAME,SIZE3_NAME, TOPPING2_NAME)
    7.99
    
    """
    temp_total = 0 #Initializing the temporary total to 0 to make sure its accurate
    if smoothie_type == SMOOTHIE1_NAME:
        temp_total = temp_total + SMOOTHIE1_COST
    elif smoothie_type == SMOOTHIE2_NAME:
        temp_total = temp_total + SMOOTHIE2_COST
    elif smoothie_type == SMOOTHIE3_NAME:
        temp_total = temp_total + SMOOTHIE3_COST
    elif smoothie_type == SMOOTHIE4_NAME:
        temp_total = temp_total + SMOOTHIE4_COST
    #The above if else add the cost of the type of smoothie to the variable temp_total
    if smoothie_size == SIZE1_NAME:
        temp_total = temp_total + SIZE1_COST
    elif smoothie_size == SIZE2_NAME:
        temp_total = temp_total + SIZE2_COST
    elif smoothie_size == SIZE3_NAME:
        temp_total = temp_total + SIZE3_COST
    elif smoothie_size == SIZE4_NAME:
        temp_total = temp_total + SIZE4_COST
    #The above if else add the cost of the size of smoothie to the variable temp_total
    if topping == TOPPING1_NAME:
        temp_total = temp_total + 0
    else:
        temp_total = temp_total + 1
    #The above if else add the cost of the topping (if any) of the smoothie to the variable temp_total
    return round(temp_total,2)
    #Here we round the final answer to 2 Decimal Points

#The following function prints the receipt for the user
def print_receipt(subtotal, smoothie_type, smoothie_size, topping):
    """ (float, string, string, string) -> float
    Prints the Receipt that is calculated through checking the parameters' values and using the corresponding data that is given.
    
    >>> print_receipt(110.99, SMOOTHIE1_NAME, SIZE4_NAME, TOPPING4_NAME)
    You ordered a galactic Pineapple Banana smoothie with shredded coconut
    Smoothie cost:       $ 105.99
    GST:       $ 5.30
    QST:       $ 10.57
    Total:     $ 121.86
    121.86
    
    >>> print_receipt(2.99, SMOOTHIE3_NAME, SIZE2_NAME, TOPPING1_NAME)
    You ordered a Medium Purple Surprise
    Smoothie cost:       $ 2.99
    GST:       $ 0.15
    QST:       $ 0.3
    Total:     $ 3.44
    3.44
    
    >>> print_receipt(10.99, SMOOTHIE4_NAME, SIZE2_NAME, TOPPING2_NAME)
    You ordered a Medium Onion Toffee with cinnamon
    Smoothie cost:       $ 10.99
    GST:       $ 0.55
    QST:       $ 1.1
    Total:     $ 12.64
    12.64
    
    
    """
    final_total = round(subtotal,2) + round((0.05*subtotal),2) + round((0.09975*subtotal),2) #Calculating the final total in advance
    if topping != TOPPING1_NAME: #Checking whether there is a topping included or not
        print("You ordered a " + smoothie_size + " " + smoothie_type + " smoothie" + " with " + topping)
    else:
        print("You ordered a " + smoothie_size + " " + smoothie_type + " smoothie")
    #Printing the final values of the Subtotal, the GST and the QST Respectively along with the final total which is also returned
    print("Smoothie cost: \t\t $" , round(subtotal,2))
    print("GST: \t   $", round((0.05*subtotal),2))
    print("QST: \t   $", round((0.09975*subtotal),2))
    print("Total: \t   $", round(final_total,2))
    return round(final_total,2)
    
#Below is the main order function which calls all of the above defined functions accordingly
def order():
    """(None) -> None
    Welcomes the User, calls the respective functions accordingly, calculates the overall bill and prints it
    
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    Which smoothie would you like?
    1)  $ 4.99       Pineapple Banana
    2)  $ 6.49       Almond Basil
    3)  $ 2.99       Purple Surprise
    4)  $ 9.99       Onion Toffee
    Your Choice (1-4): 3
    You have selected Purple Surprise
    Unfortunately, we are out of Purple Surprise
    You will be served Onion Toffee Smoothie
    Which size would you like?
    1)  $ -2.0       Small
    2)  $ 0.0        Medium
    3)  $ 2.0        Large
    4)  $ 100.0             Galactic
    Your Choice (1-4): 3
    You have selected Large
    Which topping would you like?
    1)  $ 0.0        no topping
    2)  $ 1.0        cinnamon
    3)  $ 1.0        chocolate shavings
    4)  $ 1.0        shredded coconut
    Your Choice (1-4): 1
    You have selected no topping
    You ordered a Large Onion Toffee
    Smoothie cost:          $ 11.99
    GST:       $ 0.6
    QST:       $ 1.2
    Total:   $ 13.79
    
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    Which smoothie would you like?
    1)  $ 4.99       Pineapple Banana
    2)  $ 6.49       Almond Basil
    3)  $ 2.99       Purple Surprise
    4)  $ 9.99       Onion Toffee
    Your Choice (1-4): 4
    You have selected Onion Toffee
    You will be served Onion Toffee Smoothie
    Which size would you like?
    1)  $ -2.0       Small
    2)  $ 0.0        Medium
    3)  $ 2.0        Large
    4)  $ 100.0             Galactic
    Your Choice (1-4): 4
    You have selected Galactic
    Which topping would you like?
    1)  $ 0.0        no topping
    2)  $ 1.0        cinnamon
    3)  $ 1.0        chocolate shavings
    4)  $ 1.0        shredded coconut
    Your Choice (1-4): 4
    You have selected shredded coconut
    You ordered a Galactic Onion Toffee with shredded coconut
    Smoothie cost:          $ 110.99
    GST:       $ 5.55
    QST:       $ 11.07
    Total:   $ 127.61
    
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    Which smoothie would you like?
    1)  $ 4.99       Pineapple Banana
    2)  $ 6.49       Almond Basil
    3)  $ 2.99       Purple Surprise
    4)  $ 9.99       Onion Toffee
    Your Choice (1-4): 3
    You have selected Purple Surprise
    Unfortunately, we are out of Purple Surprise
    You will be served Onion Toffee Smoothie
    Which size would you like?
    1)  $ -2.0       Small
    2)  $ 0.0        Medium
    3)  $ 2.0        Large
    4)  $ 100.0             Galactic
    Your Choice (1-4): 1
    You have selected Small
    Which topping would you like?
    1)  $ 0.0        no topping
    2)  $ 1.0        cinnamon
    3)  $ 1.0        chocolate shavings
    4)  $ 1.0        shredded coconut
    Your Choice (1-4): 1
    You have selected no topping
    You ordered a Small Onion Toffee
    Smoothie cost:           $ 7.99
    GST:       $ 0.4
    QST:       $ 0.8
    Total:   $ 9.19
    
    
    """
    #Printing the welcome message
    print("Welcome to Smooth Smoothies Smoothie Ordering System")
    print("Have you tried our new Onion Toffee smoothie?")
    option_check1 = pose_question_with_costs("Which smoothie would you like?",SMOOTHIE1_NAME,SMOOTHIE1_COST,SMOOTHIE2_NAME,SMOOTHIE2_COST,
                                            SMOOTHIE3_NAME,SMOOTHIE3_COST,SMOOTHIE4_NAME,SMOOTHIE4_COST)
    
    #The code above prints the first question along with the appropriate data and asks the user to select it
    #The code below shuffles through the value returned by the function and checks what the user inputted
    
    if option_check1 == SMOOTHIE1_NAME:
        print("Unfortunately, we are out of Pineapple Banana")
        print("You will be served Onion Toffee Smoothie")
    elif option_check1 == SMOOTHIE2_NAME:
        print("Unfortunately, we are out of Almond Basil")
        print("You will be served Onion Toffee Smoothie")
    elif option_check1 == SMOOTHIE3_NAME:
        print("Unfortunately, we are out of Purple Surprise")
        print("You will be served Onion Toffee Smoothie")
    elif option_check1 == SMOOTHIE4_NAME:
        print("You will be served Onion Toffee Smoothie")
    else:
        print("Sorry, that is not a valid option")
        return #Ends the function order since the value entered is invalid
    
    #Prints and checks what size the user ordered
    option_check2 = pose_question_with_costs("Which size would you like?", SIZE1_NAME,SIZE1_COST,SIZE2_NAME,SIZE2_COST,SIZE3_NAME,
                                             SIZE3_COST,SIZE4_NAME,SIZE4_COST)
    #Prints and checks what topping the user ordered
    option_check3 = pose_question_with_costs("Which topping would you like?", TOPPING1_NAME,TOPPING1_COST,TOPPING2_NAME,TOPPING2_COST,
                                             TOPPING3_NAME,TOPPING3_COST,TOPPING4_NAME,TOPPING4_COST)
    #Calculates the Subtotal
    subtotal = calculate_subtotal(SMOOTHIE4_NAME, option_check2, option_check3)
    #Prints the Final Receipt
    print_receipt(subtotal, SMOOTHIE4_NAME, option_check2, option_check3)
#End of Program
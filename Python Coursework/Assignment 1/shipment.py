#Author: Mohammad Abdullah, Student ID: 260980866

#The following code is comprised of all of the function definitions required

def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    """(int,int,int,int,int,int,int,int,int) -> string
    Calculates the checksum of each digit by multiplying it by its appropriate place value
    and dividing it by 11 and printing the remainder
    
    >>> calculate_isbn_checksum_by_digits(8, 7, 1, 1, 0, 7, 5, 5, 9)
    '7'
    >>> calculate_isbn_checksum_by_digits(8, 7, 1, 1, 0, 7, 5, 5, 3)
    '8'
    >>> calculate_isbn_checksum_by_digits(0, 0, 9, 1, 4, 7, 5, 5, 3)
    '8'
    """
    #Individually multiplies all the 9 digits by the corresponding place value that they have
    #After multipliction it sums it all into a single answer and divides it by 11 and returns the remainder
    checksum = (d1 + (d2*2) + (d3*3) + (d4*4) + (d5*5) + (d6*6) + (d7*7) + (d8*8) + (d9*9)) % 11
    if checksum == 10:
        return "X"
    else:
        return str(checksum) #Conversion of numerical value into a string
    

def calculate_isbn_checksum(isbn):
    """(num) -> string
    Calculates the checksum by seperating the rightmost digit and multiplying it by the appropriate
    place value and then dividing it by 11 and printing the remainder
    
    >>> calculate_isbn_checksum(871945386)
    '8'
    
    >>> calculate_isbn_checksum(992945996)
    '0'
    
    >>> calculate_isbn_checksum(902945996)
    '4'
    """
    #Following code seperates the rightmost number from the isbn provided
    #It also takes the integer part of dividing the isbn by 10 to convert the 9 digits into 8
    #By doing the above method, it slowly keeps seperating the rightmost digit and assigning it to the appropriate variable
    n9 = isbn % 10
    isbn = int(isbn /10)
    n8 = isbn % 10
    isbn = int(isbn /10)
    n7 = isbn % 10
    isbn = int(isbn /10)
    n6 = isbn % 10
    isbn = int(isbn /10)
    n5 = isbn % 10
    isbn = int(isbn /10)
    n4 = isbn % 10
    isbn = int(isbn /10)
    n3 = isbn % 10
    isbn = int(isbn /10)
    n2 = isbn % 10
    isbn = int(isbn /10)
    n1 = isbn % 10
    #Calls the previous function and calculates the checksum of the seperated digits
    checkdigit = calculate_isbn_checksum_by_digits(n1, n2, n3, n4, n5, n6, n7, n8, n9)
    return checkdigit
    
def is_isbn(isbn, checksum):
    """(num, string) -> Bool
    Takes an isbn and its checkdigit and checks whether they are consistent with each other
    
    >>> is_isbn(902945996,"4")
    True
    
    >>> is_isbn(991945996,"4")
    False
    
    >>> is_isbn(871107559,"4")
    False
    """
    #Calls the previous function using the isbn provided
    calculated_num = calculate_isbn_checksum(isbn)
    #Checks whether the value returned is consistent with the value provided already
    if calculated_num == checksum:
        return True
    else:
        return False
    
def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    """(int,int,int,int,int,int) -> Bool
    Checks whether a book of the given dimensions fits inside of a box of the given dimensions with
    rotation
    
    >>> book_fits_in_box(15, 2, 2, 2, 15, 2)
    True
    >>> book_fits_in_box(15, 2, 2, 7, 15, 2)
    False
    >>> book_fits_in_box(5, 2, 1, 2, 15, 2)
    True
    """
    #The following 6 conditions check all possible permutations of rotating the book
    #Since we're dealing with 3 planes, we need 3! conditions, i.e 6 as provided
    if box_d>=book_w and box_h>=book_d and box_w>=book_h:
        return True
    elif box_d>=book_w and box_h>=book_h and box_w>=book_d:
        return True
    elif box_d>=book_d and box_h>=book_w and box_w>=book_h:
        return True
    elif box_d>=book_d and box_h>=book_h and box_w>=book_w:
        return True
    elif box_d>=book_h and box_h>=book_w and box_w>=book_d:
        return True
    elif box_d>=book_h and box_h>=book_d and box_w>=book_w:
        return True
    #If none of the 6 conditions are satisfied, then we exit the function by returning false 
    return False

    
def get_smallest_box_for_book(book_w, book_d, book_h):
    """(int,int,int) -> string
    Checks what type of box a book of the given dimensions would fit in from the given presets
    
    >>> get_smallest_box_for_book(12, 12, 2)
    'medium'
    >>> get_smallest_box_for_book(9, 9, 2)
    'small'
    >>> get_smallest_box_for_book(19, 18, 4)
    'large'
    """
    temp = "" #Initializes temp to be an empty string in case no box fits the book's dimensions
    #The 3 conditionals check which box size the book could fit into by taking the smallest into consideration first
    if book_fits_in_box(10,10,2,book_w,book_d,book_h):
        temp = "small"
    elif book_fits_in_box(15,15,3,book_w,book_d,book_h):
        temp = "medium"
    elif book_fits_in_box(20,20,4,book_w,book_d,book_h):
        temp = "large"
    #Returns the temp value as string
    return temp

def get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h):
    """(int,int,int,int,int,int) -> int
    Checks how many books of given dimensions would fit inside the box
    of the given dimensions (without rotation of books)
    
    >>> get_num_books_for_box(10, 5, 5, 5, 5, 2)
    4
    
    >>> get_num_books_for_box(10, 5, 5, 10, 5, 1)
    5
    
    >>> get_num_books_for_box(10, 10, 10, 10, 10, 9)
    1
    """
    volume1 = 0 #Initializes volume1 variable to be 0 in case no book fits in the box

    #This checks whether all the corresponding box's dimensions are greater than the books
    if (box_w >= book_w) and (box_d >= book_d) and (box_h >= book_h):
        #Checks if atleast 1 book can fit into the box without rotation
        #The code below reassigns the dimensions of the books by floor dividing the dimension of the boxes with the dimensions of the books 
        book_w = box_w // book_w 
        book_d = box_d // book_d
        book_h = box_h // book_h
        #Once we have our new dimensions, we have an idea of how many books will fit into that specific plane (x,y,z)
        #Once we know the respective dimensions, we can just multiply them by each other to note how many books can be accomadated within the box.
        volume1 = book_w * book_d * book_h
        
    return volume1 #Returns the volume as a number of the books that will fit into the box
    
def main():
    """ (None) -> None
    Calls a greeting, and then a variety of options from where the user
    can choose and access the functions above and see their corresponding output
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice (1-4): 1
    Enter ISBN: 100101011
    Enter Checksum: 1
    ISBN is invalid (checksum did not match)
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice (1-4): 2
    Enter Box Dimensions:
    Enter box widht: 5
    Enter box height: 5
    Enter box depth: 10
    Enter book dimensions
    Enter book width: 2
    Enter book height: 3
    Enter book depth: 5
    Book fits in Box
    
    >>> main()
    Welcome to the shipment calculation system.
    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box
    Enter choice (1-4): 3
    Enter book dimensions
    Enter book width: 10
    Enter book height: 12
    Enter book depth: 3
    Book with these dimensions fits in a medium box.
    """
    #Displays the Welcome and the associated options for the user to select one of them.
    
    print("Welcome to the shipment calculation system.")
    print("1) Check ISBN")
    print("2) Check box/book size")
    print("3) Get smallest box size for book")
    print("4) Get num equally-sized books per box")
    
    prompt = int(input("Enter choice (1-4): "))#Asks user for input
    #Loads the program according to the user's input
    if prompt == 1:
        isbn1 = int(input("Enter ISBN: ")) #Asks isbn
        checksum1 = input("Enter Checksum: ") #Asks checksum
        if is_isbn(isbn1,checksum1): #Calls the function to check whether the above 2 variables are consistent
            print("ISBN is valid (checksum matched)")
        else:
            print("ISBN is not valid (checksum did not match)")
        #Prints the required output
    elif (prompt == 2 or prompt == 4): #Since both prompt 2 and 4 require similar inputs from the user
        #Taking inputs and some print statements
        print("Enter Box Dimensions:")
        
        box_w1 = int(input("Enter box widht: "))
        box_h1 = int(input("Enter box height: "))
        box_d1 = int(input("Enter box depth: "))
        
        print("Enter book dimensions")
        
        book_w1 = int(input("Enter book width: "))
        book_h1 = int(input("Enter book height: "))
        book_d1 = int(input("Enter book depth: "))
        
        if prompt == 2: #checks the prompt again to call the necessary function
            if book_fits_in_box(box_w1, box_d1, box_h1, book_w1, book_d1, book_h1):
                print("Book fits in Box") 
            else:
                print("Book does not fit in Box")
            #Prints the appropriate output
        elif prompt == 4:
            num_of_books = get_num_books_for_box(box_w1, box_d1, box_h1, book_w1, book_d1, book_h1)
            print(str(num_of_books) + " books can fit inside the box of the provided dimensions")
            
            
    elif prompt == 3:
        #Takes the appropriate inputs from the user
        print("Enter book dimensions")
        
        book_w1 = int(input("Enter book width: "))
        book_h1 = int(input("Enter book height: "))
        book_d1 = int(input("Enter book depth: "))
        
        output1 = get_smallest_box_for_book(book_w1, book_d1, book_h1)
        if output1 != "": #Checks to make sure that the books fit inside the box through using the returned value
            print("Book with these dimensions fits in a " + output1 + " box.")
        else:
            print("Book doesn't fit in the box")
        #Prints the appropriate output
#End of Program
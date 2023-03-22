#Author: Mohammad Abdullah
#Student ID: 260980866

#Importing Required modules
import turtle
import random
#Main Function
def my_artwork():
    """(none) -> none
    Makes the signature first, then calls the respective functions to create the shapes
    
    """
    #Creating the Turtle Object
    pen1 = turtle.Turtle()
    pen1.speed("fastest")

    
    #Signing "M" on the drawing.
    pen1.penup()
    pen1.goto(300,350)
    pen1.pendown()
    pen1.left(90)
    pen1.color("crimson")
    pen1.forward(28)
    pen1.right(143.13)
    pen1.forward(35)
    pen1.left(106.26)
    pen1.forward(35)
    pen1.right(143.13)
    pen1.forward(28)
    pen1.color("black")
    #Puts pen up for transporting the turtle
    pen1.penup()
    pen1.goto(0,-200)
    pen1.pendown()
    
    #Taking input for num of sides
    sides = int(input("Enter number of sides of the shape you would like to draw (between 3 & 17 Inclusive): "))
    
    side_len = random.randint(55,75) #Generates Random number that would be the lenght of the sides of the polygon
    
    #Creates 2 Polygons (Mirrored)
    polygon(pen1,side_len,sides,"r")
    polygon(pen1,side_len,sides,"l")
    
    #Creates a circle and a box, which contains 3 shapes in total
    draw_circle("gold","aqua")
    
    
def draw_circle(color1,color2):
    """(str,str) -> None
    Creates a rectangular box in which fits a circle and 2 traingles
    
    """
    #Creates another turtle object
    pen2 = turtle.Turtle()
    
    #Creating a rectangular box which is filled by the color azure
    pen2.fillcolor("azure")
    pen2.begin_fill()
    pen2.forward(250)
    pen2.left(90)
    pen2.forward(300)
    pen2.left(90)
    pen2.forward(500)
    pen2.left(90)
    pen2.forward(300)
    pen2.left(90)
    pen2.forward(250)
    pen2.end_fill()
    
    #Creates the right part of the circle with the appropriate color filling
    pen2.fillcolor(color1)
    pen2.begin_fill()
    pen2.circle(150,180)
    pen2.left(90)
    pen2.end_fill()
    
    #Aligns the turtle object correctly
    pen2.right(90)
    
    #Creates the right part of the circle with the appropriate color filling
    pen2.fillcolor(color2)
    pen2.begin_fill()
    pen2.circle(150,180)
    pen2.end_fill()
    
    #Transports the turtle to the appropriate point
    pen2.penup()
    pen2.goto(150,300)
    pen2.pendown()
    
    #Creates the right triangle
    pen2.fillcolor("aqua")
    pen2.begin_fill()
    pen2.right(90)
    pen2.forward(300)
    pen2.left(146.3)
    pen2.forward(180.2)
    pen2.left(67.4)
    pen2.forward(180.2)
    pen2.end_fill()
    
    #Transports the turtle to the appropriate point
    pen2.penup()
    pen2.goto(-150,300)
    pen2.pendown()
    
    #Creates the left triangle
    pen2.fillcolor("gold")
    pen2.begin_fill()
    pen2.left(146.3)
    pen2.forward(300)
    pen2.right(146.3)
    pen2.forward(180.2)
    pen2.right(67.4)
    pen2.forward(180.2)
    pen2.end_fill()
    
                 
    
def polygon(pen3,side_len,num_sides,direction):
    """(Turtle,int,int) -> void
    Creates a polygon shape which has the corresponding side lenght, number of sides, and tells us
    in what direction we have to draw the polygon
    
    """
    #Fills the polygons with the color indigo
    pen3.fillcolor("indigo")
    pen3.begin_fill()
    #Loops through the num of sides to change the direction of the turtle head after drawing the side
    for i in range(num_sides):
        pen3.forward(side_len)
        #Checks whether we're drawing the shape on the right or the left
        if direction == "l":
            pen3.left(360/num_sides)
        elif direction == "r":
            pen3.right(360/num_sides)
    pen3.end_fill()
    
#End of Code

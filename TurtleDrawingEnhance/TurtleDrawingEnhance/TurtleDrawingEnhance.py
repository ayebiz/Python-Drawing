#Learn how to use Turtle
#Try to deploy as much Turtle function as possible
import turtle
#Set variables to zero
nosides = 0
outlength = 0
inlength = 0
#Define number of sides
nosides = int(input('How many sides you wanted to draw? '))
#Define the outer length of the object
outlenght = 26
#Define the inner length of the object
inlenght = 18
#Define the color of the pen for outer and inner object
color1 = "blue"
color2 = "red"
#Move pen to a new position without drawing and report pen position
turtle.penup()
print(turtle.position())
#Define how the pen move and report pen position
turtle.forward(-205)
print(turtle.position())
turtle.left(45)
print(turtle.position())
turtle.right(90)
print(turtle.position())
turtle.pendown()
#Draw the pattern
for step in range(nosides):
    turtle.color(color1)
    turtle.pensize(3)
    turtle.forward(outlenght)
    turtle.right(360/nosides)
    print(turtle.position())
    for moresteps in range(nosides):
        turtle.pensize(1)
        turtle.color(color2)
        turtle.forward(inlenght)
        turtle.right(360/nosides)
#Bring the pen up and set that home
turtle.penup()
turtle.home()
#Print the Interger to confirm 
print("This is the original value")
print(int(nosides))
print(int(outlenght))
print(int(inlenght))
#Try to get the original value and divide that by 2
#Have to convert the float or string to integer
#Draw 2nd pattern
#reduce pattern size by half
nosides1 = int(int(nosides)/2)
outlenght1 = int(int(outlenght)/2)
inlenght1 = int(int(inlenght)/2)
#Print the result of the interger
print("This is the new value")
print(nosides1)
print(outlenght1)
print(inlenght1)
turtle.pendown()
for step in range(nosides1):
    turtle.color(color1)
    turtle.pensize(3)
    turtle.forward(outlenght1)
    turtle.right(360/nosides1)
    print(turtle.position())
    for moresteps in range(nosides1):
        turtle.pensize(1)
        turtle.color(color2)
        turtle.forward(inlenght1)
        turtle.right(360/nosides1)
#This is to mess thing up!!!
        turtle.forward(80)
turtle.penup()
turtle.forward(205)
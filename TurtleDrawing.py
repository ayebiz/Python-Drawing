#Learn how to use Turtle
#Try to deploy as much Turtle function as possible
import turtle
#Set variables to zero
nosides = 0
outlength = 0
inlength = 0
#Define number of sides
nosides = 24
#Define the outer length of the object
outlenght = 15
#Define the inner length of the object
inlenght = 8
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
turtle.left(90)
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
turtle.penup()
turtle.home()  
#Draw 2nd pattern
#reduce pattern size by half
nosides1 = nosides/2
outlenght1 = outlenght/2
inlenght1 = inlenght/2
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
        turtle.right(360/nosides1).
#Commit to changes

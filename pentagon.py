import turtle
turtle.Screen().bgcolor("black")
t=turtle.Turtle()
t.pencolor ("red") #we define the color of the pen to red
for i in range(8):
    t.forward(100) #we move the turtle forward by 100 units
    t.left(45)    #we turn the turtle 45 degrees to the left
    i=i+1

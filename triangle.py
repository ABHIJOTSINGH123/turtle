import turtle
t=turtle.Turtle()
t.pencolor ("red") 
turtle.Screen().bgcolor("black")
turtle.title("welcome to turtle window.")
board=turtle.Turtle()
t.hideturtle()
for i in range(3):
    t.forward(100)
    t.left(120)
    i=i+1
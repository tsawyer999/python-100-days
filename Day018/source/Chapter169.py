import turtle

draw = turtle.Turtle()

for _ in range(15):
    draw.forward(10)
    draw.penup()
    draw.forward(10)
    draw.pendown()

screen = turtle.Screen()
screen.exitonclick()

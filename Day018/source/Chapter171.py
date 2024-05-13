import turtle
import random

draw = turtle.Turtle()
draw.hideturtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 45, 90, 135, 180, 225, 270, 315]


def draw_random_lines(lines: int):
    previous_direction = 0
    direction = 0

    for _ in (range(lines)):
        turtle.color(random.choice(colors))
        turtle.forward(random.randint(30, 60))
        while direction == previous_direction:
            direction = random.choice(directions)
        turtle.setheading(direction)
        previous_direction = direction


def main() -> None:
    turtle.pensize(15)
    turtle.speed("fastest")

    draw_random_lines(200)

    screen = turtle.Screen()
    screen.exitonclick()


main()

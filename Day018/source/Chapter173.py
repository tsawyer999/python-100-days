import turtle
import random


draw = turtle.Turtle()
turtle.colormode(255)


def create_random_color() -> tuple[int, int, int]:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def draw_spirograph(angle: int) -> None:
    current_angle = angle
    number_of_angle = int(360 / angle)
    for _ in range(number_of_angle):
        draw.color(create_random_color())
        draw.circle(100)
        print(current_angle)
        draw.setheading(current_angle)
        current_angle += angle


def main() -> None:
    turtle.speed("fastest")

    draw_spirograph(5)

    screen = turtle.Screen()
    screen.exitonclick()



main()

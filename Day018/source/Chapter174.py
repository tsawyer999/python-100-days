# The image was from https://www.publicdomainpictures.net/en/view-image.php?image=75938&picture=candy-1
import random
import colorgram
import turtle
import copy


def get_colors() -> list[tuple[int, int, int]]:
    colors: list[tuple[int, int, int]] = []
    extracted_colors = colorgram.extract("../data/image.jpg", 50)
    for color in extracted_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        new_color = (r, g, b)
        colors.append(new_color)
    return colors


def draw_colors(input_colors: list[tuple[int, int, int]]) -> None:
    colors = copy.deepcopy(input_colors)
    turtle.colormode(255)
    draw = turtle.Turtle()
    draw.speed("fastest")
    draw.penup()
    draw.hideturtle()

    draw.setheading(225)
    draw.forward(250)
    draw.setheading(0)

    count = 0
    while len(colors) > 0:
        index = random.randint(0, len(colors) - 1)
        color = colors.pop(index)
        draw.dot(20, color)
        draw.forward(50)
        count += 1
        if count % 10 == 0:
            draw.setheading(90)
            draw.forward(50)
            draw.setheading(180)
            draw.forward(500)
            draw.setheading(0)


def main() -> None:
    colors = get_colors()
    draw_colors(colors)
    screen = turtle.Screen()
    screen.exitonclick()


main()

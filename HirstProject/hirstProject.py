from turtle import Turtle, Screen
import colorgram, random

turt = Turtle()
turt.speed("fastest")
turt.penup()
turt.hideturtle()
screen = Screen()
screen.colormode(255)

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = [(223, 231, 239), (237, 36, 110), (147, 25, 69), (214, 168, 52), (240, 73, 36), (9, 146, 93), (187, 160, 41), (26, 126, 193), (46, 190, 233), (252, 223, 0), (241, 219, 64), (124, 192, 82), (82, 21, 82), (187, 37, 102), (27, 171, 123), (218, 58, 24), (209, 131, 168)]

turt.setheading(225)
turt.forward(300)
turt.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turt.dot(20, random.choice(color_list))
    turt.forward(50)

    if dot_count % 10 == 0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)



screen.exitonclick()
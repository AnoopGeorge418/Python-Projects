# import colorgram
import random
import turtle as turtle_module

tim = turtle_module.Turtle()

# rgb_colors = []
# colors = colorgram.extract("./hrist spot.jpg", 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g   
#     b = color.rgb.b
#     new_color = (r, g, b)
    
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

turtle_module.colormode(255)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()

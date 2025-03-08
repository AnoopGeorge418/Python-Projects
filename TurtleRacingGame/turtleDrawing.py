from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forwards():
    turt.forward(10)

def move_backwards():
    turt.backward(10)

def turn_left():
    new_heading = turt.heading() + 10
    turt.setheading(new_heading)

def turn_right():
    new_heading = turt.heading() - 10
    turt.setheading(new_heading)

def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
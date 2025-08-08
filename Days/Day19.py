from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

def move_forward():
    leo.forward(10)

def move_backward():
    leo.backward(10)

def turn_left():
    new_heading = leo.heading()+10
    leo.setheading(new_heading)

def turn_right():
    new_heading = leo.heading()-10
    leo.setheading(new_heading)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(screen.clearscreen, "c")
screen.onkey(key="space", function=move_forward)
screen.exitonclick

import turtle as turtle_module
import random 

mike = turtle_module.Turtle()
mike.shape("classic")
mike.color("orange")
mike.speed("Fastest")
mike.pensize(15)
turtle_module.colormode(255)

def shape (num_sides):
    angle = 360 / num_sides
    for _ in (num_sides):
        mike. forward(100)
        mike.right(angle)

for shape_side_n in range (3, 11):
    mike.color(random.choice(color))

for _ in range(4):
    mike.forward(100),
    mike.right(90)
    
for _ in range(100):
    mike.forward(10)
    mike.penup()
    mike.forward(10)
    mike.pendown()

for _ in range(200):
    mike.




screen = Screen()
screen.exitonclick()
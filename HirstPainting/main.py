from turtle import Turtle, Screen
import colorgram
import random

hirst = Turtle()
my_screen = Screen()
my_screen.colormode(255)

cg_colors = colorgram.extract('hirst.jpg', 10)

def makeTurtleColorFromCGColor(cg_color):
    r = cg_color.rgb.r
    g = cg_color.rgb.g
    b = cg_color.rgb.b
    return r, g, b


colors = []
for cg_color in cg_colors:
    colors.append(makeTurtleColorFromCGColor(cg_color))


horizontal_size = 500
vertical_size = 250

num_dot_rows = 5
num_dot_columns = 5

hirst.penup()
hirst.hideturtle()
hirst.setposition(0 - (horizontal_size/2), 0 - (vertical_size/2))

for i in range(num_dot_rows):
    for j in range(num_dot_columns):
        hirst.dot(5, random.choice(colors))
        hirst.setposition(hirst.position()[0] + (horizontal_size/num_dot_columns), hirst.position()[1])
    hirst.setposition(0 - (horizontal_size/2), 0 - (vertical_size/2))
    hirst.setposition(hirst.position()[0], hirst.position()[1] + (vertical_size/num_dot_rows) * (i + 1))


my_screen.exitonclick()
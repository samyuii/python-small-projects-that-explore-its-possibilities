import turtle
import random

# turtle screen
turtle.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()

# function to draw a random line
def draw_random_line():
    x1 = random.randint(-200, 200)
    y1 = random.randint(-200, 200)
    x2 = random.randint(-200, 200)
    y2 = random.randint(-200, 200)

    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(random.random(), random.random(), random.random())
    turtle.width(random.randint(1, 5))
    turtle.goto(x2, y2)

num_lines = 50
for _ in range(num_lines):
    draw_random_line()

turtle.done()

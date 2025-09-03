import turtle
import math
import sys


# Inward Koch Polygon Fractal Program

# This program draws a polygon and replaces the middle part of each side with a "dent" that points inward.
# The dent is an equilateral triangle shape. We do this recursively (fractal) so the sides get more detailed.



# function to draw one fractal edge pointing inward
def draw_inward_koch_segment(t, length, depth):
    if depth == 0:   # base case: just draw a straight line
        t.forward(length)
    else:
        # divide the edge into 3 smaller parts
        segment = length / 3.0

        draw_inward_koch_segment(t, segment, depth - 1)

        # make a "dent" inward
        t.left(60)
        draw_inward_koch_segment(t, segment, depth - 1)
        t.right(120)
        draw_inward_koch_segment(t, segment, depth - 1)
        t.left(60)

        draw_inward_koch_segment(t, segment, depth - 1)


# function to draw a polygon with inward koch edges
def draw_polygon_with_inward_koch_edges(t, sides, side_length, depth):
    # apothem = distance from center to side, helps center the shape
    apothem = side_length / (2.0 * math.tan(math.pi / sides))

    # move turtle near the center so drawing looks centered
    t.penup()
    t.goto(-side_length / 2.0, -apothem)
    t.setheading(0)
    t.pendown()

    # turn angle for polygon
    turn = 360 / sides

    # draw each side with fractal rule
    for _ in range(sides):
        draw_inward_koch_segment(t, side_length, depth)
        t.left(turn)


# -------------------------------
# Program starts here
# -------------------------------

print("Inward Koch Polygon Fractal")
print("This makes shapes like crosses when recursion is higher!\n")

# -------------------------------
# Get user input safely
# -------------------------------

# number of sides
while True:
    try:
        sides = int(input("Enter number of sides (>=3): "))
        if sides < 3:
            print("Polygon must have at least 3 sides!")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

# side length
while True:
    try:
        length = float(input("Enter side length in pixels (>0): "))
        if length <= 0:
            print("Side length must be greater than 0!")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# recursion depth
while True:
    try:
        depth = int(input("Enter recursion depth (>=0, recommended 0-6): "))
        if depth < 0:
            print("Depth cannot be negative!")
            continue
        if depth > 7:
            print("Depth too high, setting to 7 (to avoid freezing).")
            depth = 7
        break
    except ValueError:
        print("Please enter a valid integer.")

# -------------------------------
# Setup turtle screen
# -------------------------------
try:
    screen = turtle.Screen()
    screen.title("Inward Koch Polygon Fractal")
    screen.bgcolor("white")

    # make turtle
    t = turtle.Turtle()
    t.speed(0)        
    t.hideturtle()    
    t.pensize(1)
    t.color("black")

    # draw fractal polygon
    draw_polygon_with_inward_koch_edges(t, sides, length, depth)

    print("Done! Click the window to close.")
    screen.exitonclick()

except turtle.Terminator:
    print("Turtle graphics window closed unexpectedly.")
    sys.exit(1)

except RecursionError:
    print("Error: Recursion depth too high for Python.")
    sys.exit(1)

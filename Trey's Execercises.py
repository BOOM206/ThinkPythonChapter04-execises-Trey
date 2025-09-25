import turtle
import math
from turtle import penup, pendown


def jump(length):
    """Move forward length units without leaving a trail.

    Postcondition: Leaves the pen down.
    """
    penup()
    turtle.forward(length)
    pendown()
""" Makes a rectangle, as name says """
def rectangle2(length, width):
    """length: How long the rectangle should be.
        width: How long the rectangle should be."""

    parallelogram(length, width,90,90)

def rhombus(side_length, angle1, angle2):
    parallelogram(side_length, side_length, angle1, angle2)

def parallelogram(side1_length, side2_length, angle1, angle2):
    for i in range(2):
        turtle.forward(side1_length)
        turtle.left(angle1)
        turtle.forward(side2_length)
        turtle.left(180 - angle2)
def triangle (point1, point2, point3):
    turtle.forward(point1)  # Move forward 100 units
    turtle.left(120)  # Turn left 120 degrees
    turtle.forward(point2)  # Move forward 100 units
    turtle.left(120)  # Turn left 120 degrees
    turtle.forward(point3)
def triforce(side1, side2, side3):
    for i in range(3):
        triangle(side1, side2, side3)
def line(A,Length, angle):
    for i in range(A):
        turtle.forward(Length)
        turtle.left(angle)
def pie (n, point1, point2, point3):
    base_angle = 90 - 180 / n  # The base angle of the isosceles triangle
    center_angle = 2 * base_angle  # The center angle of the triangle in the center of the polygon
    for i in range(n):  # Loop on the number of sides/triangles we need to create.
        triangle(point1, point2, point3)  # Draw a triangle
        turtle.left(180 - center_angle)  # Turn turtle to location for next triangle
def arc (radius, angle):
    arc_length = 2 * math.pi * radius
    n = 30
    length = arc_length / n
    step_angle = angle / n
    line(n, length, step_angle)

#parallelogram(150,80, 70, 70)
#rectangle2(200,100)
#rhombus(50, 60, 60)
#triangle(100,100,100)
#pie(2,100,100,100)
#pie(2,100,100,100)
#pie(2,100,100,100)
#stolen_triangle(180, 60)
arc(50,90)
turtle.done()
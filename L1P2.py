#PROBLEM 2

import turtle


def draw_poly(t, n, sz):

    """Make turtle t draw a poly of n sides with sz units per side."""

    t.down()

    for i in range(n):

        t.forward(sz)

        t.left(360/n)

    return
#first function


wn = turtle.Screen()
#Set up the window and its attributes

wn.bgcolor("lightgreen")

wn.title("Problem 2")

tess = turtle.Turtle()
#Create a turtle

tess.color("pink")

draw_poly(tess, 8, 50)
#Call the function to draw the poly

wn.mainloop()

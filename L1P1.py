#PROBLEM 1

import turtle


def draw_square(t, sz):

    """Make turtle t draw a square of sz."""

    t.down()

    for i in range(4):

        t.forward(sz)

        t.left(90)

    return
#first function


def jump_square(t, sz):

    """Make turtle t draw a square of sz."""

    t.up()

    t.right(180)

    t.forward(sz/2)

    t.left(90)

    t.forward(sz/2)

    t.left(90)

    return
#second function


wn = turtle.Screen()
#Set up the window and its attributes

wn.bgcolor("lightgreen")

wn.title("Problem 1")

some_turtle = turtle.Turtle()
#Create a turtle

some_turtle.color("pink")

for j in range(5):

    print(j)

    draw_square(some_turtle, (j+1)*20)
    # Call the function to draw the square

    jump_square(some_turtle, 20)
        # Call the function to jump for the next square


wn.mainloop()

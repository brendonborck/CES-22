import turtle # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 2
state_timer = 1
#holds the current state of the color screen to change if it needs
step = 5
#size of each step taken by turtle

def advance_state_machine():
    global state_num
    global state_timer
    if state_num == 0: # Transition from state 0 to state 1
        state_num = 1
        tess.forward(70)
        tess.fillcolor("orange")
    elif state_num == 1: # Transition from state 1 to state 2
        state_num = 2
        tess.forward(70)
        tess.fillcolor("red")
    else: # Transition from state 2 to state 0
        state_num = 0
        tess.back(140)
        tess.fillcolor("green")
    if state_timer == 0:
        wn.ontimer(advance_state_machine, 250)


def color_red():
    tess.fillcolor("red")


def color_green():
    tess.fillcolor("green")


def color_blue():
    tess.fillcolor("blue")


def increase_width():
    if tess.pensize() < 20:
        tess.pensize(tess.pensize() + 1)


def decrease_width():
    if tess.pensize() > 1:
        tess.pensize(tess.pensize() - 1)


def move_right():
    tess.setheading(0)
    tess.forward(step)


def move_left():
    tess.setheading(180)
    tess.forward(step)


def move_up():
    tess.setheading(90)
    tess.forward(step)


def move_down():
    tess.setheading(270)
    tess.forward(step)


def out_of_traffic_light():
    tess.setpos(-30,-30)


def draw_square():
    tess.setheading(0)
    tess.down()
    for i in range(4):
        tess.forward(50)
        tess.right(90)
    tess.up()


def traffic_light():
    global state_num
    state_num = 2
    tess.shapesize(3)
    tess.up()
    tess.setheading(90)
    tess.setpos(40,50)


def pencil_up():
    tess.up()


def pencil_down():
    tess.down()


def tess_fast():
    global step
    if step < 40:
        step += 5


def tess_slow():
    global step
    if step > 5:
        step -= 5


def timer_pause():
    global state_timer
    state_timer = 1


def timer_resume():
    global state_timer
    if state_timer == 0:
        return
    state_timer = 0
    if state_num == 0:
        tess.setpos(40,120)
    elif state_num == 1:
        tess.setpos(40,50)
    else:
        tess.setpos(40,190)
    wn.ontimer(advance_state_machine, 10)

advance_state_machine
#Handle some other keys....... attributes of tess and window


# Bind the event handler to the space key.

wn.onkey(color_red, "r")
wn.onkey(color_green, "g")
wn.onkey(color_blue, "b")

wn.onkey(increase_width, "plus")
wn.onkey(decrease_width, "minus")

wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

wn.onkey(out_of_traffic_light, "o")
wn.onkey(draw_square, "q")
wn.onkey(traffic_light, "t")

wn.onkey(pencil_up, "u")
wn.onkey(pencil_down, "d")

wn.onkey(tess_fast, "f")
wn.onkey(tess_slow, "s")

wn.onkey(timer_pause, "p")
wn.onkey(timer_resume, "space")

wn.listen() # Listen for events
wn.mainloop()
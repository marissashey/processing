import turtle


t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#D07A7A")
t.color("#E6E3E3")
t.speed(0)

# frame
t.penup()
t.goto(-300, -200)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(600)
    t.left(90)
    t.forward(500)
    t.left(90)
t.end_fill()

# L knob
t.penup()
t.goto(-300, -250)
t.pendown()
t.begin_fill()
for i in range(36):
    t.forward(5)
    t.right(10)
t.end_fill()

# R knob
t.penup()
t.goto(300, -250)
t.pendown()
t.begin_fill()
for i in range(36):
    t.forward(5)
    t.right(10)
t.end_fill()

move_speed = 10
turn_speed = 10

e = turtle.Turtle()


# movement methods
def move_forward():
    e.pendown()
    e.forward(move_speed)


def move_backward():

    e.pendown()
    e.backward(move_speed)


def turn_left():
    e.left(turn_speed)


def turn_right():
    e.right(turn_speed)


def reset():
    e.reset()


# screen state
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(reset, "space")
screen.listen()
turtle.mainloop()

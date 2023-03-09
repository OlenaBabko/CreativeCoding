import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
t.color('white')
t.pensize(3)
t.penup()
t.goto(-300, -280)
t.pendown()

def illustration():
    for x in range(30):
        t.forward(7)
        t.left(5)
    for x in range(18):
        t.forward(10)
        t.right(9)
    t.right(180)
    for y in range(18):
        t.forward(10)
        t.left(5)
    for y in range(30):
        t.forward(7)
        t.right(9)
    t.right(180)
    t.left(9)

t.begin_fill()
for i in range(40):
    illustration()
t.fillcolor('black')
t.end_fill()


tt = turtle.Turtle()
turtle.bgcolor('black')
tt.speed(0)
tt.color('white')
tt.pensize(1)


def illustration_2():
    tt.penup()
    tt.goto(200, 100)
    tt.pendown()
    for x in range(30):
        tt.forward(7)
        tt.left(5)
    for x in range(18):
        tt.forward(10)
        tt.right(5)
    tt.right(180)
    for y in range(18):
        tt.forward(12)
        tt.left(3)
    for y in range(30):
        tt.forward(7)
        tt.right(5)
    tt.right(180)
    tt.left(9)

tt.begin_fill()
for i in range(40):
    illustration_2()
tt.fillcolor('black')
tt.end_fill()

turtle.done()
import turtle
import canvasvg
from PIL import Image

t = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor('black')
t.speed(0)

radius = 60
t.pensize(2)
color = ['red', 'yellow', 'purple', 'blue', 'green']
for x in range(12):

    t.color(color[1])
    for i in range(6):
        t.circle(radius)
        t.right(30)
    radius = radius + 4

    t.color(color[3])
    for i in range(6):
        t.circle(radius)
        t.right(30)
    radius = radius + 4

#turtle.done()
#auto save command:
#scr.mainloop()


canvas = scr.getcanvas()
canvasvg.saveall("result.svg", canvas)
im = Image.open("result.svg")
im.save("result.png", "png")
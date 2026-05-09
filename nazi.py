#educational purposes only
import turtle as t

t.speed(10)
t.penup()
t.goto(-125, -75)                           #red rectangle (250x150)
t.color("red")
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(250)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()
t.penup()

t.goto(0, -56.25)                           #white circle (radius = 56.25)
t.color("white")
t.pendown()
t.begin_fill()
t.circle(56.25)
t.end_fill()
t.penup()

t.goto(0, -35.15625 * (2**0.5))             #nazi swastika
t.left(45)
t.color("black")
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(42.1875)
    t.left(90)
    t.forward(28.125)
    t.right(90)
    t.forward(14.0625)
    t.right(90)
    t.forward(28.125)
    t.left(90)
    t.forward(14.0625)
    t.left(90)
t.end_fill()
t.hideturtle()
t.done()
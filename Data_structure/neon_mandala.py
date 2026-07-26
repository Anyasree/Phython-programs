import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]
for i in range(80):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 3)
    t.right(59)
t. penup
t. goto(0, 0)
t. setheading(90)
t. pendown()
t. fillcolor("gold")
t. pencolor("gold")
t. begin_fill()
for i in range(5):
    t.forward(100)
    t. right(144)
t. end_fill()
t. penup()
t.goto(0, -120)
t.pendown()
petal_colors = [
    "red", "orange", "yellow", "green",
    "cyan", "blue", "purple", "pink"
]
for i in range(36):
    t. fillcolor (petal_colors[i % len(petal_colors) ])
    t. begin_fill()
    t. circle(40,60)
    t. left (120)
    t. circle(40,60)
    t.left(120)
    t.end_fill()
    t.right(10)
t.hideturtle()
turtle.done()

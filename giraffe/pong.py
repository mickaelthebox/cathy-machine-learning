import turtle

wn = turtle.Screen()
wn.title("my first pong")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Barre 1
Barre_a=turtle.Turtle()
Barre_a.speed(0)
Barre_a.shape("square")
Barre_a.color("black")
Barre_a.shapesize(stretch_wid=5 , stretch_len=1)
Barre_a.penup()
Barre_a.goto(-350 ,0)

# Barre 2
Barre_b=turtle.Turtle()
Barre_b.speed(0)
Barre_b.shape("square")
Barre_b.color("black")
Barre_b.shapesize(stretch_wid=5 , stretch_len=1)
Barre_b.penup()
Barre_b.goto(350 ,0)

# Ball
Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.penup()
Ball.goto(0,0)

#Fontions
def Barre_a_up():
    y= Barre_a.ycor()
    y += 20
    Barre_a.sety(y)

def Barre_a_down():
    y=Barre_a.ycor()
    y -= 20
    Barre_a.sety(y)

def Barre_b_up():
    y=Barre_b.ycor()
    y += 20
    Barre_b.sety(y)

def Barre_b_down():
    y=Barre_b.ycor()
    y -= 20
    Barre_b.sety(y)


# Clavier
wn.listen()
wn.onkeypress(Barre_a_up, "a")

wn.listen()
wn.onkeypress(Barre_a_down, "z")

wn.listen()
wn.onkeypress(Barre_b_up, "i")

wn.listen()
wn.onkeypress(Barre_b_down, "o")
# Main game loop
while True:
    wn.update()
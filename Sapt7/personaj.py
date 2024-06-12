import turtle as t

def deseneaza_urechi():
    t.penup()
    t.goto(-50, 100)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10, steps=3)
    t.end_fill()

    t.penup()
    t.goto(50, 100)
    t.pendown()
    t.begin_fill()
    t.circle(10, steps=3)
    t.end_fill()

def deseneaza_obrazi():
    t.penup()
    t.goto(-35, 50)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(35, 50)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def deseneaza_ochi():
    t.penup()
    t.goto(-20, 70)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.penup()
    t.goto(20, 70)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

def deseneaza_gura():
    t.penup()
    t.goto(-10, 50)
    t.pendown()
    t.right(90)
    t.circle(10, 180)
    t.left(90)

def deseneaza_cap_si_corp():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.begin_fill()
    t.circle(80)
    t.end_fill()

def deseneaza_pikachu():
    t.speed(3)
    deseneaza_cap_si_corp()
    deseneaza_urechi()
    deseneaza_ochi()
    deseneaza_obrazi()
    deseneaza_gura()
    t.hideturtle()

# Configurare fereastră
t.bgcolor("white")
t.title("Desen Pikachu cu Turtle")

# Desenează Pikachu
deseneaza_pikachu()

# Păstrează fereastra deschisă
t.done()

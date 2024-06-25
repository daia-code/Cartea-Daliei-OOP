import turtle
import random

# Setări inițiale
screen = turtle.Screen()
screen.title("Joc cu Turtle - Colectează steluțe!")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Crearea țestoasei jucător
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.speed(0)
player.goto(0, -250)

# Crearea listei pentru steluțe
stars = []

# Variabilă pentru puncte
points = 0

# Crearea turtle pentru afișarea punctelor
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(0, 260)

# Funcție pentru a actualiza punctajul pe ecran
def update_score():
    score_turtle.clear()
    score_turtle.write(f"Puncte: {points}", align="center", font=("Courier", 24, "normal"))

# Funcție pentru a crea steluțe noi
def create_star():
    star = turtle.Turtle()
    star.shape("circle")
    star.color("yellow")
    star.penup()
    star.speed(0)
    x = random.randint(-280, 280)
    y = random.randint(100, 250)
    star.goto(x, y)
    stars.append(star)

# Funcție pentru a distruge o steluță și a actualiza punctajul
def destroy_star(star):
 
    star.hideturtle()
    stars.remove(star)

# Verificarea coliziunii între jucător și steluțe
def check_collision():
    for star in stars:
        if star.distance(player) < 20:
            global points
            destroy_star(star)
            points += 1
            update_score()

            return True
    return False

# Crearea funcțiilor de mișcare pentru jucător
def move_left():
    x = player.xcor()
    x -= 15
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 15
    if x > 280:
        x = 280
    player.setx(x)

# Asocierea funcțiilor de mișcare la tastele săgeată
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Bucla principală a jocului
while True:
    screen.update()

    # Crearea unei steluțe noi la fiecare 30 de cadre
    if random.randint(1, 30) == 1:
        create_star()

    # Verificarea coliziunii doar atunci când jucătorul se mișcă
    if check_collision():
        update_score()

    # Mișcarea steluțelor existente
    for star in stars:
        y = star.ycor()
        y -= 1
        star.sety(y)

        # Verificarea ieșirii steluțelor din ecran
        if star.ycor() < -280:
            destroy_star(star)

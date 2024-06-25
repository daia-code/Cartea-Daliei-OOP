import turtle

# Setări inițiale
screen = turtle.Screen()
screen.title("Pac-Man cu Turtle")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Variabile pentru dimensiunea labirintului
GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30

# Labirintul (0 = spațiu gol, 1 = perete)
level = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X............XX............X.X",
    "X.XXXX.XXXXX.XX.XXXXX.XXXX.X.X",
    "X.XXXX.XXXXX.XX.XXXXX.XXXX.X.X",
    "X.XXXX.XXXXX.XX.XXXXX.XXXX.X.X",
    "X..........................X.X",
    "X.XXXX.XX.XXXXXXXXXX.XX.XXXX.X",
    "X.XXXX.XX.XXXXXXXXXX.XX.XXXX.X",
    "X......XX....XX....XX......X.X",
    "XXXXXX.XXXXX XX XXXX.XXXXXXXX",
    "     X.XXXXX XX XXXX.X      ",
    "     X.XX          XX.X      ",
    "     X.XX XXXXXXXX XX.X      ",
    "XXXXXX.XX X      X XX.XXXXXXX",
    "      .   X      X   .       ",
    "XXXXXX.XX X      X XX.XXXXXXX",
    "     X.XX XXXXXXXX XX.X      ",
    "     X.XX          XX.X      ",
    "     X.XXXXXXXXXXXX XX.X      ",
    "XXXXXX................XXXXXXX",
    "X......XX.XXXXXXXXXX.XX......X",
    "X.XXXX.XX.XXXXXXXXXX.XX.XXXX.X",
    "X.XXXX.XX............XX.XXXX.X",
    "X.XXXX.XXXXXXXXXXXXXXXX.XXXX.X",
    "X..........................X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Crearea labirintului
def draw_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            char = level[y][x]
            screen_x = -290 + x * GRID_SIZE
            screen_y = 290 - y * GRID_SIZE
            
            if char == "X":
                draw_box(screen_x, screen_y)

def draw_box(x, y):
    box = turtle.Turtle()
    box.speed(0)
    box.shape("square")
    box.color("blue")
    box.penup()
    box.goto(x, y)
    box.stamp()
    box.hideturtle()

# Inițializarea labirintului
draw_level(level)

# Crearea lui Pac-Man
pacman = turtle.Turtle()
pacman.shape("triangle")
pacman.color("yellow")
pacman.penup()
pacman.speed(0)
pacman.goto(-280, 280)  # Poziția de start a lui Pac-Man

# Funcții pentru mișcarea lui Pac-Man
def move_up():
    if is_valid_move(pacman.xcor(), pacman.ycor() + GRID_SIZE):
        pacman.setheading(90)
        pacman.goto(pacman.xcor(), pacman.ycor() + GRID_SIZE)

def move_down():
    if is_valid_move(pacman.xcor(), pacman.ycor() - GRID_SIZE):
        pacman.setheading(270)
        pacman.goto(pacman.xcor(), pacman.ycor() - GRID_SIZE)

def move_left():
    if is_valid_move(pacman.xcor() - GRID_SIZE, pacman.ycor()):
        pacman.setheading(180)
        pacman.goto(pacman.xcor() - GRID_SIZE, pacman.ycor())

def move_right():
    if is_valid_move(pacman.xcor() + GRID_SIZE, pacman.ycor()):
        pacman.setheading(0)
        pacman.goto(pacman.xcor() + GRID_SIZE, pacman.ycor())

def is_valid_move(x, y):
    grid_x = int((x + 300) / GRID_SIZE)
    grid_y = int((-y + 300) / GRID_SIZE)
    return level[grid_y][grid_x] == "." or level[grid_y][grid_x] == " "

# Asocierea mișcărilor lui Pac-Man la tastatură
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Activarea urmăririi ecranului
screen.tracer(1)

# Menținerea ferestrei deschise
turtle.done()

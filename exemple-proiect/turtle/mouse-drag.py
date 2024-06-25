import turtle

# Funcții pentru controlul țestoasei cu tastele săgeată
def move_up():
    turtle.setheading(90)  # Orientare în sus
    turtle.forward(10)

def move_down():
    turtle.setheading(270)  # Orientare în jos
    turtle.forward(10)

def move_left():
    turtle.setheading(180)  # Orientare la stânga
    turtle.forward(10)

def move_right():
    turtle.setheading(0)  # Orientare la dreapta
    turtle.forward(10)

def main():
    turtle.speed(0)  # Viteză maximă
    turtle.shape('turtle')
    turtle.color('blue')

    # Asociem funcțiile de mișcare la tastele săgeată
    turtle.onkey(move_up, 'Up')
    turtle.onkey(move_down, 'Down')
    turtle.onkey(move_left, 'Left')
    turtle.onkey(move_right, 'Right')

    # Ascultăm evenimentele de la tastatură
    turtle.listen()
    turtle.mainloop()

if __name__ == "__main__":
    main()

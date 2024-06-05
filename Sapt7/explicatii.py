# EXEMPLU COD : Cerc

import turtle

creion = turtle.Turtle()

creion.circle(100) # s-a ales raza de 100 pixeli

turtle.mainloop()

# EXEMPLU COD : Pătrat

import turtle

creion = turtle.Turtle()

for _ in range(4):

  creion.circle(100, 90)

  creion.backward(100)

turtle.mainloop()

# EXEMPLU COD : Triunghi

import turtle

creion = turtle.Turtle()

for i in range(3):

    turtle.forward(100)

    turtle.left(180)

    turtle.right(60)

turtle.mainloop()


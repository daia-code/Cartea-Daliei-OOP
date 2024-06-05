'''
Citiți o lungime de la tastatură și desenați o linie de acea lungime 
(veți alege voi în ce direcție sa fie dintre: sus, jos, stânga, dreapta)

'''

import turtle

wn = turtle.Screen()
wn.bgcolor("white")

linie = turtle.Turtle()

linie.speed(1)

lungime = int(input("Introduceți lungimea liniei: "))

linie.left(90)

linie.forward(lungime)

turtle.mainloop()
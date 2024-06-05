'''
Citiți de la tastatură o valoare care reprezintă un unghi și o altă valoare
 ce reprezintă distanța Desenați o linie în direcția dată de unghi și 
 lungimea dată de distanță.
 Putem folosi un unghi negativ ? 
'''

import turtle

wn = turtle.Screen()

wn.bgcolor("white")

linie = turtle.Turtle()

linie.speed(1)

unghi = int(input("Introduceți unghiul: "))

distanta = int(input("Introduceți distanța: "))

linie.left(unghi)

linie.forward(distanta)

turtle.mainloop()
'''
CONCEPT : goto

EXPLICAȚIE : Desenează o linie din poziția în care se afla săgeata pana în poziția în care ii spunem noi.

Pentru a înțelege ce e poziția definim următoarele concepte:

    origine: centrul ferestrei în care se desenează (poziția (0,0))

    axa X: deplasare pe orizontală (de la origine la dreapta avem valori pozitive, de la origine la stânga avem valori negative)

    axa Y: deplasare pe verticală (de la origine în sus avem valori pozitive, de la origine în jos avem valori negative)

Astfel, o poziție oarecare de pe ecran are o coordonata X (pe axa X) și o coordonata Y (pe axa Y).
'''


# EXEMPLU COD : 

import turtle

creion = turtle.Turtle()

creion.goto(200,100)

turtle.mainloop()

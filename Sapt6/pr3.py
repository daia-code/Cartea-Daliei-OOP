'''
Scrieți un script în care putem roti săgeata care reprezintă creionul 
cu câte un grad în continuu. Schimbați direcția.
 Ce se întâmplă dacă schimbați unghiul.
'''

import turtle

wn = turtle.Screen()

wn.bgcolor("white")

creion = turtle.Turtle()

creion.speed(0)


# Citiți direcția de rotație de la tastatură

directie = input("Introduceți direcția de rotație (stânga/dreapta): ").lower()


# Verificați dacă direcția introdusă este validă

if directie not in ['stânga', 'dreapta']:

    print("Direcția introdusă nu este validă. Încercați din nou.")

    wn.bye()

    exit()


# Rotiți creionul în direcția aleasă în mod continuu

while True:

    if directie == "stânga":

        creion.left(1)

    else:

        creion.right(1)

turtle.mainloop()

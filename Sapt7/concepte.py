'''
CONCEPT : onscreenclick

EXPLICAȚIE : Ne oferă posibilitatea să executăm cod doar atunci când dăm click pe ecran.

'''

# EXEMPLU COD : 

# imaginea trebuie sa fie de tip GIF

import turtle

# cream functia pe care o vom apela cand se da click

def afiseaza(x, y):

  creion.goto(x, y)

ecran = turtle.Screen()

creion = turtle.Turtle()

ecran.onscreenclick(afiseaza)

turtle.mainloop()

'''
CONCEPT : onkeypress() and listen()

EXPLICAȚIE : onkeypres face același lucru ca și onscreenclick doar cu taste de la tastatura în loc de click din maus.

listen ne permite să ascutăm pentru a observa când sunt apăsate anumite taste.

'''

# EXEMPLU COD : 

import turtle

ecran = turtle.Screen()

creion = turtle.Turtle()

turtle.onkeypress(creion.forward, 'd')

turtle.onkeypress(creion.backward, 'a')

turtle.listen()


turtle.mainloop()

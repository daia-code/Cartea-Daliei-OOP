CONCEPT : shape

EXPLICAȚIE : Ne oferă posibilitatea să modificăm cursorul cu altă formă la alegere dintre:

    sageată ('arrow' - default)

    testoasă('turtle')

    cerc ('circle')

    patrat('square')

    triunghi('triangle')

    clasic('classic' - tot sageata)


# EXEMPLU COD : 

#incercati si alte forme ale cursorului

import turtle

creion = turtle.Turtle()

creion.shape('turtle')

for i in range(4):

    creion.forward(100)

    creion.left(90)

from turtle import *

def mystere(a, b, c):
    # a : nb tours
    # b : espacement de base
    # c : augmentation de la spirale
    cote = b
    for i in range(2*a):
        forward(cote)
        left(90)
        forward(cote)
        left(90)
        cote = cote + c

def triangle_spirale(a, b, c):
    # a : nb tours
    # b : espacement de base
    # c : augmentation de la spirale
    cote = b
    for i in range(3*a):
        forward(cote)
        left(120)
        cote = cote + c

triangle_spirale(4, 20, 30)
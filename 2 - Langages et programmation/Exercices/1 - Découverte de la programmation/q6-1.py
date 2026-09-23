from turtle import *

def carre(cote):
    # Dessiner un carré de côté cote
    for i in range(4):
        forward(cote)
        left(90)
   
def fleur(taille, nb_carres):
    for a in range(nb_carres):
        carre(taille)
        left(360/nb_carres)

fleur(20, 8)

done()
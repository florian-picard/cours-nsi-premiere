objets = ["pomme", "ananas", "prune"]
quantite = [3, 1, 6]
prix = [100, 500, 50]

def prix_total(quantites, prix):
    """ [int], [int] -> int
    longueur(quantites) = longueur(prix)
    Renvoie le prix total d'un panier """
    montant_caisse = 0
    for i in range(len(quantite)):
        quantite_objet = quantite[i]
        prix_objet = prix[i]
        montant_caisse = montant_caisse + prix_objet*quantite_objet
    return montant_caisse

assert prix_total(quantite, prix) == 1100
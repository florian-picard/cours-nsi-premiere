from q2 import longueur

def plus_long_mot(liste_mots):
    """ [str] -> int
    Renvoie le nombre de lettres du plus long mot de la liste """
    record = 0
    for m in liste_mots:
        n = longueur(m)
        if n > record:
            record = n
    return record

def mot_plus_long(liste_mots):
    """ [str] -> str """
    record = 0
    mot_plus_long = ""
    for m in liste_mots:
        n = longueur(m)
        if n > record:
            record = n
            mot_plus_long = m
    return mot_plus_long

assert plus_long_mot(["vive", "la", "nsi!!!"]) == 6
assert mot_plus_long(["vive", "la", "nsi!!!"]) == "nsi!!!"
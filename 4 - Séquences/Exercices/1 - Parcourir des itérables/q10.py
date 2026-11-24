mois = ["Janvier", "Février", "Mars",
        "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre",
        "Octobre", "Novembre", "Décembre"]
temperatures = [24.8, 25.8, 25.7, 25.2,
                24.9, 23.9,23.3, 23.2,
                23.7, 24.1, 24.5, 24.4]

# print(mois[4])
# print(mois[len(mois) - 1])

# for i in range(len(mois)):
#     e = mois[i]
#    print(i, e)
    
def premier_mois_sous24(temperatures):
    """ [float] -> int
    Renvoie l'indice du premier mois dont la température mensuelle moyenne
    est inférieure à 24C.,
    Renvoie -1 si aucun mois ne possède une température mensuelle moyenne
    inférieure à 24C. """
    for i in range(len(temperatures)):
        t = temperatures[i]
        if t < 24:
            return i
    return -1

def premier_mois_sous(temperatures, seuil):
    for i in range(len(temperatures)):
        t = temperatures[i]
        m = mois[i]
        if t < seuil:
            return m
    return ""

def mois_plus_chaud(temp):
    indice = 0
    record = temp[0]
    for i in range(len(temp)):
        t = temp[i]
        if t > record:
            record = t
            indice = i
    return mois[indice]
        
print(mois_plus_chaud(temperatures))


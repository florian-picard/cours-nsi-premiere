tab1 = [1, 3, 2, 4, 5, 6]
tab2 = [1, 2, 3, 4, 5, 6]

def est_trie(tab):
    
    for i in range(len(tab)-1):
        # l'élément d'indice i
        # est plus grand que l'élément
        # d'indice i + 1
        if tab[i] > tab[i + 1]:
            return False
    return True


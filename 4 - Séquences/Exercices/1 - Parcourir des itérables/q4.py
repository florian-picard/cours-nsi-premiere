def nombre_occurences(iterable, elem):
    compte = 0
    for e in iterable:
        if e == elem:
            compte = compte + 1
    return compte
        
assert nombre_occurences([1, 2, 1, 1, 2, 1], 1) == 4
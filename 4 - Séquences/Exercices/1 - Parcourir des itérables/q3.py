def appartient(iterable, elem):
    for e in iterable:
        if elem == e:
            return True
    return False
        

iterable = [2, 3, 4]    
elem = 4
appartient(iterable, elem)
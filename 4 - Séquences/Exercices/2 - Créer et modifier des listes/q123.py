# notes = [9, 11, 15]
# notes[0]
# notes[0] = 10
# print(notes)

# notes = (9, 11, 15)
# notes[0]
# notes[0] = 10
# print(notes)

# lst = []
# lst.append(2)
# lst.append(4)
# lst.append(8)
# print(lst)
# e = lst.pop()
# print(e, lst)

lst = []
for x in range(-5, 5):
    if x**2 - 4 == 0:
        lst.append(x)

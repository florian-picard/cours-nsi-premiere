notes = [16.5, 9.9, 6.4, 7.8, 11.7, 15.4]
notes_interro = [8, 7, 9, 6, 10, 10, 9]

notes[2] = 16.4
def double_notes(notes):
    """ [float] -> None """
    for i in range(len(notes)):
        notes[i] = notes[i] * 2
    return None

double_notes(notes_interro)
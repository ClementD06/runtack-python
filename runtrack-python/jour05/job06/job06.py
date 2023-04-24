def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        elif note >= 40 and note < 100:
            multiple = (note // 5) * 5
            if multiple + 5 - note < 3:
                arrondies.append(multiple + 5)
            else:
                arrondies.append(note)
        else:
            arrondies.append(note)
    return arrondies
notes = [78, 82, 85, 36, 92, 40, 100]
arrondies = arrondir_notes(notes)
print(arrondies)
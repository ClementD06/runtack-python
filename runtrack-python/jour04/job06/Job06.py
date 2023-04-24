
L = [2, 4, 8, 16, 32]
print("Affichage à l'endroit :", (L))
def liste():
    temp = L[0]
    L[0] = L[-1]
    L[-1] = temp
    print("Affichage a l'envers :", (L))
liste()

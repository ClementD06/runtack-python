def changer_mot(mot):
    # Vérifier que le mot ne contient que des lettres de l'alphabet
    if not mot.isalpha():
        print("Erreur : le mot doit contenir uniquement des lettres de l'alphabet.")
        return mot
    
    # Transformer le mot en une liste de lettres
    lettres = list(mot)
    
    # Trouver la première paire de lettres consécutives dans l'ordre décroissant
    for i in range(len(lettres)-2, -1, -1):
        if lettres[i] < lettres[i+1]:
            # Trouver la lettre suivante la plus proche dans l'ordre alphabétique
            lettre_suivante = min(lettres[j] for j in range(i+1, len(lettres)) if lettres[j] > lettres[i])
            # Échanger les deux lettres
            j = lettres.index(lettre_suivante)
            lettres[i], lettres[j] = lettres[j], lettres[i]
            # Trier les lettres suivantes dans l'ordre croissant
            lettres[i+1:] = sorted(lettres[i+1:])
            # Retourner le nouveau mot
            return ''.join(lettres)
    
    # Si le mot est déjà le dernier possible dans l'ordre alphabétique, le retourner tel quel
    return mot
mot = input("Entrez un mot : ")
nouveau_mot = changer_mot(mot)
print("Le nouveau mot est :", nouveau_mot)
def dessiner_tapis(taille):
    # Dessiner les lignes du tapis
    for i in range(taille + 1):
        # dessiner la diagonale
        if i == taille // 2:
            print('\\' + '-' * (taille - 2) + '\\')
        else:
            print('|' + 'X' * taille + '|')

    # Dessiner la dernière ligne
    print('-' * (taille + 1))
dessiner_tapis(10)
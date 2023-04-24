def distance_toilettes(marches, hauteur):
    # calculer la distance parcourue par le gardien pour descendre les marches
    distance_descendue = marches * hauteur / 100
    # calculer la distance parcourue par le gardien pour remonter les marches
    distance_remontee = marches * hauteur / 100
    # calculer la distance totale parcourue par jour
    distance_jour = 2 * (distance_descendue + distance_remontee)
    # calculer la distance totale parcourue par semaine
    distance_semaine = 7 * distance_jour
    # formater la chaîne de sortie
    message = "Pour {} marches de {} cm, le gardien parcours {:.2f} m par semaine.".format(marches, hauteur, distance_semaine)
    # afficher le résultat
    print(message)

distance_toilettes(100, 20)
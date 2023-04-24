#Job8

def aliments(type, saison):

    if   (type == 'fruits' and saison == 'hiver'):
        print("orange, mandarine et kiwi")
    elif (type == 'fruits' and saison == 'été'):
        print("Poire, Fraise , Cassis")
    elif (type == 'legumes' and saison == 'hiver'):
        print("carotte, topinambour, endive")
    elif (type == 'legumes' and saison == 'été'):
        print("artichaut, aubergine,navet")
    else :
        print("Les aliments et la saison choisis sont incorrects")

aliments("legumes", "été")

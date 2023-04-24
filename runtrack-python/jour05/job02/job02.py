def draw_rectangle(width, height):
    # dessiner la première ligne
    print('-' * width)

    # dessiner les lignes du milieu
    for i in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # dessiner la dernière ligne
    print('-' * width)
draw_rectangle(10, 3)
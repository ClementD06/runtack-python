def chiffrement_cesar(message, decalage):
    message_chiffre = ''
    for lettre in message:
        # Convertir la lettre en caractère ASCII
        ascii_val = ord(lettre)
        # Appliquer le décalage au caractère ASCII
        ascii_val_decale = ascii_val + decalage
        # Gérer les dépassements en cas de caractères en dehors de l'alphabet
        if ascii_val_decale > 122:
            ascii_val_decale -= 26
        elif ascii_val_decale < 97:
            ascii_val_decale += 26
        # Ajouter le caractère décalé au message chiffré
        message_chiffre += chr(ascii_val_decale)
    return message_chiffre

message_chiffre = chiffrement_cesar("LaPlateforme", 3)
print(message_chiffre)
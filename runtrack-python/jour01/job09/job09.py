s = "bonjour le monde"
letter = "e"
 
for i, c in enumerate(s):
    if c == letter:
        print("e est présent à l'indice ", i+1)
    else:
        print("e absent à l'indice ", i+1)

